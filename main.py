import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

#função de distância de Minkowski
#k-centros 2-aproximado, versao em que o intervalo para o raio ótimo é refinado até
#uma largura definida
#k-centros 2-aproximado, versao em que os centros são escolhidos para maximizar a
#distância entre os centros previamente escolhidos

def minkowski(p1, p2, p):
  #p1 = [x1, y1]
  #p2 = [x2, y2]
  
  p1 = np.array(p1)
  p2 = np.array(p2)

  result = np.sum(np.abs(p1-p2) ** p)
  return result ** (1/p) 

#######
df = pd.read_csv('testes/UCI_DF1/ObesityDF.csv')
x = df['Height']
y = df['Weight']

#normalização simples usando Min-Max Scaling
x = (x - x.min()) / (x.max() - x.min())
y = (y - y.min()) / (y.max() - y.min())
#######

#num_points = 14
#x = [23,22,13,43,31,17,19,29,47,15,23,35,43,14]
#y = [13,22,16,19,33,39,44,31,29,30,41,47,31,28]

used = [False for i in range(0, len(x))]

centers_x = []
centers_y = []

#tentativa com 11 centros
k = 11

# s arbitrario
C = [random.randint(0, len(x) - 1)]
#C = [0]

#p = 1
while len(C) < k:
  s = -1
  max_dist = -1
  for i in range(len(x)):
    if used[i]:
      continue
    min_dist = float('inf')
    for j in C:
      dist = minkowski([x[i], y[i]], [x[j], y[j]], 1)
      if dist < min_dist:
        min_dist = dist
    #procurando a maior distancia entre um ponto e seu centro mais proximo
    if min_dist > max_dist:
      max_dist = min_dist
      s = i
  #salvo os indices da solução
  C.append(s)
  used[s] = True

for i in C:
  centers_x.append(x[i])
  centers_y.append(y[i])

centers_x = np.array(centers_x) 
centers_y = np.array(centers_y)

#####
def calculate_solution_radius(points, centers, p):
    max_radius = 0
    for point in points:
        min_distance = float('inf')
        for center in centers:
            dist = minkowski(point, center, p)
            if dist < min_distance:
                min_distance = dist
        if min_distance > max_radius:
            max_radius = min_distance
    return max_radius

points = list(zip(x, y))
centers = list(zip(centers_x, centers_y))
radius = calculate_solution_radius(points, centers, 1)
print(f"Raio da solução: {radius}")
####

plt.scatter(x, y, label='Pontos')
plt.scatter(centers_x, centers_y, color='red', label='Centros')

plt.show()