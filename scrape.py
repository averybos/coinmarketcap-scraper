
from bs4 import BeautifulSoup
import asyncio

from pyppeteer import launch
import pandas as pd

name = []
price = []
daily_percent = []
weekly_percent = []
market_cap = []
volume = []
circulating_supply = []

async def main():

    browser = await launch(headless=True)
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
        price.append(a[1].text)  
        daily_percent.append(span[2].text)   
        weekly_percent.append(span[4].text)  

        long = p[3].text.split('$')
        market_cap.append('$'+long[2])   

        volume.append(p[4].text)      
        circulating_supply.append(p[6].text)
    print(name)  

    dict = {'name':name,
            'price': price,
            'daily_percent': daily_percent,
            'weekly_percent': weekly_percent,
            'market_cap':market_cap,
            'volume':volume,
            'circulating_supply':circulating_supply
    }

    df = pd.DataFrame(dict)
    df.to_csv('crypto.csv')

    await browser.close() 
    

asyncio.get_event_loop().run_until_complete(main())
