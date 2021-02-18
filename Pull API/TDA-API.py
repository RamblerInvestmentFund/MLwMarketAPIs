# Pulling Data from TD Ameritrade API
# Anthony and Yandi

import requests
import json



def retreiveTickerQuote(ticker):
    endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/quotes?'
    full_url = endpoint.format(stock_ticker=ticker)
    page = requests.get(url=full_url,
                        params={'apikey' : 'NXHAYFIAP0TXGN9NFR27DDAF7QSNQPHA'})
    content = json.loads(page.content)
    return content

def retreiveTickerPriceHistory(ticker):
    endpoint = endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory'
    full_url = endpoint.format(stock_ticker=ticker)
    page = requests.get(url=full_url,
                        params={'apikey' : 'NXHAYFIAP0TXGN9NFR27DDAF7QSNQPHA'})
    content = json.loads(page.content)
    return content

def retreiveTickerOptionChain(ticker):
    endpoint = endpoint = 'https://api.tdameritrade.com/v1/marketdata/chains?&symbol={stock_ticker}'
    full_url = endpoint.format(stock_ticker=ticker)
    page = requests.get(url=full_url,
                        params={'apikey' : 'NXHAYFIAP0TXGN9NFR27DDAF7QSNQPHA'})
    content = json.loads(page.content)
    return content

print(retreiveTickerQuote('AAL'))
print(retreiveTickerPriceHistory('AAPL'))
print(retreiveTickerOptionChain('AMZN'))
