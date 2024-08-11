import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#DATASET https://archive.ics.uci.edu/dataset/760/multivariate+gait+data

df = pd.read_csv('UCI_DATA/UCI_DF2/GaitDF.csv')
#print(df.info())s
#print(df.columns)

#df_int = df[['Height', 'Weight']]

##print(df_int.info())
#
x = df['angle']
y = df['time']

#
plt.scatter(x, y, label='Pontos', s=4)
plt.show()