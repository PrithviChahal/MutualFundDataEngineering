import pandas as pd 
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

print("Database created successfully!")

nav = pd.read_csv(
    "data/processed/nav_history_cleaned.csv"
)

transactions = pd.read_csv(
    "data/processed/investor_transaction_cleaned.csv"
)

performance = pd.read_csv(
    "data/processed/scheme_performance_cleaned.csv"
)

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)



fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)


nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fund_transactions",
    engine,
    if_exists="replace",
    index= False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)


print("Dim_fund rows:", len(fund_master))
print("Fact_nav rows:", len(nav))
print("Fact_transactions rows:", len(transactions))
print("Fact_performance rows:", len(performance))

print("\nDatabase loaded successfully!")