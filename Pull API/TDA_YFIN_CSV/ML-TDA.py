import pandas as pd
import numpy as np

df = pd.read_csv("/Users/anthonypeters/Desktop/Coding-Jobs-and-Projects/For-Projects/Projects-Python/MLwMarketAPIs/Pull API/TDA_YFIN_CSV/TDA_CSV/price_data_TSLA.csv", index_col=0)
df = df['close']
df = df.to_numpy()

print(df)