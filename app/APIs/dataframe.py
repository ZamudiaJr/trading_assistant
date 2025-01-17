import requests
import pandas as pd
from decouple import config

api_key = config('AV_API_KEY')
symbol = "EUR/USD"  # Par de divisas
url = f"https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=EUR&to_symbol=USD&interval=5min&apikey={api_key}"

response = requests.get(url)
data = response.json()

# Convertir los datos a un DataFrame
df = pd.DataFrame.from_dict(data["Time Series FX (5min)"], orient="index")
df.columns = ["open", "high", "low", "close"]
df = df.astype(float)
df.index = pd.to_datetime(df.index)
df = df.sort_index()
print(df.head())