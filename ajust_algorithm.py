import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn.metrics import silhouette_score, adjusted_rand_score

#------------------------------------------
#• Seja S’ = S; C = ∅
#• Enquanto S’ ≠ ∅
#•   Selecione arbitrariamente um ponto s ∈ S’ e coloque-o em C
#•   Remova de S’ todos os pontos que estiverem a uma distância máxima de 2r de s
#• Se |C| ≤ k, retorne C
#• Senão, não há solução
#------------------------------------------

#função de distância de Minkowski
def minkowski(p1, p2, p):
    p1 = np.array(p1)
    p2 = np.array(p2)
    result = np.sum(np.abs(p1 - p2) ** p)
    return result ** (1 / p)

def max_dist(S):
    max_distance = -1
    for i in S:
        for j in S:
            curr = minkowski(i, j, 2)
            if not np.array_equal(i, j) and curr > max_distance:
                max_distance = curr
    return max_distance

'''
tem q ajustar para o usuario passar o caminho do arquivo como parametro
'''
#ler dados do arquivo
filename = 'sintetic_samples/sample1_sqtd0.5.txt'
data = np.loadtxt(filename)

x = data[:, 0]
y = data[:, 1]

'''
#normalização usando Min-Max Scaling
x = (x - x.min()) / (x.max() - x.min())
y = (y - y.min()) / (y.max() - y.min())
'''

#inicialização
k = 3
r = float('inf')
rmax = max_dist(data)
left = 0
right = rmax
print('rmax:', rmax)
percent = 0.00001
C = []
#enquanto os L e R nao convergirem para valores proximos
while r / rmax > percent:
    r = (left + right) / 2
    C = []
    S = data.copy()
    
    while len(S) > 0 and len(C) < k:
      s = random.randint(0, len(S) - 1)
      C.append(S[s])
      
      to_remove = [p for p in range(len(S)) if minkowski(S[p], S[s], 2) <= 2 * r]
      S = np.delete(S, to_remove, axis=0)
    
    if len(C) <= k:
      right = r
    else:
      left = r

centers_x = [center[0] for center in C]
centers_y = [center[1] for center in C]

#calcula o raio da solução
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
radius = calculate_solution_radius(points, centers, 2)
print(f"Raio da solução: {radius}")

#atribuir cores diferentes aos pontos de cada cluster
def assign_clusters(points, centers):
    labels = []
    for point in points:
        min_distance = float('inf')
        cluster_label = -1
        for i, center in enumerate(centers):
            dist = minkowski(point, center, 2)
            if dist < min_distance:
                min_distance = dist
                cluster_label = i
        labels.append(cluster_label)
    return np.array(labels)

labels = assign_clusters(points, centers)

#silhueta
silhouette_avg = silhouette_score(data, labels)
print(f"Coeficiente de Silhueta: {silhouette_avg}")


plt.figure(figsize=(8, 6))
scatter = plt.scatter(x, y, c=labels, cmap='viridis', edgecolor='k')
plt.scatter(centers_x, centers_y, color='red', marker='x', s=100, label='Centros')

plt.title('Clusters e Centros')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.colorbar(scatter, label='Cluster ID')
plt.show()
