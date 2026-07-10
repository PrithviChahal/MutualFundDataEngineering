import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Convert Date type
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"].str.strip().str.title()
)

df["transaction_type"] = df["transaction_type"].replace({
    "Sip" : "SIP",
    "Lumpsum" : "Lumpsum",
    "Redemption" : "Redemption"
})

# Validate transactions types
valid_types = [
    "SIP",
    "Lumpsum",
    "Redemption"
]

invalid_types = df[~df["transaction_type"].isin(valid_types)]

print("Invalid transaction types :",len(invalid_types))


# Validate KYC status
valid_types2 = [
    "Verified",
    "Pending"
]

invalid_types2 = df[~df["kyc_status"].isin(valid_types2)]

print("Invalid KYC values :",len(invalid_types2))


# Validate amount
df = df[df["amount_inr"] > 0]


# Saved clean file
df.to_csv(
    "data/processed/investor_transaction_cleaned.csv",
    index= False)

print("Cleaned investor transctions saved successfully...")

print(df.columns)
print(df.info)

