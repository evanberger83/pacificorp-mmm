# ⚡ PacifiCorp Marketing Mix Modeling (MMM)

## Overview
This project implements a **Bayesian hierarchical Marketing Mix Model (MMM)** to quantify the impact of marketing channels on:

- Customer acquisition (new connections)
- Energy program enrollments
- Demand response participation

The model simulates a real-world utility marketing environment with regional variation and external drivers like weather.

---

## Key Features

- Bayesian MMM using PyMC
- Adstock transformation (lagged media effects)
- Saturation modeling (diminishing returns)
- Hierarchical modeling across regions
- Budget optimization

---

## Dataset

Synthetic dataset with:
- Weekly data over 3 years
- Multiple regions (UT, OR, WY, ID)
- Media channels: TV, Search, Social, Email
- External variables:
  - Heating Degree Days (HDD)
  - Cooling Degree Days (CDD)
  - Unemployment rate

---

## Model

The model estimates:

y_t = β0 + Σ βc * f(Adstock(media_c)) + γX + ε

Where:
- f() = saturation function
- X = control variables (weather, macro)

---

## Results

- Channel-level ROI estimates
- Response curves (diminishing returns)
- Optimal budget allocation

---

## How to Run

```bash
pip install -r requirements.txt
python src/data_generation.py
python src/model.py
