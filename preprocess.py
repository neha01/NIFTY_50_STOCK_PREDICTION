from sklearn import preprocessing
import pandas as pd
import numpy as np


#how many days data will be used to create series to train RNN
SERIES_LENGTH=7

TICKER="NIFTY_50"

def normalize_data(df):
    pass#implement it if you want to use different techniques for normalizing and scaling

def scale_data(df):
    for column in df.columns:
        df[column] = preprocessing.scale(df[column].values)
    return df

def process_data(df):
    df["nifty_future_price"]=df[f"{TICKER}_Close"].shift(-SERIES_LENGTH)

    #Dropping any Nan values
    df.dropna(inplace=True)

    #comparing future nifty price with today's price and labeling it as 1 if price increases and zero otherwise
    df["Label"]=np.where(df["nifty_future_price"]>=df["NIFTY_50_Close"],1,0)
    # print(f"df wth nifty future and label:{df}")

    new_df=pd.DataFrame()
    new_df["Label"]=df['Label'].copy()

    #dropping 'nifty_future_price' and 'label' columns as they are no longer required
    df.drop('nifty_future_price',1,inplace=True)
    df.drop('Label',1,inplace=True)

    df=scale_data(df)

    X=[]
    y=[]
    sequence=[]
    for i in range (len(df)-SERIES_LENGTH):
       sequence.append(np.array(df[i:i+SERIES_LENGTH]))

    final_sequence=[]
    final_sequence=np.array(sequence)

    #shuffling data before feeding it to model
    np.random.shuffle(final_sequence)

    X=final_sequence
    y=np.array(new_df[:-SERIES_LENGTH])
    print("X=",X)
    print("y=",y)
    return X,y