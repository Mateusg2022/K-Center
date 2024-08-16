import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from ucimlrepo import fetch_ucirepo 
#https://archive.ics.uci.edu/dataset/890/aids+clinical+trials+group+study+175
# fetch dataset 
  
# fetch dataset 
aids_clinical_trials_group_study_175 = fetch_ucirepo(id=890) 
  
# data (as pandas dataframes) 
label = aids_clinical_trials_group_study_175.data.targets 
x = aids_clinical_trials_group_study_175.data.features.wtkg
y = aids_clinical_trials_group_study_175.data.features.age

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
print(len(x))
print(len(y))
# print(estimation_of_obesity_levels_based_on_eating_habits_and_physical_condition.metadata) 
with open('resultado.txt', 'w') as file:
# Iterando sobre as listas/arrays simultaneamente
    for i in range(len(x)):
    # Escrevendo no arquivo com o formato desejado
        pass
        file.write(f"{x[i]} {y[i]} {label_numeric[i]}\n")
        
plt.scatter(x, y, label='Pontos', s=4)
plt.show()