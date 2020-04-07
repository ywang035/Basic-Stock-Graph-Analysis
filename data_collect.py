import yahoofinancials as yf
import pandas as pd
from pandas_datareader import data


def getPriceData1(ticker, start_date, end_date):
    dataset = data.DataReader(ticker, 'yahoo', start_date, end_date)
    return dataset

def getPriceData2(ticker, start_date, end_date, time_interval='daily'):
    stock = yf.YahooFinancials(ticker)
    stock_history_price_dict = stock.get_historical_price_data(start_date=start_date, end_date=end_date,
                                                               time_interval='daily')
    price_list = stock_history_price_dict.get(ticker).get('prices')
    price_df = pd.DataFrame(price_list)
    return price_df