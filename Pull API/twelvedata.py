from twelvedata import TDClient

td = TDClient(apikey="YOUR_API_KEY")
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