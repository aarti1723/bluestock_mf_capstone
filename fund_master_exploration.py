import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("===== FUND HOUSES =====")
print(df["fund_house"].unique())

print("\n===== CATEGORIES =====")
print(df["category"].unique())

print("\n===== SUB CATEGORIES =====")
print(df["sub_category"].unique())

print("\n===== RISK GRADES =====")
print(df["risk_category"].unique())