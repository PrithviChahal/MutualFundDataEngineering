import pandas as pd


df = pd.read_csv("data/raw/01_fund_master.csv")


print("\nFirst 5 Rows:")
print(df.head())


print("\nShape:")
print(df.shape)


print("\nColumns:")
print(df.columns.tolist())


print("\nUnique Fund Houses:")
print(df["fund_house"].unique())


print("\nUnique Categories:")
print(df["category"].unique())


print("\nUnique Sub Categories:")
print(df["sub_category"].unique())


print("\nUnique Risk Categories:")
print(df["risk_category"].unique())


print("\nNumber of Unique Fund Houses:", df["fund_house"].nunique())
print("Number of Categories:", df["category"].nunique())
print("Number of Sub Categories:", df["sub_category"].nunique())
print("Number of Risk Categories:", df["risk_category"].nunique())