import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#DATASET https://archive.ics.uci.edu/dataset/194/wall+following+robot+navigation+data

df = pd.read_csv('UCI_DATA/UCI_DF7/RobotNavigationDF.txt', sep=",", header=None)
x = df.iloc[:, 7]
y = df.iloc[:, 11]

plt.scatter(x, y, label='Pontos', s=4)
plt.show()