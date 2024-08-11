import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#DATASET https://archive.ics.uci.edu/dataset/554/cnnpred+cnn+based+stock+market+prediction+using+a+diverse+set+of+variables

df = pd.read_csv('UCI_DATA/UCI_DF9/CiscoSecureDF.csv')
x = df['nr']
y = df['i1_legid']

#normalização usando Min-Max Scaling
x = (x - x.min()) / (x.max() - x.min())
y = (y - y.min()) / (y.max() - y.min())


plt.scatter(x, y, label='Pontos', s=4)
plt.show()