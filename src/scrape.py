
from bs4 import BeautifulSoup
import asyncio

from pyppeteer import launch
import pandas as pd
from datetime import datetime

name = []
nickname = []
price = []
daily_percent = []
weekly_percent = []
market_cap = []
volume = []
circulating_supply = []

async def main():

    browser = await launch()
    page = await browser.newPage()
    page_path = "https://coinmarketcap.com"
    await page.goto(page_path)

    for i in range(200):
        await page.keyboard.press('ArrowDown')
        
    page_content = await page.content() 
    soup = BeautifulSoup(page_content, 'html.parser')

    i=0
    for trs in soup.select('tr'):
        if i==0:
            i += 1
            continue

        p = trs.select('p')
        a = trs.select('a')
        span = trs.select('span')

        name.append(p[1].text)
        nickname.append(p[2].text)
        price.append(a[1].text)  
        daily_percent.append(span[2].text)   
        weekly_percent.append(span[4].text)  

        long = p[3].text.split('$')
        market_cap.append('$'+long[2])   

        volume.append(p[4].text)      
        circulating_supply.append(p[6].text) 

    time = datetime.now()
    date = str(time).split(' ')[0]
    t = str(time).split(' ')[1]

    dict = {
            'name': name,
            'nickname': nickname,
            'price': price,
            'daily_percent': daily_percent,
            'weekly_percent': weekly_percent,
            'market_cap': market_cap,
            'volume': volume,
            'circulating_supply': circulating_supply,
            'time': time
    }

    df = pd.DataFrame(dict)
    df.to_csv('name_crypto_'+date+'_'+t+'.csv')  

    await browser.close() 
    

asyncio.get_event_loop().run_until_complete(main())
