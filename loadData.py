import quandl
import os
import pandas as pd
import numpy as np
import time
import pickle
import bs4 as bs
import requests


#To get API key create an account on Quandl website.Obtaining API Key lets you make more than 50 API calls in a day
quandl.ApiConfig.api_key='xxxxxx'


#fetch stock data between start and end dates
startdate="2005-10-06"
enddate="2018-10-06"



#function that scraps WIKI NIFTY page to fetch list of NIFTY50 stock tickers
def nifty50_list():
    resp = requests.get('https://en.wikipedia.org/wiki/NIFTY_50')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'},'tbody')
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[1].text

        tickers.append(ticker)

    with open("nifty50_list.pickle","wb") as f:
        pickle.dump(tickers,f)
    tickers.append('BAJAJ_AUTO')#Adding it manually since ticker name obtained from Wikipedia contains a hypen whereas quandl code expects an underscore
    tickers.append('MM')#Adding it manually since quandl code is different than the ticker symbol obtained from Wiki which is M&M
    tickers.append('NIFTY_50')#Fetching data for NIFTY50 index whose price we want to predict

    return tickers

#function to scrap NIFTY50 list from WIKI only if not already obtained
def get_nifty50_list(scrap=False):
    if scrap:
        tickers=nifty50_list()
    else:
        with open("nifty50_list.pickle","rb") as f:
            tickers=pickle.load(f)
    return tickers

#function to fetch stock prices from Quandl and then storing them to avoid making duplicate calls to Quandl API
def getStockdataFromQuandl(ticker):
    quandl_code="NSE/"+ticker


    try:

        if not os.path.exists(f'stock_data/{ticker}.csv'):
          data=quandl.get(quandl_code,start_date=startdate,end_date=enddate)
          data.to_csv(f'stock_data/{ticker}.csv')
        else:
            print(f"stock data for {ticker} already exists")
    except quandl.errors.quandl_error.NotFoundError as e:
        print(ticker)
        print(str(e))




def load():

    tickers=get_nifty50_list(True)

    df=pd.DataFrame()
    for ticker in tickers:

        getStockdataFromQuandl(ticker)
        try:



            data=pd.read_csv(f'stock_data/{ticker}.csv')
            if(ticker == "NIFTY_50"):
                data.rename(columns={'Close':f"{ticker}_Close",'Shares Traded':f"{ticker}_Volume"},inplace=True)
            else:
                data.rename(columns={'Close':f"{ticker}_Close",'Total Trade Quantity':f"{ticker}_Volume"},inplace=True)


            df=pd.concat([df,data[f'{ticker}_Volume'],data[f'{ticker}_Close']],axis=1)

        except Exception as e:
            print(f"couldn't find {ticker}")
            print(str(e))

    # df.to_csv('nifty50_closingprices.csv')
    df.dropna(inplace=True)
    return df



