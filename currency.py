"""Currency convertor using Python and freecurrencyconvertorAPI"""

import os
import requests
import dotenv
dotenv.load_dotenv()


api_key = os.environ['API_KEY']
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}"

def convert_currency(start, currencies):
    """Function takes base and target currency and converts it using the API key"""
    url = f"{BASE_URL}&base_currency={start}&currencies={currencies}"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        return data["data"]
    except:
        print("Invalid Currency.")
        return None

while True:
    first = input("Enter the base currency (q for quit): ").upper()
    if first == "Q":
        break
    amount = float(input("Enter the amount: "))
    second = input("Enter target currency\
        (seperate multiple currencies with comma and no spaces):").upper()
    data_return = convert_currency(first, second)
    if not data_return:
        continue

    for ticker, value in data_return.items():
        print(f"{ticker}: {amount * value:.2f}")
