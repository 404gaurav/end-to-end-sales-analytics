"""
Sales Data Cleaning Script
Author: Gaurav Singh Rathore

Description:
This script performs basic data cleaning and feature engineering
on the sales dataset and exports the cleaned file.
"""

import pandas as pd


# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("sales/sales.csv", encoding="latin1")


# ==========================
# Data Cleaning
# ==========================

# Convert date columns to datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

# Remove duplicate records (if any)
df.drop_duplicates(inplace=True)

# ==========================
# Feature Engineering
# ==========================

# Create Shipping Duration (in days)
df["Shipping Duration"] = (df["Ship Date"] - df["Order Date"]).dt.days

# Extract Year, Month, Day from Order Date
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Day"] = df["Order Date"].dt.day


# ==========================
# Save Cleaned Dataset
# ==========================

df.to_csv("sales_cleaned.csv", index=False)

print("Data cleaning completed successfully.")
