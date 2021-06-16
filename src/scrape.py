
from bs4 import BeautifulSoup
import asyncio

from pyppeteer import launch
import pandas as pd
from datetime import datetime
from datetime import timedelta

'''Author: Avery Bostick'''

name = []
nickname = []
price = []
daily_percent = []
weekly_percent = []
market_cap = []
volume = []
circulating_supply = []

async def main():
    '''
    This is an asynchronous function that calls a website (coinmarketcap.com) 
    in order to collect certain items of data from it.

    '''

    browser = await launch()
    page = await browser.newPage()
    page_path = "https://coinmarketcap.com"
    await page.goto(page_path)

    # this 200 number is close enough to the amount of time
    # it takes to scroll all the way down
    for i in range(200):
        # pyppeteer scrolling down on the headless browser
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

        # looking through the developer console on chrome, 
        # this is where each piece of data is to be found
        # and collected to be put in a list
        name.append(p[1].text)
        nickname.append(p[2].text)
        price.append(a[1].text)  
        daily_percent.append(span[2].text)   
        weekly_percent.append(span[4].text)  

        long = p[3].text.split('$')
        market_cap.append('$'+long[2])   

        volume.append(p[4].text)      
        circulating_supply.append(p[6].text) 

    # finding exact time of data collection
    # in order to differentiate each csv file name
    time = datetime.now()
    x = timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)
    date = str(time).split(' ')[0]

    # final dictionary to store all data
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

    # simply converted to dataframe and then csv file from there
    df = pd.DataFrame(dict)
    df.to_csv('top_100_'+date+'_'+str(x)+'.csv')  

    await browser.close() 
    
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())

