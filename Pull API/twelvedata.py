#Nicholas Barone and Brianna Chou
#pip install twelvedata

import twelvedata
from twelvedata import TDClient

td = TDClient(apikey="API_KEY_HERE") #Insert your API key!
ts = td.time_series(
    symbol="SPY",
    exchange="NYSE",
    interval="5min",
    outputsize=22,
    timezone="America/New_York",
)
# Returns: OHLC, MACD() as json
ts.with_macd().as_json()

# Options .as_json() .as_csv() .as_pandas()
