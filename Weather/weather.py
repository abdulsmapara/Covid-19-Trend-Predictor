import requests
import json
URL = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx"
key = "c1376ebc189c472bb3784906200904"
PARAMS = {
	'key': key,
	'q'  : 'Wuhan, China',
	'date': '2020-04-01',
	'enddate': '2020-04-09',
	'format': 'json'
}

r = requests.get(url = URL, params = PARAMS)
data = r.json()
print(data)

with open('china_weather_apr.json', 'w') as f:
	json.dump(data, f)
