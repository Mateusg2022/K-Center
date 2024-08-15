import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from ucimlrepo import fetch_ucirepo 
#https://archive.ics.uci.edu/dataset/172/ozone+level+detection]
# fetch dataset 
ozone_level_detection = fetch_ucirepo(id=172) 
  
# data (as pandas dataframes) 
x = ozone_level_detection.data.features.WSR1
y = ozone_level_detection.data.features.WSR2
label = ozone_level_detection.data.targets

if isinstance(label, pd.DataFrame):
    label = label.squeeze()  # Converter DataFrame para Series se necessário

#Criar um dicionário de mapeamento
unique_labels = label.unique()
label_dict = {lbl: idx for idx, lbl in enumerate(unique_labels)}

#Converter os rótulos para valores numéricos
label_numeric = label.map(label_dict)

print(label_numeric)

num_unique_labels = label.nunique()
print("Quantidade de valores diferentes em 'label':", num_unique_labels)
# # metadata 
# print(estimation_of_obesity_levels_based_on_eating_habits_and_physical_condition.metadata) 
with open('resultado.txt', 'w') as file:
# Iterando sobre as listas/arrays simultaneamente
    for i in range(len(x)):
    # Escrevendo no arquivo com o formato desejado
        file.write(f"{x[i]} {y[i]} {label_numeric[i]}\n")
        
plt.scatter(x, y, label='Pontos', s=4)
plt.show()