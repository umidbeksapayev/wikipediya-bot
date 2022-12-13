import requests
import json
city = 'Xiva'
url = f"https://dailyprayer.abdulrcs.repl.co/api/{city}"
r = requests.get(url)
print(r.json())