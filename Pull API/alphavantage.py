#Aditi and Dana

#set up environment

import pandas
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange
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


