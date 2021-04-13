import requests
import json
import csv
import pandas as pd

#### Create Empty CSV for data Transfer
def create_csv(tickers):
    df = pd.DataFrame()
    for i in tickers:
        written = df.to_csv(path_or_buf="/Users/anthonypeters/Desktop/Coding-Jobs-and-Projects/For-Projects/Projects-Python/MLwMarketAPIs/Pull API/TDA_YFIN_CSV/TDA_CSV/price_data_{ticker}.csv".format(ticker = i))
    return(written)
####

#### Retrieve Ticker Price History
def retrieveTickerPriceHistory(ticker):
    endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory'
    full_url = endpoint.format(stock_ticker=ticker)
    parameters = {'apikey' : 'NXHAYFIAP0TXGN9NFR27DDAF7QSNQPHA',
                        'periodType': 'month',
                        'period': 3,
                        'frequencyType': 'daily',
                        'frequency': 1}
    page = requests.get(url=full_url, params=parameters)
    content = json.loads(page.content)
    return content
####

#### Pull data and write to CSV
def pull_close(tickers):
    df = pd.DataFrame()

    for i in tickers:
        output = retrieveTickerPriceHistory(i)
        for j in output["candles"]:
            df = df.append(j, ignore_index=True)
        written = df.to_csv(path_or_buf="/Users/anthonypeters/Desktop/Coding-Jobs-and-Projects/For-Projects/Projects-Python/MLwMarketAPIs/Pull API/TDA_YFIN_CSV/TDA_CSV/price_data_{ticker}.csv".format(ticker = i))
####

tickers = ["TSLA"]
create_csv(tickers)
pull_close(tickers)
#print(retrieveTickerPriceHistory(ticker))
pull_close(tickers)