import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


def create_historical_df(yf_name):   #input as string
    stock = yf.Ticker(yf_name)
    df = stock.history('3mo')
    df_exp = df[['Close']]
    return df_exp

def average_sd(df):
    sd_arr = []
    print('shape :', df.shape[0])
    for i in range(df.shape[0]):
        if i+7 < df.shape[0]:
            day_df = df.iloc[i-7:i+7]
            sd = day_df['Close'].std()
        else :
            sd = np.nan
        sd_arr.append(sd)
    df['sd'] = sd_arr
    mean_sd = df['sd'].mean()
    return mean_sd

def risk_level(mean_sd_percent):
    if   0.0 < mean_sd_percent <= 1.0:
        risk = 1
    elif 1.0 < mean_sd_percent <= 2.0:
        risk = 2
    elif 2.0 < mean_sd_percent <= 3.0:
        risk = 3
    elif 3.0 < mean_sd_percent <= 4.0:
        risk = 4
    elif 4.0 < mean_sd_percent <= 5.0:
        risk = 5
    elif 6.0 < mean_sd_percent <= 7.0:
        risk = 6
    else:
        risk = 7
    return risk



# ------- main --------
def risk_from_his(stock_name):
    print(stock_name)
    df_history = create_historical_df(stock_name)
    mean_sd = average_sd(df_history)
    mean_stock_price = df_history["Close"].mean()
    mean_sd_percent = mean_sd/mean_stock_price * 100
    print('3mo mean stock price = ', mean_stock_price)
    print('sd of stock mean over 3 mo = ', mean_sd)
    print('percentage of sd of mean price to the stockprice = ', mean_sd_percent)
    risk = risk_level(mean_sd_percent)
    print('-----')
    print('risk level(1-7): ', risk)
    return risk

# risk_from_his("3K-BAT.BK")