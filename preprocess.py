from sklearn import preprocessing
import pandas as pd
import numpy as np
import loadData


#how many days data will be used to create series to train RNN
SERIES_LENGTH=30
PREDICT_LENGTH=7

TICKER="NIFTY_50"

def normalize_data(df):
    pass#implement it if you want to use different techniques for normalizing and scaling

def scale_data(df):
    for column in df.columns:
        df[column] = preprocessing.scale(df[column].values)
    return df

def process_data(df):
    df["nifty_future_price"]=df[f"{TICKER}_Close"].shift(-PREDICT_LENGTH)

    #Dropping any Nan values
    df.dropna(inplace=True)

    #comparing future nifty price with today's price and labeling it as 1 if price increases and zero otherwise
    df["Label"]=np.where(df["nifty_future_price"]>=df["NIFTY_50_Close"],1,0)

    #dropping 'nifty_future_price'  columns as it is no longer required
    df.drop('nifty_future_price',1,inplace=True)
    df.to_csv('nifty50_future_label.csv')

    sequence=[]
    temp=df.loc[:, df.columns != 'Label']
    temp=scale_data(temp)
    # print(f"temp{temp[:30]}")
    for i in range (len(temp)-SERIES_LENGTH):
       sequence.append([np.array(temp[i:i+SERIES_LENGTH]),df.iloc[i+SERIES_LENGTH,-1]])

    np.random.shuffle(sequence)

    X=[]
    y=[]
    buy=[]
    sell=[]
    for seq ,label in sequence:
        if label == 0:
            sell.append([seq,label])
        else:
            buy.append([seq,label])
    # print(f"buy :{buy[:10]}")
    # print(f"sell :{sell[:10]}")
    buys=len(buy)
    sells=len(sell)
    # print(f"original buys:{buys} original sells:{sells}")
    if(buys<sells):
        buy=buy[:buys]
        sell=sell[:buys]
    else:
        buy=buy[:sells]
        sell=sell[:sells]

    # print(f"buys:{len(buy)} sells:{len(sell)}")
    sequence=buy+sell

    np.random.shuffle(sequence)


    for seq ,label in sequence:
        X.append(seq)
        y.append(label)


    return np.array(X),np.array(y)

# df=loadData.load()
# process_data(df)