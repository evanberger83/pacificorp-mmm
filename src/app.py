import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="PacifiCorp MMM Dashboard", layout="wide")

st.title("⚡ Marketing Mix Model Dashboard")
st.markdown("Estimate channel performance and optimize budget allocation")

# Load data
df = pd.read_csv("data/synthetic_data.csv")

# Sidebar controls
st.sidebar.header("Controls")

budget = st.sidebar.slider("Total Budget", 100, 5000, 1000)

channels = ["tv", "search", "social", "email"]

allocations = {}
for ch in channels:
    allocations[ch] = st.sidebar.slider(f"{ch} allocation", 0, 100, 25)

# Normalize allocation
total_alloc = sum(allocations.values())
allocations = {k: v / total_alloc * budget for k, v in allocations.items()}

# Simple response curves (demo)
def response(x, a=0.05):
    return a * np.log1p(x)

results = {ch: response(val) for ch, val in allocations.items()}

# Display
col1, col2 = st.columns(2)

with col1:
    st.subheader("Budget Allocation")
    st.bar_chart(pd.DataFrame(allocations, index=["Budget"]))

with col2:
    st.subheader("Estimated Returns")
    st.bar_chart(pd.DataFrame(results, index=["Return"]))

st.subheader("Raw Data Preview")
st.dataframe(df.head())
