import json
import requests


binance_url = "https://api.chucknorris.io/jokes/random"

data = requests.get(binance_url)
data = data.json()
print(data['value'])
