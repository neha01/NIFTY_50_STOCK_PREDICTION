## Overview
Predicting NIFTY50 index movement for 7 days period.
LSTM layers are used in keras to predict NIFTY50 index movement for 7 days period.

Project is divided into three parts:
1.loadData.py
Scraped Wiki's NIFTY50 page to get ticker symbols
Used Quandl API to fetch stock data for past 5 years

2.Preprocess.py
Label training data as 0(sell) and 1(buy)
Scale data using sklaern preprocessing libarary

3.Build_model.py
Build model in keras with LSTM layers.

Program runs at 56% Validation accuracy and 39% Validation loss

### Dependencies:
pandas
tensorflow
keras
sklearn
numpy
beautifulsoup4
requests
