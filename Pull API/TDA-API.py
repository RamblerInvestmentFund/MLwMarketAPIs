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

#Additional API pulls

#### Get Hours for a Single Market
#Valid markets are EQUITY, OPTION, FUTURE, BOND, or FOREX
def retrieveSingleMarketHours(market):
    endpoint = 'https://api.tdameritrade.com/v1/marketdata/{market}/hours'
    full_url = endpoint.format(market=market)
    page = requests.get(url=full_url,
                        params={'apikey' : 'NXHAYFIAP0TXGN9NFR27DDAF7QSNQPHA'})
    content = json.loads(page.content)
    return content
####

#### Retrieve Ticker Price History with specific parameters (2day/1min chart)
def retrieve2Day1MinChart(ticker):
    endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory'
    full_url = endpoint.format(stock_ticker=ticker)
    page = requests.get(url=full_url,
                        params={'apikey' : 'NXHAYFIAP0TXGN9NFR27DDAF7QSNQPHA',
                                'period' : '2',
                                'periodType' : 'day',
                                'frequency' : '1',
                                'frequencyType' : 'minute'})
    content = json.loads(page.content)
    return content
####

#### Retrieve Multiple Ticker Quote
def retrieveMultipleQuotes(symbols):
    full_url = 'https://api.tdameritrade.com/v1/marketdata/quotes'
    page = requests.get(url=full_url,
                        params={'apikey' : 'NXHAYFIAP0TXGN9NFR27DDAF7QSNQPHA', 'symbol' : symbols})
    content = json.loads(page.content)
    return content


#### Retrieve Movers
#Valid index can be $COMPX, $DJI, $SPX.X
def retrieveMovers(index):
    endpoint = 'https://api.tdameritrade.com/v1/marketdata/{index}/movers'
    full_url = endpoint.format(index=index)
    page = requests.get(url=full_url,
                        params={'apikey' : 'NXHAYFIAP0TXGN9NFR27DDAF7QSNQPHA', 'direction' : 'up', 'change' : 'percent'})
    content = json.loads(page.content)
    return content
####

#### Test Output
print(retrieveTickerQuote('AAL'))
print(retrieveTickerPriceHistory('AAPL'))
print(retrieveTickerOptionChain('AMZN'))
print(retrieveSingleMarketHours('FOREX'))
print(retrieve2Day1MinChart("APPL"))
print(retrieveMultipleQuotes("GOOG,MSFT,APPL,PINS"))
print(retrieveMovers('$COMPX'))