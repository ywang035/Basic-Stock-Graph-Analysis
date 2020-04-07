import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import math

                            ###################### strategy and profit ######################


    ### buy and hold ###
def buy_hold(dataset):
    dataset['Shares'] = [1 for ei in dataset.index]
    dataset['Close1'] = dataset['Close'].shift(-1)
    dataset['Profit'] = [dataset.loc[ei, 'Close1'] - dataset.loc[ei, 'Close'] if dataset.loc[ei, 'Shares'] == 1 else 0
                         for ei in dataset.index]
    dataset['Wealth'] = dataset['Profit'].cumsum()

    a = plt.figure('Buy and Hold Strategy', figsize=(20, 8))
    plt.subplot(3, 1, 1)
    plt.bar(dataset.index, width=0.5, height=dataset['Shares'], label='shares')

    plt.subplot(3, 1, 2)
    dataset['Profit'].plot(label='profit')
    plt.axhline(y=0, color='red')

    plt.subplot(3, 1, 3)
    dataset['Wealth'].plot(label='wealth')

    return dataset['Wealth'].tail(), a
    ### buy and hold ###



    ### SMA strategy ###
def sma_strategy(dataset):
    dataset['Shares'] = [1 if dataset.loc[ei, 'SMA10'] > dataset.loc[ei, 'SMA50'] else 0 for ei in dataset.index]
    dataset['Close1'] = dataset['Close'].shift(-1)
    dataset['Profit'] = [dataset.loc[ei, 'Close1'] - dataset.loc[ei, 'Close'] if dataset.loc[ei, 'Shares'] == 1 else 0
                         for ei in dataset.index]
    dataset['Wealth'] = dataset['Profit'].cumsum()

    a = plt.figure('SMA Strategy Profit / Wealth', figsize=(20, 8))
    plt.subplot(3,1,1)
    # plt.plot(dataset['Shares'], label='shares')
    plt.bar(dataset.index, width=0.5, height=dataset['Shares'], label='shares')

    plt.subplot(3,1,2)
    dataset['Profit'].plot(label='profit')
    plt.axhline(y=0, color='red')

    plt.subplot(3,1,3)
    dataset['Wealth'].plot(label='wealth')
    return dataset['Wealth'].tail(), a
    ### SMA strategy ###


    ### MACD + RSI strategy ###
def macd_strategy(dataset):
    MACD = dataset['MACD'].tolist()
    MACD_signal = dataset['MACD_Signal'].tolist()
    MACD_hist = dataset['MACD_Hist'].tolist()
    RSI_list = dataset['RSI'].tolist()

    share_list = []
    for x, y, z in zip(MACD, MACD_signal, RSI_list):
        if (math.isnan(x)):
            share_list.append(float('nan'))
        else:

            if x > y:
                share_list.append(1)
            else:
                share_list.append(0)

    dataset['Shares'] = share_list
    dataset['Close1'] = dataset['Close'].shift(-1)
    dataset['Profit'] = [dataset.loc[ei, 'Close1'] - dataset.loc[ei, 'Close'] if dataset.loc[ei, 'Shares'] == 1 else 0
                         for ei in dataset.index]
    dataset['Wealth'] = dataset['Profit'].cumsum()


    plt.rcParams['axes.grid'] = True
    a = plt.figure('MACD CROSS Strategy', figsize=(20, 8))

    # plotting shares
    plt.subplot(3,1,1)
    plt.bar(dataset.index, width=0.5, height=dataset['Shares'], label='shares')
    plt.legend()

    # plotting profit
    plt.subplot(3,1,2)
    dataset['Profit'].plot(label='profit')
    plt.axhline(y=0, color='red')
    plt.legend()

    # plotting wealth
    plt.subplot(3,1,3)
    dataset['Wealth'].plot(label='wealth')
    plt.legend()

    return dataset['Wealth'].tail(), a
    ### MACD + RSI strategy ###


                            ###################### strategy and profit ######################