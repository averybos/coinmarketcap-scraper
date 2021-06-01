import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import urllib.request
import re
import asyncio
import os
from pyppeteer import launch


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
    for trs in soup.select('tr'):
        print (trs.text)

    await browser.close()
    

asyncio.get_event_loop().run_until_complete(main())
