import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,LSTM,BatchNormalization,Conv1D,MaxPooling1D
import matplotlib.pyplot as plt
import loadData
import preprocess
from sklearn import preprocessing
import pandas as pd


df=loadData.load()

# features=len(df.columns)
training_size=0.8

spilt_point=int(training_size*len(df))

#splitting data for training and testing in ratio 8:2
train_df=df[:spilt_point]
test_df=df[spilt_point:]

print(f"train_df {train_df[:10]}")
print(f"test_df {test_df[:10]}")

train_x,train_y=preprocess.process_data(train_df)

test_x,test_y=preprocess.process_data(test_df)



# print(f"train_x.shape[1:]{train_x.shape[1:]}")

NAME="NIFTY50PRED"
BATCH_SIZE=64
EPOCHS=100


def build_model():

    model=Sequential()
    model.add(LSTM(256,input_shape=(train_x.shape[1:]),return_sequences=True))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())

    model.add(LSTM(256,return_sequences=True))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())

    model.add(LSTM(256,return_sequences=False))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())

    # model.add(LSTM(128,return_sequences=False))
    # model.add(Dropout(0.2))
    # model.add(BatchNormalization())

    model.add(Dense(32,activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(2,activation='softmax'))


    model.compile(loss='sparse_categorical_crossentropy',optimizer="adam",metrics=['accuracy'])


    history=model.fit(train_x,train_y,batch_size=BATCH_SIZE,epochs=EPOCHS,validation_data=(test_x,test_y))
    score=model.evaluate(test_x,test_y)
    print("Validation accuracy percentage",score[1]*100)
    print("Validation loss percentage",score[0]*100)
    # prediction=model.predict(test_x)
    # plt.plot(prediction,color='green',label='predicted_data')
    # plt.plot(test_y,color='blue',label='actual_data')

    # plt.show()

build_model()














