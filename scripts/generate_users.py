import pandas as pd

# Load data
users = pd.read_csv("data/raw/users.csv")
applications = pd.read_csv("data/raw/applications.csv")

# Step 1: total users
total_users = users["user_id"].nunique()

# Step 2: applied users
applied_users = applications["user_id"].nunique()

# Step 3: funnel table
funnel = pd.DataFrame({
    "Step": ["Signed Up", "Applied"],
    "Users": [total_users, applied_users]
})

# Step 4: conversion %
funnel["Conversion %"] = (funnel["Users"] / total_users) * 100

# Print
print("\nActivation Funnel:\n")
print(funnel)

# Save CSV ✅
funnel.to_csv("outputs/activation_funnel.csv", index=False)