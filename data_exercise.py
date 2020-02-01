import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests
import lxml

def top100_crypto():
    resp = requests.get('https://coinmarketcap.com/all/views/all/')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    # "Table" in coinmarketcap is not named, So i find the div before it.
    table = soup.find('div', {'class': 'cmc-table__table-wrapper-outer'})
    # then I tell bs4 to find the tbody after that.
    table_sorted = table.find_next('tbody')
    tickers = []
    for row in table_sorted.findAll('tr')[:100]:
        ticker = row.findAll('td')[2].text
        tickers.append(ticker + "-USD" + "\n")

    print(tickers)
top100_crypto()

def get_data_from_yahoo(reload_top100_crypto=False):
    if reload_top100_crypto:
        tickers = top100_crypto()
    else:
        with open("top100_cryptos", "rb") as f:
            tickers = pickle.load(f)

    if not os.path.exists('crypto_dfs'):
        os.makedirs('crypto_dfs')

    start = dt.datetime(2008, 1, 1)
    end = dt.datetime(2020, 1, 30)

    for ticker in tickers[:100]:
        print(ticker)
        if not os.path.exists('crypto_dfs/{}.csv'.format(ticker)):
            df = web.DataReader(ticker, 'yahoo', start, end)
            df.to_csv('crypto_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))
