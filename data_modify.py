import numpy as np
import pandas as pd
import talib


def calculation(dataset):

    dataset['Date'] = dataset.index
    dataset['PriceDiff'] = dataset['Close'].shift(-1) - dataset['Close']
    dataset['Return'] = dataset['PriceDiff'] / dataset['Close']
    dataset['Direction'] = [1 if dataset['PriceDiff'].loc[ei] > 0 else 0 for ei in dataset.index]
    dataset['SMA10'] = dataset['Close'].rolling(10).mean()
    dataset['SMA50'] = dataset['Close'].rolling(50).mean()
    dataset['SMA200'] = dataset['Close'].rolling(200).mean()
    dataset['EMA12'] = talib.EMA(dataset['Close'], timeperiod=12)
    dataset['EMA26'] = talib.EMA(dataset['Close'], timeperiod=26)
    dataset['RSI'] = talib.RSI(np.asarray(dataset['Close']))
    dataset['RSI_Modify'] = dataset['RSI'] - 50
    dataset["JBBAND_UP"], dataset["JBBAND_MID"], dataset["JBBAND_LOW"] = talib.BBANDS(np.asarray(dataset['Close']),
                                                                                      timeperiod=20, nbdevup=2,
                                                                                      nbdevdn=2, matype=0)
    dataset['MACD'], dataset['MACD_Signal'], dataset['MACD_Hist'] = talib.MACD(np.asarray(dataset['Close']),
                                                                               fastperiod=12, slowperiod=26,
                                                                               signalperiod=9)
    dataset['OBV'] = talib.OBV(np.asarray(dataset['Close']), np.asarray(dataset['Volume'], dtype='float'))
    dataset['STO_SLOW_K'], dataset['STO_SLOW_D'] = talib.STOCH(np.asarray(dataset['High']), np.asarray(dataset['Low']), np.asarray(dataset['Close']), fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3,
                         slowd_matype=0)
    return dataset
