# Pulling Data from TD Ameritrade API
# Anthony and Yandi

import requests
import json

#### Retrieve Ticker Quote
def retrieveTickerQuote(ticker):
    endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/quotes?'
    full_url = endpoint.format(stock_ticker=ticker)
    page = requests.get(url=full_url,
                        params={'apikey' : 'NXHAYFIAP0TXGN9NFR27DDAF7QSNQPHA'})
    content = json.loads(page.content)
    return content
#### 

#### Retrieve Ticker Price History
def retrieveTickerPriceHistory(ticker):
    endpoint = endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory'
    full_url = endpoint.format(stock_ticker=ticker)
    page = requests.get(url=full_url,
                        params={'apikey' : 'NXHAYFIAP0TXGN9NFR27DDAF7QSNQPHA'})
    content = json.loads(page.content)
    return content
####

#### Retrieve Ticker Option Chain
def retrieveTickerOptionChain(ticker):
    endpoint = endpoint = 'https://api.tdameritrade.com/v1/marketdata/chains?&symbol={stock_ticker}'
    full_url = endpoint.format(stock_ticker=ticker)
    page = requests.get(url=full_url,
                        params={'apikey' : 'NXHAYFIAP0TXGN9NFR27DDAF7QSNQPHA'})
    content = json.loads(page.content)
    return content
####

#### Test Output
print(retrieveTickerQuote('AAL'))
print(retrieveTickerPriceHistory('AAPL'))
print(retrieveTickerOptionChain('AMZN'))
