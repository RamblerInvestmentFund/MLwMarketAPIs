# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:55:32 2021

@author: Ashton Hansen
"""

!pip install finnhub-python

import requests as req

# You need to create an account to get a token; I'm using one of mine below
request1 = req.get('https://finnhub.io/api/v1/quote?symbol=AAPL&token=sandbox_c0grqpv48v6ttm1smfr0')
# As seen above, you will need a URL and need to change the symbol as needed.

# Will return the current OHLC prices, as well as previous close and time
aapl_ohlc = request1.json()
print(aapl_ohlc)

## Candle
request2 = req.get('https://finnhub.io/api/v1/stock/candle?symbol=AAPL&resolution=1&from=1605543327&to=1605629727&token=c0grqpv48v6ttm1smfqg')
print(request2.json())