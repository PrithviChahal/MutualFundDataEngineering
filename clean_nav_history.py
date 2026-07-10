import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert Date type
df["date"] = pd.to_datetime(df["date"])

# Sorting
df = df.sort_values(by=["amfi_code","date"])

# Forward Fill NAV values
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Removed Duplicates
print("Duplicated rows before cleaning :",df.duplicated().sum())

df = df.drop_duplicates()

print("Duplicated rows after cleaning :", df.duplicated().sum())

# Validate NAV
invalid_nav = df[df["nav"] <= 0]

print("Invalid NAV Rows i.e. NAV value is equal to 0 or Negative :",len(invalid_nav))

df = df[df["nav"] > 0]

# Saved cleaned file
df.to_csv(
    "data/processed/nav_history_cleaned.csv",
    index=False
)

print("Cleaned NAV history saved successfully...")


