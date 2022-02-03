import requests
from datetime import datetime
from pprint import pprint

r = requests.get('https://api.openwathermap.org/data/2.5/weather?q=Buenos%20Aires&units=metris&lang=es&appid=6ce13bc6d5a965e991adaea8fce8676a')
data = r.Json()
pprint(data)

print("\n\nFecha y hora del pronóstico:")
print(datetime.fromtimestamp(data['dt']))

print("\n\nSalida del sol")
print(datetime.fromtimestamp(data['sys'] ['sunrise']))
print("\n\nPuesta del Sol:")
print(datetime.fromtimestamp(data['sys'] ['sunset']))

r = requests.get('https://api.openwathermap.org/data/2.5/onecall?')