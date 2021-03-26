#Aditi and Dana

#installation: pip install avapi
import avapi as aa 

#set up environment

import pandas
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.fundamentaldata import FundamentalData
from pprint import pprint

#set API Key and Symbol

mykey = 'YOUR_API_KEY'
mysymb = "TSLA"                                                                                   #other stock Symbols: '' '' '' etc


#Get intraday data and metadata
def getData(key,symb):
    time = TimeSeries(key= key, output_format= "pandas")                                          #create TimeSeries object and Make API Call
    data, meta = time.get_intraday(symbol=symb , interval='1min', outputsize= 'full')
    print(meta)
    print(data)


#Get time stock trade is at it's high and low for a day

def getHighs(key,symb):
    time = TimeSeries(key=key, output_format="pandas")                                            #create TimeSeries object and Make API Call
    data, meta = time.get_intraday(symbol=symb, interval='1min',outputsize='full')                #approx 10 days of high volume of the trade
    print(data['2. high'])


def getLows(key,symb):
    time = TimeSeries(key=key, output_format="pandas")                                            #create TimeSeries object and Make API Call
    data, meta = time.get_intraday(symbol=symb, interval='1min', outputsize='full')               #approx 10 days of low volume of the trade
    print(data['3. Lows'])


#plot the intra-minute value for stock
def plotValue(key,symb):
    time = TimeSeries(key=key, output_format="pandas")
    data, meta = time.get_intraday(symbol=symb, interval='1min', outputsize='full')
    data['4. close'].plot()
    plt.title('Intraday Times Series for the ' + symb + ' stock (1 min)')
    plt.show()

#Foreign Exchange Bitcoin to USD
def fxData(key):
    cc = ForeignExchange(key=key)
    data = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
    pprint(data)

####################################################
################ Christian & Nancy #################
####################################################

def get_rsi(key, symbol, interval, time_period, series_type, include_plot=False):
    """Get RSI data for a given ticker. If requested, plot returned data marked 
        with two standard deviations above/below avg
        Return: RSI dataframe, mean RSI over period, std deviation of RSI over period"""
    ti = TechIndicators(key=key, output_format='pandas')
    data, meta_data = ti.get_rsi(symbol=symbol, interval=interval, time_period=time_period, series_type=series_type)
    mean = data['RSI'].mean()
    std = data['RSI'].std()
    if include_plot:
        data.plot()
        plt.title(f'RSI indicator for {symbol} stock (Interval: {interval} @ {series_type})\nLine = 2 std dev')
        plt.axhline(y=mean + 2*std, color='r', linestyle='-')
        plt.axhline(y=mean - 2*std, color='r', linestyle='-')
        plt.show()
    return data, mean, std

def get_crypto_monthly(key, symbol, market, include_plot=False):
    """Get monthly price of a given cryptocurrency
        Return: Price dataframe, mean price over period, std deviation of price over period"""
    cc = CryptoCurrencies(key=key, output_format='pandas')
    data, meta_data = cc.get_digital_currency_monthly(symbol=symbol, market=market)
    print(data.columns)
    mean = data['1b. open (USD)'].mean()
    std = data['1b. open (USD)'].std()
    if include_plot:
        data.plot(y='1b. open (USD)')
        plt.title(f'Monthly open price for {symbol} (Market: {market})\nLine = 2 std dev')
        plt.axhline(y=mean + 2*std, color='r', linestyle='-')
        plt.axhline(y=mean - 2*std, color='r', linestyle='-')
        plt.show()
    return data, mean, std

def get_earnings(key, symbol, include_plot=False):
    fd = FundamentalData(key=key, output_format='pandas')
    data, meta_data = fd.get_income_statement_annual(symbol=symbol)
    if include_plot:
        plt.bar(data['fiscalDateEnding'], data['grossProfit'])
        plt.title(f'Yearly Gross Profit for {symbol}')
        plt.show()

def getOpens(key,symb):
    time = TimeSeries(key=key, output_format="pandas")                                            
    data, meta = time.get_intraday(symbol=symb, interval='1min',outputsize='full')                
    print(data['1. open'])
    
def getCloses(key,symb):
    time = TimeSeries(key=key, output_format="pandas")                                            
    data, meta = time.get_intraday(symbol=symb, interval='1min',outputsize='full')                
    print(data['4. close'])
 
#create csv for data pulled from alphavantage
def create_csv():
    
    #data functions specified in alphavantage.py
    data_calls = [
        {
        #pull for intraday data: open, high, low, close, volume
         'function':'TIME_SERIES_INTRADAY', 
         'symbol': 'TSLA',
         'interval': '1min',
         'output_size': 'compact',
         'datatype': 'csv',
         'apikey': mykey,
        }
    ]

    for i in range(len(data_calls)):
        save_to = 'alphavantage.csv'
        data_calls = aa.get_data(save_to=save_to, **data_calls[i])

create_csv()
    
if __name__ == '__main__':
    get_earnings(key=mykey, symbol='TSLA', include_plot=True)
    get_crypto_monthly(key=mykey, symbol='BTC', market='CNY', include_plot=True)
    get_rsi(key=mykey, symbol='TSLA', interval='60min', time_period=60, series_type='open', include_plot=True)
