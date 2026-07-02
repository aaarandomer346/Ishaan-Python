import yfinance as yf
import numpy as np

df = yf.Ticker("RECLTD.NS").history(period="1y")

trading_days = np.array(df.index.strftime('%Y-%m-%d'))
prices       = np.round(df['Close'].values, 2)

print(len(trading_days))

print(f"{len(trading_days)} days: {trading_days[0]} → {trading_days[-1]}")