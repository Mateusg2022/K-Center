import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('UCI_DATA/UCI_DF1/ObesityDF.csv')
#print(df.info())
#print(df.columns)

#df_int = df[['Height', 'Weight']]

##print(df_int.info())

x = df['Height']
y = df['Weight']

plt.scatter(x, y, label='Pontos')
plt.show()