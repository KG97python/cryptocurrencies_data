import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import lxml
import csv
from plotly.graph_objs import Bar
from plotly import offline


df = pd.read_csv("crypto_data.csv")
cap = df['Marketcap']
names = df['Symbol']
b = 1000000000
m = 1000000
new = []

# I need to turn huge number like '$171,676,306,564' to small symbol like '$171.7B'
# in order to do that I need to turn string to integer first.

def turn_to_integer():
    for i in cap:
        # get rid of money sign
        symbol = i.replace('$', '')
        # get rid of commas
        commas = symbol.replace(',', '')
        final = int(commas)
        new.append(final)

# Now I turn billions to B and millions to M
marketcaps = []

def convert_symbol():
    for i in new:
        if i > 1000000000:
            devision = i / b
            rounded = round(devision, 1)
            result = '$' + str(rounded) + 'B'
            marketcaps.append(result)
        else:
            devisions = i / m
            roundeds = round(devisions, 1)
            results = '$' + str(roundeds) + 'M'
            marketcaps.append(results)
    print(marketcaps)


def visual():
    symbols = []
    marketcaps.reverse()
    for i in names:
        symbols.append(i)
    symbols.reverse()
    data = [{
        'type': 'bar',
        'x': symbols,
        'y': marketcaps,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.0, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6,
    }]

    my_layout = {
        'title': 'Top 100 crypto-currencies',
        'xaxis': {
            'title': 'Crypto-Symbols',
            'titlefont': {'size': 20},
            'tickfont': {'size': 14},
        },
        'yaxis': {
            'title': 'Marketcap',
            'titlefont': {'size': 20},
            'tickfont': {'size': 14},
        },
    }

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='python_repos.html')


def main_loop():
    turn_to_integer()
    convert_symbol()
    visual()


main_loop()