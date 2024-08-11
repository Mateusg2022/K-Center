import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#DATASET https://archive.ics.uci.edu/dataset/343/ujiindoorloc+mag

df = pd.read_csv('UCI_DATA/UCI_DF5/IndoorDF.txt', sep=" ", header=None)

x = df.iloc[:, 3]
y = df.iloc[:, 4]

plt.scatter(x, y, label='Pontos', s=4)
plt.show()