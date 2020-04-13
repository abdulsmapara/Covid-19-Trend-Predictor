import json
import pandas as pd
f = open("india_weather_apr.json")
data = json.load(f) 
# print(json.dumps(data, indent=2))
f.close()
path = "../Timeseries-Data/test_data.csv"
df = pd.read_csv(path)

temp_data = {}
for d in data['data']['weather']:
	year, month, day = d['date'].split("-")
	temp_data[(year,int(month),int(day))] = (d['mintempC'], d['maxtempC'])
print(temp_data.items())
for i, date, _, _ in zip(df['Index'], df['Date'], df['Min_Temp'],df['Max_Temp']):
	month, day, year = date.split("/")
	if month == "4" and int(day) <= 13:
		df.at[i,'Min_Temp'] = temp_data[(year,int(month),int(day))][0]
		df.at[i,'Max_Temp'] = temp_data[(year,int(month),int(day))][1]

df.to_csv(path, index=False)
