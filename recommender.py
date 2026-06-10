import pandas as pd

performance = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

risk = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

recommend = performance[
    performance["risk_grade"] == risk
]

recommend = recommend.nlargest(
    3,
    "sharpe_ratio"
)

print("\nTop Fund Recommendations\n")

print(
    recommend[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ]
)