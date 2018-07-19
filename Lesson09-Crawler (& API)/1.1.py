import json
import requests

url = 'https://www.metaweather.com/api/location/2306179/2018/7/18/'
taipei_weather_data = requests.get(url)
taipei_weather_data.encoding = 'utf-8' 

data = json.loads(taipei_weather_data.text)
print("creat weather time\t\t","weather state")
for i in range(1,len(data)):
    print(data[i]['created']+"\t "+data[i]['weather_state_name'])



#"woeid":2306179