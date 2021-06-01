this is a repo by avery bostick that collects data from coinmarketcap.com, a cryptocurrency website.

using python

I used the python scraping library BeautifulSoup, and at first was getting a weird error where I would collect the data from the top 10 cryptos, and the rest of the 100 would have missing data. Upon further inspection, it was not BeautifulSoup's parsing giving me the error, but the webpage itself.

the key to figuring out how to take the data from this website was not the scraping itself, but figuring out how to collect data from a lazy loading site.

I found another library called Pyppeteer, a python port of puppeteer, a javascript headless chromium automation library.

essentially I used a "virtual" keyboard that would scroll to the bottom of the page to make sure all data rows were loaded, before creating the page content variable and then having BeautifulSoup parse that.

from there, I used Pandas to convert all data into one DataFrame, and then export to a csv file.
