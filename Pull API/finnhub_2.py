# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:10:21 2021

@author: Ashton Hansen
"""
# Code source:
# https://github.com/Finnhub-Stock-API/finnhub-python

# Just in case you need this for some reason, run what's below in terminal:
# pip install finnhub-python

import finnhub
import pandas as pd
from datetime import datetime

# Setup client
# This code uses Ashton's sandbox API key; make an account and use your own
finnhub_client = finnhub.Client(api_key="sandbox_c0grqpv48v6ttm1smfr0")

# Real-time Stock Quote
aapl_quote = finnhub_client.quote(symbol = 'AAPL')
print("Real-time Quote of AAPL:")
print(aapl_quote)
print(" ")

# Stock candlestick data
# Start/end dates are in unix
aapl_candles = finnhub_client.stock_candles(symbol = 'AAPL', 
                                            resolution = 'D', 
                                            _from = 1590988249, 
                                            to = 1591852249)

print(" Candlestick Data for AAPL:")
print(" ")

# Candlestick data length:
print("Length:", len(aapl_candles['c']))

# What is the timespan for that data?
start = int("1590988249")
print("Start:", datetime.utcfromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S'))

end = int("1591852249")
print("End:", datetime.utcfromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S'))
print(" ")
print(aapl_candles)
print(" ")

# Convert Candlestick data to Pandas Dataframe
print("Candlestick data as Data Frame:")
print(pd.DataFrame(aapl_candles))
print(" ")

# Tick Data (Premium/Paid Content)
# Will throw error if you try running this w/o right subscription
# print(finnhub_client.stock_tick('AAPL', '2020-03-25', 500, 0))

# Bid/Asking price
print("Bid/Asking price for AAPL")
print(finnhub_client.last_bid_ask('AAPL'))

print(" ")

# Crypto Candlestick Data
print("DOGE Candlestick data:")
doge_candles = finnhub_client.crypto_candles(symbol = 'DOGE', 
                                     resolution = 'D', 
                                     _from = 1590988249,
                                     to = 1591852249)
print(pd.DataFrame(doge_candles))
