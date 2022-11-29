import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from mplfinance.original_flavor import candlestick2_ochl

def ohlc2cs(fname, seq_len, dimension):
    df = pd.read_csv(fname, names=['Date', 'Open', 'High', 'Low', 'Close'])
    df.fillna(0)
    plt.style.use('dark_background')
    df.reset_index(inplace=True)

    figs = np.zeros((len(df), dimension, dimension, 3))
    labels = []

    for i in range(0, len(df)-19):
        # ohlc+volume
        c = df.iloc[i:i + int(seq_len), :]
        c_ = df.iloc[i:i + int(seq_len)+1, :]
        if not os.path.isfile("chart_data/chart_{0}.png".format(i)):
            if len(c) == int(seq_len):
                my_dpi = 96
                fig = plt.figure(figsize=(dimension/my_dpi, dimension/my_dpi), dpi=my_dpi)
                ax1 = fig.add_subplot(1,1,1) #그리려는 그래프만큼 subplot을 만드는 것(1*1 graph 중 첫번째 라는 뜻)
                candlestick2_ochl(ax1, c['Open'], c['Close'], c['High'], c['Low'], width=1, colorup='#77d879', colordown='#db3f3f')
                ax1.grid(False)
                ax1.set_xticklabels([])
                ax1.set_yticklabels([]) #Label 필요 없기에
                ax1.xaxis.set_visible(False)
                ax1.yaxis.set_visible(False)
                ax1.axis('off')
            plt.savefig("chart_data/chart_{0}.png".format(i))
            plt.close(fig)


        starting = c_["Close"].iloc[-2]
        ending = c_["Close"].iloc[-1]

        if ending > starting:
            label = 1
        else: label = 0
        labels.append(label)

    print("Converting olhc to candlestik finished.")
    return labels



seq_len = 20
dimension = 48
labels = ohlc2cs("BitStamp_btc_usd_hourly_data.csv", seq_len, dimension)

with open('chart_label.txt', 'w') as f:
    for label in labels:
        f.write("{0}\n".format(label))