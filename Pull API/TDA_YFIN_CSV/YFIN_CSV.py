import yfinance as yf
import csv

def pull_close(tickers):
    #### Pulls and cleans data into priceDict from yfinance
    for i in tickers:
        data = yf.download(tickers=i, group_by="Close", interval="1d")
        priceList = data['Close']
        written = priceList.to_csv(path_or_buf="stock_data_{ticker}.csv".format(ticker = i))
    return(written)

tickers = ["AAPL", "AMZN", "MSFT", "JNJ"]
pull_close(tickers)
# with open('stock_data.csv', mode='w') as stock_data:
#     stock_data = csv.writer(stock_data)
#     stock_data.writerows(pull_close(tickers))