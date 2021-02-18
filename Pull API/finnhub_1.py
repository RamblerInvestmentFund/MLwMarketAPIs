# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:55:32 2021

@author: Ashton Hansen, Avi Patel
"""
# Code source:
# https://finnhub.io/docs/api/introduction

import requests as req

# For .json files:

# Real-Time Quote:
# Will return the current OHLC prices, as well as previous close and time

# You need to create an account to get a token; I'm using one of mine below
request1 = req.get('https://finnhub.io/api/v1/quote?symbol=AAPL&token=sandbox_c0grqpv48v6ttm1smfr0')

# As seen above, you will need a URL and need to change the symbol as needed.
aapl_ohlc = request1.json()
print(aapl_ohlc)

## Candlestick Data (1yr):
## Also includes OHLC and timestamp; trade volume is also included
request2 = req.get('https://finnhub.io/api/v1/stock/candle?symbol=AAPL&resolution=1&from=1605543327&to=1605629727&token=sandbox_c0grqpv48v6ttm1smfqg')
aapl_candle = request2.json()
print(aapl_candle)

crypto = req.get('https://finnhub.io/api/v1/crypto/candle?symbol=BINANCE:BTCUSDT&resolution=D&from=1572651390&to=1575243390&token=sandbox_c0grqpv48v6ttm1smfr0')
print(r.json())
