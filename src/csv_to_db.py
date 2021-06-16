import sqlite3
import csv
from urllib.request import pathname2url

try:

    with open('../name_crypto_2021-06-02_11:24:44.991497.csv') as dat:
        dr = csv.DictReader(dat)
        name_data = [(i['name'], 
            i['nickname']) for i in dr] 
  
        market_data = [(i['price'], 
            i['daily_percent'], 
            i['weekly_percent'], 
            i['market_cap'], 
            i['volume'], 
            i['circulating_supply']) for i in dr]

    try:
        db = 'file:{}?mode=rw'.format(pathname2url('scraper.db'))
        con = sqlite3.connect(db, uri=True)
    except sqlite3.OperationalError:
        print('database does not exist')
    # handle missing database case
    cur = con.cursor()

    #cur.execute('''CREATE TABLE crypto_data
    #                (name text, 
    #                nickname text,
    #                id real PRIMARY KEY
    #                );''')

    #cur.execute('''CREATE TABLE market_data
    #                (time_scraped text,
    #                id real,
    #                price real, 
    #                daily_percent text, 
    #                weekly_percent text,
    #                market_cap real,
    #                volume real,
    #                circulating_supply text,
    #                FOREIGN KEY(id) REFERENCES crypto_data(id)
    #                );''')

    cur.executemany("insert into crypto_data (name, nickname) VALUES (?, ?);", name_data)
    cur.executemany(
        "insert into market_data (time_scraped, price, daily_percent, weekly_percent,market_cap ,volume,circulating_supply) VALUES (?, ?,?,?,?,?,?);", market_data)
    

except sqlite3.Error as error:
    print('Error occured - ', error)
finally:
    con.close()