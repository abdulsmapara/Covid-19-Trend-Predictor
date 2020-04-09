import requests
import json
URL = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx"
key = ""
PARAMS = {
	'key': key,
	'q'  : 'Australia',
	'date': '2020-01-22',
	'enddate': '2020-01-31',
	'format': 'json'
}

r = requests.get(url = URL, params = PARAMS)
data = r.json()
print(data)

with open('australia_weather_jan.json', 'w') as f:
	json.dump(data, f)
