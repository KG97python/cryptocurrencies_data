import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import requests
import lxml
import csv

# Built this module to obtain the data I need from CoinMarketCap.

def top100_crypto():
    resp = requests.get('https://coinmarketcap.com/all/views/all/')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    # "Table" in coinmarketcap is not named, So i find the div before it.
    table = soup.find('div', {'class': 'cmc-table__table-wrapper-outer'})
    # then I tell bs4 to find the tbody after that.
    table_sorted = table.find_next('tbody')

    names = []
    symbols = []
    marketcaps = []
    prices = []
    volumes = []

    for row in table_sorted.findAll('tr')[:100]:
        name = row.findAll('td')[1].text
        names.append(name)
        symbol = row.findAll('td')[2].text
        symbols.append(symbol)
        marketcap = row.findAll('td')[3].text
        marketcaps.append(marketcap)
        price = row.findAll('td')[4].text
        prices.append(price)
        volume = row.findAll('td')[6].text
        volumes.append(volume)

    with open("crypto_data.csv", 'w', newline='') as f:
        columns = ['Name', 'Symbol', 'Marketcap' 'Price', 'Volume']
        the_writer = csv.DictWriter(f, fieldnames=columns)
        the_writer.writeheader()
        n = 0
        for i in range(100):
            the_writer.writerow({'Name': names[n], 'Symbol': symbols[n], 'Marketcap': marketcaps, 'Price': prices[n], 'Volume': volumes[n] })
            n += 1

top100_crypto()