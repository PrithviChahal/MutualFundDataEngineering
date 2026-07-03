import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("Total AMFI Codes in fund master:", len(fund_codes))
print("Total AMFI Codes in nav history:", len(nav_codes))

if len(missing_codes) == 0:
    print("\nAll AMFI codes in fund master exist in nav_history")
else:
    print("\n Missing AMFI codes:")
    print(missing_codes)
    print("\nTotal Missing Codes:", len(missing_codes))    
