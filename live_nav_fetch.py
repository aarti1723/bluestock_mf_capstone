import requests
import pandas as pd
import os

os.makedirs("data/raw/live_nav", exist_ok=True)

schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url, timeout=20)

        if response.status_code == 200:

            data = response.json()

            nav_df = pd.DataFrame(data["data"])

            file_path = f"data/raw/live_nav/{fund_name}.csv"

            nav_df.to_csv(file_path, index=False)

            print(f"Saved: {fund_name}")

        else:
            print(f"Failed: {fund_name} | Status: {response.status_code}")

    except Exception as e:
        print(f"Error in {fund_name}: {e}")