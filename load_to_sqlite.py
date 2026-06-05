from sqlalchemy import create_engine
import pandas as pd

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned datasets

pd.read_csv(
    "data/processed/01_fund_master_cleaned.csv"
).to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
).to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/03_aum_by_fund_house_cleaned.csv"
).to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
).to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
).to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("Database created successfully!")