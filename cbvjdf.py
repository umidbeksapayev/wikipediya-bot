import requests
from pprint import pprint as print
app_id = "9f33f758"
app_key = "d6f0daea153dedd7c29638d9a2fc08bd"
language = "en-gb"
word_id = "football"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
print(r.status_code)
res = r.json()
# print(res)
print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'])
# print(res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile'])