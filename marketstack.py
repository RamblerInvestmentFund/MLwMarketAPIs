import matplotlib.pyplot as plt
import requests

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

	# Data returns w/ most recent first, want reverse
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

if __name__ == '__main__':
	plot_aapl_eod_highs()
	plot_aapl_daily_volume()