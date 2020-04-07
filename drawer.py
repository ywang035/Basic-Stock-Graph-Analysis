import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import pandas as pd


register_matplotlib_converters()


                    ###################### making graph ######################


    ### basic price & volume ###
def plot_basic(dataset, date1, date2):
    plt.rcParams['axes.grid'] = True
    grid = plt.GridSpec(15, 4)
    a = plt.figure('Price and Volume', figsize=(20,8))
    plt.subplot(grid[0:10, 0:])
    plt.plot(dataset['Close'][date1:date2], label='close price', color='k')
    plt.legend()

    plt.subplot(grid[10:15, 0:])
    plt.plot(dataset['Volume'][date1:date2], label='volume', color='r')
    plt.legend()
    ### basic price & volume ###



    ### SMA 10/50/200 ###
def plot_sma(dataset, date1, date2):
    a = plt.figure('SMA 10/50/200', figsize=(20, 8))
    dataset['Close'][date1:date2].plot(label='Close', color='k', linestyle='solid')
    dataset['SMA10'][date1:date2].plot(label='SMA_10')
    dataset['SMA50'][date1:date2].plot(label='SMA_50')
    dataset['SMA200'][date1:date2].plot(label='SMA_200')
    plt.legend()
    return a
    ### SMA 10/50/200 ###



    ### RSI ###
def plot_RSI(dataset, date1, date2):
    plt.rcParams['axes.grid'] = True
    a = plt.figure('RSI', figsize=(20, 8))

    plt.subplot(2, 1, 1)
    plt.subplots_adjust(hspace=0.3)
    plt.title('Original RSI')
    plt.plot(dataset['RSI'].loc[date1:date2])
    plt.axhline(y=50, color='r')

    plt.subplot(2,1,2)
    plt.subplots_adjust(hspace=0.3)
    plt.title('Modified RSI')
    plt.bar(dataset['Date'].loc[date1:date2], width=0.5, height=dataset['RSI_Modify'].loc[date1:date2], color=(dataset['RSI_Modify'].loc[date1:date2] > 0).map({True: 'g',
                                                        False: 'r'}))
    plt.axhline(y=-20, color='r')
    plt.axhline(y=20, color='r')

    return a
    ### RSI ###


    ### EMA 12/26 ###
def plot_EMA(dataset, date1, date2):
    a = plt.figure('EMA + MACD', figsize=(20, 8))
    plt.plot(dataset['Close'].loc[date1:date2], color='k', linestyle='solid', label='Close')
    plt.plot(dataset['EMA12'].loc[date1:date2], label='EMA_12')
    plt.plot(dataset['EMA26'].loc[date1:date2], label='EMA_26')
    plt.legend()
    return a
    ### EMA 12/26 ###



    ### EMA + MACD ###
def plot_MACD(dataset, date1, date2):
    plt.rcParams['axes.grid'] = True
    a = plt.figure('EMA+MACD', figsize=(20, 8))

    plt.subplot(3, 1, 1)
    plt.subplots_adjust(hspace=0.25)
    plt.plot(dataset['Close'][date1:date2], color='k', linestyle='solid', label='Close')
    plt.plot(dataset['EMA12'][date1:date2], label='EMA_12')
    plt.plot(dataset['EMA26'][date1:date2], label='EMA_26')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.subplots_adjust(hspace=0.25)
    plt.plot(dataset['MACD'][date1:date2], label='MACD')
    plt.plot(dataset['MACD_Signal'][date1:date2], label='Signal')
    # plt.plot(dataset['MACD_Hist'][days:], label='Momentum')
    plt.bar(dataset['Date'].loc[date1:date2], width=0.5, height=dataset['MACD_Hist'][date1:date2] * 2,
            color=(dataset['MACD_Hist'][date1:date2] > 0).map({True: 'g',
                                                         False: 'r'}))
    plt.axhline(y=0, color='red')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.subplots_adjust(hspace=0.3)
    plt.title('Modified RSI')
    plt.bar(dataset['Date'].loc[date1:date2], width=0.5, height=dataset['RSI_Modify'][date1:date2],
            color=(dataset['RSI_Modify'][date1:date2] > 0).map({True: 'g',
                                                          False: 'r'}))
    plt.axhline(y=-20, color='r')
    plt.axhline(y=20, color='r')
    return a
    ### EMA + MACD ###



    ### JB Bands ###
def plot_jbbands(dataset, date1, date2):
    plt.rcParams['axes.grid'] = True
    a = plt.figure('Bollinger Bands',figsize=(20, 8))
    plt.plot(dataset['Close'][date1:date2], color='k', linestyle='solid')
    plt.plot(dataset['JBBAND_UP'][date1:date2], label='upper')
    plt.plot(dataset['JBBAND_MID'][date1:date2], label='mid')
    plt.plot(dataset['JBBAND_LOW'][date1:date2], label='lower')
    plt.legend()
    return a
    ### JB Bands ###



    ### OBV ###
def plot_obv(dataset, date1, date2):
    plt.rcParams['axes.grid'] = True
    a = plt.figure('OBV', figsize=(20, 8))

    plt.subplot(3, 1, 1)
    plt.plot(dataset['Close'][date1:date2], color='k', linestyle='solid', label='close')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(dataset['Volume'][date1:date2], label='volume', color='r')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(dataset['OBV'][date1:date2], label='OBV', color='b')
    plt.legend()
    return a
    ### OBV ###



    ### Stochastic Slow ###
def plot_sto_slow(dataset, date1, date2):
    plt.rcParams['axes.grid'] = True
    a = plt.figure('Stochastics Slow', figsize=(20, 8))

    plt.subplot(2, 1, 1)
    plt.plot(dataset['Close'][date1:date2], color='k', linestyle='solid', label='close')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(dataset['STO_SLOW_K'][date1:date2], label='k', color='r')
    plt.plot(dataset['STO_SLOW_D'][date1:date2], label='d', color='b')
    plt.legend()
    return a
    ### Stochastic Slow ###


                    ###################### making graph ######################