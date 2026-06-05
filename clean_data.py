import pandas as pd

# NAV History
nav = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date
nav["date"] = pd.to_datetime(nav["date"])

# Sort
nav = nav.sort_values(["amfi_code", "date"])

# Remove duplicates
nav = nav.drop_duplicates()

# Keep only positive NAV
nav = nav[nav["nav"] > 0]

# Forward fill missing NAV
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# Save cleaned file
nav.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)

print("NAV cleaned successfully!")


# =====================================
# INVESTOR TRANSACTIONS CLEANING
# =====================================

txn = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Fix date format
txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

# Standardize transaction type
txn["transaction_type"] = (
    txn["transaction_type"]
    .str.upper()
    .str.strip()
)

# Keep only valid amounts
txn = txn[
    txn["amount_inr"] > 0
]

# Check KYC values
print("\nKYC Status Values:")
print(txn["kyc_status"].unique())

# Save cleaned file
txn.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

print("Transactions cleaned successfully!")

# =====================================
# SCHEME PERFORMANCE CLEANING
# =====================================

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

# Return columns numeric banayein
return_cols = [
    'return_1yr_pct',
    'return_3yr_pct',
    'return_5yr_pct',
    'benchmark_3yr_pct'
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors='coerce'
    )

# Expense ratio anomalies (0.1% - 2.5%)
anomalies = perf[
    (perf['expense_ratio_pct'] < 0.1)
    |
    (perf['expense_ratio_pct'] > 2.5)
]

print("\nExpense ratio anomalies:", len(anomalies))

# Save cleaned file
perf.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

print("Scheme performance cleaned successfully!")

# =====================================
# COPY REMAINING DATASETS
# =====================================

other_files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in other_files:
    df = pd.read_csv(f"data/raw/{file}")

    cleaned_name = file.replace(
        ".csv",
        "_cleaned.csv"
    )

    df.to_csv(
        f"data/processed/{cleaned_name}",
        index=False
    )

print("Remaining datasets copied successfully!")