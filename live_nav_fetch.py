import requests
import pandas as pd


url = " https://api.mfapi.in/mf/125497"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv("data/raw/live_nav_125497.csv",index=False)

    print("CSV saved successfully!")

else:

    print(f"Failed to fetch 125497. Status Code:{response.status_code}")



schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():
    print(f"Fetching {name}...")

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        nav_df.to_csv(f"data/raw/{name}.csv" , index= False)

        print(f"{name}.csv saved successfully!")

    else:
        print(f"Failed to fetch {name}. Status Code:{response.status_code}")


print("\nAll Nav Files downloaded successfully!")            






