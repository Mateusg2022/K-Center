import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from ucimlrepo import fetch_ucirepo 

#https://archive.ics.uci.edu/dataset/602/dry+bean+dataset
# fetch dataset 
dry_bean = fetch_ucirepo(id=602) 

# data (as pandas dataframes) 
x = dry_bean.data.features.Perimeter.iloc[:3000]
y = dry_bean.data.features.Eccentricity.iloc[:3000]

label = dry_bean.data.targets.Class.iloc[:3000]

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

#
plt.scatter(x, y, label='Pontos', s=4)
plt.show()