import time
import pickle
import bs4 as bs
import requests

def nifty50_list():#function that scraps WIKI NIFTY%) page to fetch list of NIFTY50 stock tickers
    resp = requests.get('https://en.wikipedia.org/wiki/NIFTY_50')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'},'tbody')
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[1].text
        print(ticker)
        tickers.append(ticker)

    with open("nifty50_list.pickle","wb") as f:
        pickle.dump(tickers,f)

    return tickers

def get_nifty50_list(scrap=False):#function to scrap NIFTY50 list from WIKI only if not already obtained
    if scrap:
        tickers=nifty50_list()
    else:
        with open("nifty50_list.pickle","rb") as f:
            tickers=pickle.load(f)
    return tickers

