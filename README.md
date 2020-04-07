# Welcome

This is a simple Python project I made during my learning about Python data manipulation and plotting.<br/>
Lots of stuff learned in Pandas, NumPy and Matplotlib.<br/>
Trying to come up with some trading strategies that will beat buy&hold in mid/long term.
More to come in the future.

**Notice: these trading strategies are very basic and they are not designed to be used in real life. This play area is used at your own risk.** 


## How to Run

- ```python main.py -t ^GSPC -d BASIC``` to plot basic graph of close price and volume
- ```python main.py -t ^GSPC -it 2010-01-01 -ts BUY_HOLD,MACD_CROSS``` to calculate profit of each strategy


## Available Commands

- ```-h, --help```<br/>
  look for help
- ```-t, --ticker``` **(required)**<br/>
  for choosing ticker, such as AAPL for Apple.inc or ^GSPC for S&P500 index
- ```-it, --interval```<br/>
  for choosing time interval, default is 'DAILY', or choose 'WEEKLY'
- ```-sd, --start-date```<br/>
  for choosing start date, format in yyyy-mm-dd, default is 1-year from 'TODAY'
- ```-ed, --end-date```<br/>
  for chossing end date, format in yyyy-mm-dd, default is 'TODAY'
- ```-d, --draw```<br/>
  for plotting, input example: <SMA_CROSS,MACD_CROSS>, available option: <BASIC, SMA, EMA, MACD, RSI, JBBAND, STO_SLOW>
- ```-ts, --trade-strategy```<br/>
  for choosing basic trading strategy, input example: <SMA_CROSS,MACD_CROSS>, available option: <BUY_HOLD, SMA_CROSS, MACD_CROSS>


## Example of Plotting

<img src="https://github.com/ywang035/Basic-Stock-Graph-Analysis/blob/master/SMA.png" width="400"><img src="https://github.com/ywang035/Basic-Stock-Graph-Analysis/blob/master/EMA+MACD.png" width="400">
<img src="https://github.com/ywang035/Basic-Stock-Graph-Analysis/blob/master/OBV.png" width="400"><img src="https://github.com/ywang035/Basic-Stock-Graph-Analysis/blob/master/MACD_CROSS_Strategy.png" width="400">


### Installed of Library
- pandas
- matplotlib
- talib = '0.4.17'
