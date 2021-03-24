""" Christian Panici and Nancy Paul """

import matplotlib.pyplot as plt
import requests
import pandas as pd

# Insert your API key here
params = {
  'access_key': 'API_KEY'
}


def plot_aapl_eod_highs():
	""" Plot the EOD highs for AAPL based on the 
		last 100 days of data returned by the API"""
	eod_highs = []
	dates = []
	api_result = requests.get('http://api.marketstack.com/v1/tickers/aapl/eod', params)

	stock_data = api_result.json()['data']['eod'][::-1]
	for day in stock_data:
		eod_highs.append(day["high"])
		dates.append(day["date"])

	plt.plot(dates, eod_highs)
	plt.title('AAPL EOD Highs over last 100 available days')
	plt.xlabel('Date')	
	plt.ylabel('EOD Price (S)')
	plt.xticks(rotation=90)
	plt.show()

def plot_aapl_eod_lows():
	""" Plot the EOD lows for AAPL based on the 
		last 100 days of data returned by the API"""
	eod_lows = []
	dates = []
	api_result = requests.get('http://api.marketstack.com/v1/tickers/aapl/eod', params)

	# Data returns w/ most recent first, want reverse
	stock_data = api_result.json()['data']['eod'][::-1]
	for day in stock_data:
		eod_lows.append(day["low"])
		dates.append(day["date"])

	plt.plot(dates, eod_lows)
	plt.title('AAPL EOD Lows over last 100 available days')
	plt.xlabel('Date')    
	plt.ylabel('EOD Price (S)')
	plt.xticks(rotation=90)
	plt.show()
	
def plot_aapl_daily_volume():
	""" Plot the daily volume for AAPL based on the 
		last 100 days of data returned by the API"""
	volumes = []
	dates = []
	api_result = requests.get('http://api.marketstack.com/v1/tickers/aapl/eod', params)

	# Data returns w/ most recent first, want reverse
	stock_data = api_result.json()['data']['eod'][::-1]
	for day in stock_data:
		volumes.append(day["volume"])
		dates.append(day["date"])

	plt.plot(dates, volumes)
	plt.title('AAPL Volume over last 100 available days')
	plt.xlabel('Date')	
	plt.ylabel('Volume (in hundred millions)')
	plt.xticks(rotation=90)
	plt.show()

def plot_msft_daily_opens():
	""" Plot the daily opening prices for MSFT based on the 
		last 100 days of data returned by the API"""
	opens = []
	dates = []
	api_result = requests.get('http://api.marketstack.com/v1/tickers/msft/eod', params)

	# Data returns w/ most recent first, want reverse
	stock_data = api_result.json()['data']['eod'][::-1]
	for day in stock_data:
		opens.append(day["open"])
		dates.append(day["date"])

	plt.plot(dates, opens)
	plt.title('MSFT Daily Opening Prices over last 100 available days')
	plt.xlabel('Date')    
	plt.ylabel('Opening Price')
	plt.xticks(rotation=90)
	plt.show()
	
def plot_msft_eod_closes():
	""" Plot the EOD closing prices for MSFT based on the 
		last 100 days of data returned by the API"""
	closes = []
	dates = []
	api_result = requests.get('http://api.marketstack.com/v1/tickers/msft/eod', params)

	# Data returns w/ most recent first, want reverse
	stock_data = api_result.json()['data']['eod'][::-1]
	for day in stock_data:
		closes.append(day["close"])
		dates.append(day["date"])

	plt.plot(dates, closes)
	plt.title('MSFT EOD Closing Prices over last 100 available days')
	plt.xlabel('Date')    
	plt.ylabel('Closing Price')
	plt.xticks(rotation=90)
	plt.show()

def create_csv(tickers: list, features: list, days: int) -> None:
	""""Use marketstack data to create csv for arbitrary number of tickers, features, days"""
	# Initialize empty dataframe
	data = pd.DataFrame()

	for ticker in tickers:
		try:
			row = {}
			# Get API data for ticker
			api_result = requests.get(f'http://api.marketstack.com/v1/tickers/{ticker}/eod', params)

			# Isolate the day range we want (Last {days} days...)
			stock_data = api_result.json()['data']['eod'][:days]

			# Record the data for each day for each feature specified (see Marketstack docs for options)
			for index, day in enumerate(stock_data, 1):
				for feature in features:
					row[f'{index}day_lag_{feature}'] = day[feature]
			
			# Add on to our main dataframe
			pd_row = pd.Series(row, name=ticker)
			data = data.append(pd_row)
			print(f'SUCCESS: {ticker}')
		except:
			print(f'ERROR: ticker {ticker}')
	
	# Save dataframe to csv
	try:
		print('Saving to csv...')
		data.to_csv('stock_data.csv', index=True, index_label='ticker')
		print('Saved!')
	except Exception as e:
		print(f'Error saving: {e}')



if __name__ == '__main__':
	# plot_aapl_eod_highs()
	# plot_aapl_eod_lows()
	# plot_aapl_daily_volume()
	# plot_msft_daily_opens()
	# plot_msft_eod_closes()
	create_csv(tickers=['AACG', 'AACQ', 'AACQU', 'AACQW', 'AAL', 'AAME', 'AAOI', 'AAON', 'AAPL', 'AAWW',
 				'ABCB', 'ABCL', 'ABCM', 'ABEO', 'ABGI', 'ABIO', 'ABMD', 'ABNB', 'ABST', 'ABTX',
 				'ABUS', 'ACAC', 'ACACU', 'ACACW', 'ACAD', 'ACAHU', 'ACBI', 'ACCD', 'ACER', 'ACET',
 				'ACEV', 'ACEVU', 'ACEVW', 'ACGL', 'ACGLO', 'ACGLP', 'ACHC', 'ACHV', 'ACIU', 'ACIW',
 				'ACKIT', 'ACKIU', 'ACKIW', 'ACLS', 'ACMR', 'ACNB', 'ACOR', 'ACQRU', 'ACRS'], 
				features= ['open', 'close', 'high', 'low', 'volume'], 
				days=5)
