import argparse
import datetime as dt
import pandas as pd
import data_collect
import data_modify
import drawer
import profit_calculate
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Basic Stock Data & Graph for Fun')
parser.add_argument('-t','--ticker', help='enter ticker in CAP, AAPL for Apple Inc, ^GSPX for SP500, etc...', required=True)
parser.add_argument('-it','--interval', help='default=daily, Alternative: <WEEKLY>', required=False)
parser.add_argument('-sd','--start-date', help='date format: yyyy-mm-dd', required=False)
parser.add_argument('-ed', '--end-date', help='date format: yyyy-mm-dd', required=False)
parser.add_argument('-d', '--draw', help='input example: <MACD,RSI,SMA>, available graph: <BASIC, SMA, EMA, MACD, RSI, JBBAND, STO_SLOW>', required=False)
parser.add_argument('-ts', '--trade-strategy', help='input example: <SMA_CROSS,MACD_CROSS>, available strategies: <BUY_HOLD, SMA_CROSS, MACD_CROSS>', required=False)
args = parser.parse_args()



    ### args ###
ticker = args.ticker
interval = args.interval
start_date = args.start_date
end_date = args.end_date
draw = args.draw
draw_list = list(str(args.draw).split(","))
trade_strategy=args.trade_strategy
ts_list = list(str(args.trade_strategy).split(","))
    ### args ###




    ### print parameter ###
print('chosen ticker \t\t-----> \t', ticker)
if (start_date is None):
    start_date = dt.date.today() - dt.timedelta(days=365)
    print('setting start date \t-----> \t', start_date)
else:
    print('start date \t-----> \t', start_date)

if (end_date is None):
    end_date = dt.date.today()
    print('setting end date \t-----> \t', end_date)
else:
    print('end date -----> ', end_date)
    ### print parameter ###


    ### calculate weekly price ###
def week_open(array_like):
    return array_like[0]
def week_close(array_like):
    return array_like[-1]
    ### calculate weekly price ###


    ### getting price data ###
dataset_daily = data_collect.getPriceData1(ticker, start_date, end_date)
if (interval is None):
    modified_dataset = data_modify.calculation(dataset_daily)
else:
    dataset_weekly = dataset_daily.resample('W',
                                 how={'Open': week_open,
                                      'High': 'max',
                                      'Low': 'min',
                                      'Close': week_close,
                                      'Volume': 'sum'},
                                 loffset=pd.offsets.timedelta(days=-6))
    dataset_weekly = dataset_weekly[['Open', 'High', 'Low', 'Close', 'Volume']]
    modified_dataset = data_modify.calculation(dataset_weekly)
print(modified_dataset.tail(10))
    ### getting price data ###




    ### plotting graphs ###
if draw is not None:
    print('Plotting: ',draw_list)
    if draw_list.__contains__('BASIC'):
        drawer.plot_basic(modified_dataset, start_date, end_date)
    if draw_list.__contains__('SMA'):
        drawer.plot_sma(modified_dataset, start_date, end_date)
    if draw_list.__contains__('MACD'):
        drawer.plot_MACD(modified_dataset, start_date, end_date)
    if draw_list.__contains__('EMA'):
        drawer.plot_EMA(modified_dataset,start_date,end_date)
    if draw_list.__contains__('RSI'):
        drawer.plot_RSI(modified_dataset, start_date, end_date)
    if draw_list.__contains__('JBBAND'):
        drawer.plot_jbbands(modified_dataset, start_date, end_date)
    if draw_list.__contains__('OBV'):
        drawer.plot_obv(modified_dataset, start_date, end_date)
    if draw_list.__contains__('STO_SLOW'):
        drawer.plot_sto_slow(modified_dataset, start_date, end_date)
    ### plotting graphs ###




    ### calculate strategy profit ###
if trade_strategy is not None:
    print('Calculating: ', ts_list)
    if ts_list.__contains__('BUY_HOLD'):
        profit_1 = profit_calculate.buy_hold(modified_dataset)
        print('***** buy and hold cumulate profit *****')
        print(profit_1, '\n')
    if ts_list.__contains__('MACD_CROSS'):
        profit_3, fig_2 = profit_calculate.macd_strategy(modified_dataset)
        print('***** MACD strategy cumulate profit *****')
        print(profit_3, '\n')
    if ts_list.__contains__(('SMA_CROSS')):
        profit_2, fig_1 = profit_calculate.sma_strategy(modified_dataset)
        print('***** SMA strategy cumulate profit *****')
        print(profit_2, '\n')
    ### calculate strategy profit ###

plt.show()



