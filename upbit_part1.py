# -*- coding: utf-8 -*-
"""Upbit_part1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16LVbD54oRZWlta3VdoGYz9-RiIJxYAQf

**Interview Test**
"""

import pandas as pd
import requests

url = "https://th-api.upbit.com/v1/candles/days?market=THB-BTC&count=200"
r = requests.get(url)
candle_data = r.json()
r.status_code

df_candle = pd.DataFrame(candle_data)

df_candle

df_candle.dtypes

df = df_candle[["candle_date_time_utc","opening_price","high_price","low_price","prev_closing_price"]]
df

df.dtypes

# Change column name
df.columns = ["timestamp","open","high","low","close"]
df

#Change timestamp column to timestamp format
df["timestamp"]=pd.to_datetime(df["timestamp"],format='%Y-%m-%d %H:%M:%S', utc=True)
df

# Average closing price
df.describe()

# max closing price and date
max_close=df[df["close"]==df["close"].max()]
max_close[["timestamp","close"]]

# min closing price and date
min_close=df[df["close"]==df["close"].min()]
min_close[["timestamp","close"]]

# Average closing price
df["close"].mean(axis=0)

# ADD column price_change
df["price_change"]=df["close"]-df["open"]
df

#apply absolute function to column price_change
df["price_change"]=df.apply(lambda x: abs(x["price_change"]), axis=1)
df

# Filter where price_change > 1000, Display first 5 rows
df[df["price_change"]>1000].head()

# the correlation between the "price_change" column and the "high" column
df[["price_change","high"]].corr()

# Export upbit_data.csv
df.to_csv("upbit_data.csv", index = False)