import numpy as np
import pandas as pd

np.random.seed(42)

weeks = 156
regions = ["UT", "OR", "WY", "ID"]

data = []

for region in regions:
    base = np.random.randint(200, 400)
    
    for t in range(weeks):
        tv = np.random.gamma(5, 20)
        search = np.random.gamma(3, 15)
        social = np.random.gamma(2, 10)
        email = np.random.gamma(1, 5)

        hdd = np.random.normal(30, 10)
        cdd = np.random.normal(20, 8)
        unemployment = np.random.uniform(3, 7)

        noise = np.random.normal(0, 10)

        y = (
            base
            + 0.05 * tv
            + 0.08 * search
            + 0.04 * social
            + 0.02 * email
            + 0.3 * hdd
            + 0.2 * cdd
            - 2 * unemployment
            + noise
        )

        data.append([
            region, t, tv, search, social, email,
            hdd, cdd, unemployment, y
        ])

df = pd.DataFrame(data, columns=[
    "region", "week", "tv", "search", "social", "email",
    "hdd", "cdd", "unemployment", "target"
])

df.to_csv("data/synthetic_data.csv", index=False)
print("Data saved.")
