import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#https://archive.ics.uci.edu/dataset/267/banknote+authentication

from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
banknote_authentication = fetch_ucirepo(id=267) 
  
# data (as pandas dataframes) 
x = banknote_authentication.data.features.variance
y = banknote_authentication.data.features.entropy 
label = banknote_authentication.data.targets 
  
# metadata 
print(banknote_authentication.metadata) 
  
# variable information 
print(banknote_authentication.variables) 



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