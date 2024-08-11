import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#DATASET https://archive.ics.uci.edu/dataset/554/cnnpred+cnn+based+stock+market+prediction+using+a+diverse+set+of+variables

df = pd.read_csv('UCI_DATA/UCI_DF8/StockMarketPredictionDF.csv')
print (df.columns)
x = df['mom']
y = df['TE2']

plt.scatter(x, y, label='Pontos', s=4)
plt.show()