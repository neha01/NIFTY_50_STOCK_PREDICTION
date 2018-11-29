## Overview
Predicting NIFTY50 index movement for 7 days period.
LSTM layers are used in keras to predict NIFTY50 index movement for 7 days period.

## Youtube Tutorial
https://www.youtube.com/watch?v=BYd9M_ragR0

Project is divided into three parts:</br>
* loadData.py</br>
Scraped Wiki's NIFTY50 page to get ticker symbols<br>
Used Quandl API to fetch stock data for past 5 years

* Preprocess.py</br>
Label training data as 0(sell) and 1(buy)<br>
Scale data using sklearn preprocessing libarary

* Build_model.py</br>
Build model in keras with LSTM layers.

Program runs at 61% Validation accuracy and 39% Validation loss

### Dependencies:
* pandas
* tensorflow
* keras
* sklearn
* numpy
* beautifulsoup4
* requests

### Usage:
Run Buildmodel.py script on commandline.

### Acknowledgements:
* sentdex tutorial -> https://www.youtube.com/watch?time_continue=535&v=yWkpRdpOiPY
* Siraj Raval tutorial -> https://www.youtube.com/watch?v=ftMq5ps503w&vl=en
