import requests
from pprint import pprint as print

sura = 1
oyat = 4
url_sura = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/{sura}.json"
url_oyat = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/{sura}/{oyat}.json"

r=requests.get(url_oyat)
res = r.json()
rr = requests.get(url_oyat)
# print(r.status_code)
# print(rr.json())
print(res['text'])