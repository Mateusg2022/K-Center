import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn.metrics import silhouette_score, adjusted_rand_score

##############################################
#PSEUDO-CÓDIGO
#Se k ≥ |S|, retorne S
#• Senão, selecione s arbitrário e crie C={s}
#• Enquanto |C| < k
#•  Selecione s que maximize dist(s,C)
#•  Adicione s a C
#• Retorne C
##############################################

#função de distância de Minkowski
def minkowski(p1, p2, p):
    p1 = np.array(p1)
    p2 = np.array(p2)
    result = np.sum(np.abs(p1 - p2) ** p)
    return result ** (1 / p)

#ler dados do arquivo
filename = 'samples/sample_blobs1.txt'
data = np.loadtxt(filename)

x = data[:, 0]
y = data[:, 1]

#normalização usando Min-Max Scaling
#x = (x - x.min()) / (x.max() - x.min())
#y = (y - y.min()) / (y.max() - y.min())

#inicialização
used = [False for _ in range(len(x))]
centers_x = []
centers_y = []

#tentativa com 2 centros
k = 3

#escolher o primeiro centro arbitrariamente
C = [random.randint(0, len(x) - 1)]

#algoritmo guloso de k-centros 2-aproximado (segundo algoritmo ensinado)
while len(C) < k:
    s = -1
    max_dist = -1
    for i in range(len(x)):
        if used[i]:
            continue
        min_dist = float('inf')
        for j in C:
            dist = minkowski([x[i], y[i]], [x[j], y[j]], 2)
            if dist < min_dist:
                min_dist = dist
        #procurando a maior distância entre um ponto e seu centro mais próximo
        if min_dist > max_dist:
            max_dist = min_dist
            s = i
    #quando encontrar, salva
    C.append(s)
    used[s] = True

for i in C:
    centers_x.append(x[i])
    centers_y.append(y[i])

centers_x = np.array(centers_x)
centers_y = np.array(centers_y)

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

#plot
plt.figure(figsize=(8, 6))
scatter = plt.scatter(x, y, c=labels, cmap='viridis', edgecolor='k')
plt.scatter(centers_x, centers_y, color='red', marker='x', s=100, label='Centros')

plt.title('Clusters e Centros')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.colorbar(scatter, label='Cluster ID')

plt.show()
