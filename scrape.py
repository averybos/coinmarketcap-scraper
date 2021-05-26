import requests
from bs4 import BeautifulSoup

res = requests.get('https://coinmarketcap.com')
soup = BeautifulSoup(res.content, 'html.parser')

txt = res.text
status = res.status_code
title = soup.title.text

print(status, title)

