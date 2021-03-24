import pandas as pd
import requests
import json
import plotly.graph_objects as go
from API_Credentials import API_Key
from urllib.request import urlopen

# Company profile endpoint
profile_endpoint = fr"https://financialmodelingprep.com/api/v3/profile/AAPL?apikey={API_Key}"
# Make request
profile_content = requests.get(url = profile_endpoint)
# Convert JSON
profile_data = profile_content.json()
print(profile_data)

# Insider Trading
insider_endpoint = fr"https://financialmodelingprep.com/api/v4/insider-trading?symbol=AAPL&limit=100&apikey={API_Key}"
insider_content = requests.get(url = insider_endpoint)
insider_data = insider_content.json()
print(insider_data)

# Historical Price
historical_endpoint = fr"https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?apikey={API_Key}"
historical_content = requests.get(url = historical_endpoint)
historical_data = historical_content.json()
print(historical_data)

# Technical Indicators
# Can be modified for SMA EMA WMA DEMA TEMA williams RSI ADX Stdev
indicator_endpoint = fr"https://financialmodelingprep.com/api/v3/technical_indicator/daily/AAPL?period=10&type=ema&apikey={API_Key}"
indicator_content = requests.get(url = indicator_endpoint)
indicator_data = indicator_content.json()
print(indicator_data)

# Commodities Historical
commodities_endpoint = fr"https://financialmodelingprep.com/api/v3/historical-price-full/commodity/ZGUSD?apikey={API_Key}"
commodities_content = requests.get(url = commodities_endpoint)
commodities_data = commodities_content.json()
print(commodities_data)

# Sector Performance
sector_endpoint = fr"https://financialmodelingprep.com/api/v3/stock/sectors-performance?apikey={API_Key}"
sector_content = requests.get(url = sector_endpoint)
sector_data = sector_content.json()
print(sector_data)

# todo Figure out why Earnings Date is not printing. Response is successfully received but data is unable to print
# Earnings Calendar
earnings_endpoint = rf"https://financialmodelingprep.com/api/v3/historical/earning_calendar/AAPL?apikey={API_Key}"

earnings_content = requests.get(url = earnings_endpoint)
#print(earnings_content)


# todo Figure out why Financial Growth is not printing. Response is successfully received but data is unable to print
# Financial Growth
growth_endpoint =  rf"https://financialmodelingprep.com/api/v3/financial-growth/AAPL?apikey={API_Key}"

growth_content = requests.get(url = growth_endpoint)
#print(growth_content)

