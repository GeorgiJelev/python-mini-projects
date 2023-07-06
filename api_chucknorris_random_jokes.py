import json
import requests


url = "https://api.chucknorris.io/jokes/random"

data = requests.get(url)
data = data.json()
print(data['value'])
