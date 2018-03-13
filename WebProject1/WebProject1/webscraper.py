from bs4 import BeautifulSoup
import requests

url = "portview.agencies.vopak.com/ords/f?p=PUB:1:0::::P1_OFE_CODE:AWR"
r = requests.get("http://" + url)
data = r.text
soup = BeautifulSoup(data)
list = []

for link in soup.find_all('td'):
    if link.get("headers") == ['ARRIVAL'] and link.string != '\xa0':
        list.append(link.string)

print(list)
