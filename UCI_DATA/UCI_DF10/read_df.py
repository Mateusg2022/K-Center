import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#DATASET https://archive.ics.uci.edu/dataset/196/localization+data+for+person+activity

df = pd.read_csv('UCI_DATA/UCI_DF10/LocalizationDataDF.txt', sep=",", header=None)
x = df.iloc[:, 4]
y = df.iloc[:, 5]

#    1) Sequence Name {A01,A02,A03,A04,A05,B01,B02,B03,B04,B05,C01,C02,C03,C04,C05,D01,D02,D03,D04,D05,E01,E02,E03,E04,E05} (Nominal)
#       - A, B, C, D, E  = 5 people
#    2) Tag identificator {010-000-024-033,020-000-033-111,020-000-032-221,010-000-030-096}	(Nominal)
#       - ANKLE_LEFT = 010-000-024-033
#       - ANKLE_RIGHT = 010-000-030-096
#       - CHEST = 020-000-033-111
#       - BELT = 020-000-032-221
#    3) timestamp (Numeric) all unique
#    4) date FORMAT = dd.MM.yyyy HH:mm:ss:SSS (Date) 
#    5) x coordinate of the tag (Numeric)
#    6) y coordinate of the tag (Numeric)
#    7) z coordinate of the tag (Numeric)
#    8) activity  {walking,falling,'lying down',lying,'sitting down',sitting,'standing up from lying','on all fours','sitting on the ground','standing up from sitting','standing up from sitting on the ground'} (Nominal)
# #normalização usando Min-Max Scaling
# x = (x - x.min()) / (x.max() - x.min())
# y = (y - y.min()) / (y.max() - y.min())


plt.scatter(x, y, label='Pontos', s=4)
plt.show()