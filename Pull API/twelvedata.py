#Nicholas Barone and Brianna Chou
#pip install twelvedata[pandas,matplotlib,plotly]
#pip install websocket_client
#pip install mplfinance

import twelvedata
from twelvedata import TDClient
td = TDClient(apikey="42659dffdec7409e9b158e709351ad53") #Insert your API key!

#Function 1 - Nick
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


#Function 2:matplotlib. We use .as_pyplot_figure() - Brianna
ts = td.time_series(
    symbol="MSFT",
    outputsize=75,
    interval="1day",
)
# 1. Returns OHLCV chart
ts.as_pyplot_figure()

# 2. Returns OHLCV + BBANDS(close, 20, 2, SMA) + %B(close, 20, 2 SMA) + STOCH(14, 3, 3, SMA, SMA)
ts.with_bbands().with_percent_b().with_stoch(slow_k_period=3).as_pyplot_figure()



#Function 3: batch requests. Only supported with json and pandas - Brianna
ts = td.time_series(
    symbol="V, RY, AUD/CAD, BTC/USD:Huobi"
)
#This is with .as_json()
ts = td.time_series(symbol='AAPL,MSFT', interval="1min", outputsize=3)
df = ts.with_macd().with_macd(fast_period=10).with_stoch().as_json()

{
    "AAPL": ({'datetime': '2020-04-23 15:59:00', 'open': '275.23001', 'high': '275.25000', 'low': '274.92999', 'close': '275.01001', 'volume': '393317', 'macd_1': '-0.33538', 'macd_signal_1': '-0.24294', 'macd_hist_1': '-0.09244', 'macd_2': '-0.40894', 'macd_signal_2': '-0.29719', 'macd_hist_2': '-0.11175', 'slow_k': '4.52069', 'slow_d': '7.92871'}, {'datetime': '2020-04-23 15:58:00', 'open': '275.07001', 'high': '275.26999', 'low': '275.00000', 'close': '275.25000', 'volume': '177685', 'macd_1': '-0.31486', 'macd_signal_1': '-0.21983', 'macd_hist_1': '-0.09503', 'macd_2': '-0.38598', 'macd_signal_2': '-0.26925', 'macd_hist_2': '-0.11672', 'slow_k': '14.70578', 'slow_d': '6.82079'}, {'datetime': '2020-04-23 15:57:00', 'open': '275.07001', 'high': '275.16000', 'low': '275.00000', 'close': '275.07751', 'volume': '151169', 'macd_1': '-0.30852', 'macd_signal_1': '-0.19607', 'macd_hist_1': '-0.11245', 'macd_2': '-0.38293', 'macd_signal_2': '-0.24007', 'macd_hist_2': '-0.14286', 'slow_k': '4.55965', 'slow_d': '2.75237'}),
    "MSFT": ({'datetime': '2020-04-23 15:59:00', 'open': '171.59000', 'high': '171.64000', 'low': '171.22000', 'close': '171.42000', 'volume': '477631', 'macd_1': '-0.12756', 'macd_signal_1': '-0.10878', 'macd_hist_1': '-0.01878', 'macd_2': '-0.15109', 'macd_signal_2': '-0.12915', 'macd_hist_2': '-0.02193', 'slow_k': '20.95244', 'slow_d': '26.34919'}, {'datetime': '2020-04-23 15:58:00', 'open': '171.41000', 'high': '171.61000', 'low': '171.33501', 'close': '171.61000', 'volume': '209594', 'macd_1': '-0.12440', 'macd_signal_1': '-0.10408', 'macd_hist_1': '-0.02032', 'macd_2': '-0.14786', 'macd_signal_2': '-0.12367', 'macd_hist_2': '-0.02419', 'slow_k': '39.04785', 'slow_d': '23.80945'}, {'datetime': '2020-04-23 15:57:00', 'open': '171.34500', 'high': '171.48000', 'low': '171.25999', 'close': '171.39999', 'volume': '142450', 'macd_1': '-0.13791', 'macd_signal_1': '-0.09900', 'macd_hist_1': '-0.03891', 'macd_2': '-0.16800', 'macd_signal_2': '-0.11762', 'macd_hist_2': '-0.05037', 'slow_k': '19.04727', 'slow_d': '14.92063'})
}
