import yfinance as yf
import csv

def pull_close(tickers):
    #### Pulls and cleans data into priceDict from yfinance
    for i in tickers:
        data = yf.download(tickers=i, group_by="Close", period="3mo", interval="1d")
        price = data['Close']
        written = price.to_csv(path_or_buf="stock_data_{ticker}.csv".format(ticker = i))
    return(written)

tickers = ["TSLA"]
pull_close(tickers)