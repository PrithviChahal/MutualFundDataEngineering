import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Validate Numeric return
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

print("Missing values in return columns :" , df[return_cols].isnull().sum())

print("---------------------------------------------------")

# Flag anomalies
anomalies = pd.DataFrame()

for col in return_cols:
    temp = df[(df[col] < -100) | (df[col] > 200)]

    anomalies = pd.concat([anomalies,temp])

anomalies = anomalies.drop_duplicates()

print("Anomalous Rows :", len(anomalies))

print("------------------------------------------------------")

print(anomalies)

print("-------------------------------------------------------")


# Validate expense ratio (0.1% – 2.5%)
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1 ) | (df["expense_ratio_pct"] > 2.5)
]

print("Invalid expense ratio rows :", len(invalid_expense))

print("------------------------------------------------------")


# Saved clean file
df.to_csv("data/processed/scheme_performance_cleaned.csv" , index= False)

print("scheme_performance cleaned successfully!")