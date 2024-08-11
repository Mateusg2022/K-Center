import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#DATASET https://archive.ics.uci.edu/dataset/172/ozone+level+detection

df = pd.read_csv('UCI_DATA/UCI_DF6/OzoneLevelDF.txt', sep=",", header=None)
x = df.iloc[:, 1]
y = df.iloc[:, 2]

plt.scatter(x, y, label='Pontos', s=4)
plt.show()