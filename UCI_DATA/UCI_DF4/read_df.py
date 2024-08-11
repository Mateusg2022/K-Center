import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#DATASET https://archive.ics.uci.edu/dataset/377/geo+magnetic+field+and+wlan+dataset+for+indoor+localisation+from+wristband+and+smartphone

df = pd.read_csv('UCI_DATA/UCI_DF4/SmartphoneSense.csv')

#df_int = df[['Height', 'Weight']]

##print(df_int.info())

# Posso testar com os outros tb, vamos descutir qual o melhor dps
x = df[' AccelerationX']
y = df[' AccelerationY']

# x = df[' MagneticFieldX']
# y = df[' MagneticFieldY']

# x = df[' X-AxisAngle(Pitch)']
# y = df[' Y-AxisAngle(Roll)']

plt.scatter(x, y, label='Pontos', s=4)
plt.show()