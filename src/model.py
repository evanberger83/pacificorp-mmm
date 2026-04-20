import pandas as pd
import pymc as pm
import numpy as np
from preprocessing import adstock, saturation

df = pd.read_csv("data/synthetic_data.csv")

# Apply transformations
for col in ["tv", "search", "social", "email"]:
    df[col + "_adstock"] = df.groupby("region")[col].transform(adstock)
    df[col + "_sat"] = saturation(df[col + "_adstock"])

X_media = df[[
    "tv_sat", "search_sat", "social_sat", "email_sat"
]].values

X_ctrl = df[["hdd", "cdd", "unemployment"]].values
y = df["target"].values

with pm.Model() as model:
    beta_media = pm.HalfNormal("beta_media", sigma=1, shape=X_media.shape[1])
    beta_ctrl = pm.Normal("beta_ctrl", mu=0, sigma=1, shape=X_ctrl.shape[1])
    intercept = pm.Normal("intercept", mu=0, sigma=10)

    mu = intercept + pm.math.dot(X_media, beta_media) + pm.math.dot(X_ctrl, beta_ctrl)

    sigma = pm.HalfNormal("sigma", sigma=10)
    y_obs = pm.Normal("y_obs", mu=mu, sigma=sigma, observed=y)

    trace = pm.sample(1000, tune=1000, target_accept=0.9)

print("Model training complete.")
