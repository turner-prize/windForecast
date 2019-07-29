import requests
from datetime import datetime

r = requests.get("https://api.darksky.net/forecast/{API KEY HERE}/49.1671,-2.0837")
resp = r.json()
winds=resp['hourly']
now = datetime.now()
windList = []
for i in winds['data']:
    ts = int(i['time'])
    dt = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    dt2 = datetime.utcfromtimestamp(ts)
    if dt2.day == now.day:
        windList.append(i['windSpeed'])

wAverage= sum(windList) / len(windList)
print(f'average windspeed for the afty is {wAverage:.2f}')
