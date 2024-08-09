import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('testes/UCI_DF3/ObesityDF.csv')
#print(df.info())
#print(df.columns)

#df_int = df[[2, 3]]

##print(df_int.info())
#
x = df['Height']
y = df['Weight']
#
plt.scatter(x, y, label='Pontos')
plt.show()