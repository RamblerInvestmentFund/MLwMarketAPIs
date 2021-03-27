import requests
import json
import csv
import pandas as pd

#### Retrieve Ticker Option Chain
def retrieveTickerOptionChain(ticker):
    endpoint = endpoint = 'https://api.tdameritrade.com/v1/marketdata/chains?&symbol={stock_ticker}'
    full_url = endpoint.format(stock_ticker=ticker)
    page = requests.get(url=full_url,
                        params={'apikey' : 'NXHAYFIAP0TXGN9NFR27DDAF7QSNQPHA'})
    content = json.loads(page.content)
    return content
####

#### Create Empty CSV for data Transfer
def create_csv(tickers):
    df = pd.DataFrame(data=None)
    for i in tickers:
        written = df.to_csv(path_or_buf="/Users/anthonypeters/Desktop/Coding-Jobs-and-Projects/For-Projects/Projects-Python/MLwMarketAPIs/Pull API/TDA_YFIN_CSV/TDA_CSV/option_data_{ticker}.csv".format(ticker = i))
    return(written)
####

#### Pull data and write to CSV
def pull_close(tickers):
    for i in tickers:
        data = retrieveTickerOptionChain(i)
        with open('/Users/anthonypeters/Desktop/Coding-Jobs-and-Projects/For-Projects/Projects-Python/MLwMarketAPIs/Pull API/TDA_YFIN_CSV/TDA_CSV/option_data_{ticker}.csv'.format(ticker = i), 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in data.items():
                writer.writerow([key, value])
####

tickers = ["AAPL", "AMZN", "MSFT", "JNJ"]
create_csv(tickers)
pull_close(tickers)