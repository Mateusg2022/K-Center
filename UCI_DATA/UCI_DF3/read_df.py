import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#DATASET https://archive.ics.uci.edu/dataset/286/user+identification+from+walking+activity

df = pd.read_csv('UCI_DATA/UCI_DF3/WalkingDF.csv', header=None)

#df_int = df[['Height', 'Weight']]

##print(df_int.info())
#
x = df.iloc[:, 1]
y = df.iloc[:, 2]

plt.scatter(x, y, label='Pontos', s=4)
plt.show()