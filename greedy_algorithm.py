import numpy as np
import random
import time
from sklearn.metrics import silhouette_score
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

def load_distance_matrix(filename):
    matrix = np.loadtxt(filename)
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("A matriz de distâncias deve ser quadrada.")
    return matrix

def calculate_solution_radius(distance_matrix, centers):
    max_radius = 0
    for i in range(distance_matrix.shape[0]):
        min_distance = float('inf')
        for center in centers:
            dist = distance_matrix[i][center]
            if dist < min_distance:
                min_distance = dist
        if min_distance > max_radius:
            max_radius = min_distance
    return max_radius

def assign_clusters(distance_matrix, centers):
    labels = []
    for i in range(distance_matrix.shape[0]):
        min_distance = float('inf')
        cluster_label = -1
        for j, center in enumerate(centers):
            dist = distance_matrix[i][center]
            if dist < min_distance:
                min_distance = dist
                cluster_label = j
        labels.append(cluster_label)
    return np.array(labels)

dist_matrix_file = 'save_dist_matrix.txt'
distance_matrix = load_distance_matrix(dist_matrix_file)
#normalização usando Min-Max Scaling
#x = (x - x.min()) / (x.max() - x.min())
#y = (y - y.min()) / (y.max() - y.min())

filename = 'samples/sample_blobs1.txt'
p_value = 2
k_value = 3
algorithm = 'greedy'

used = [False] * distance_matrix.shape[0]
centers = []

#escolher o primeiro centro arbitrariamente
centers.append(random.randint(0, distance_matrix.shape[0] - 1))

start_time = time.time()

#algoritmo guloso de k-centros 2-aproximado (segundo algoritmo ensinado)
while len(centers) < k_value:
    s = -1
    max_dist = -1
    for i in range(distance_matrix.shape[0]):
        if used[i]:
            continue
        min_dist = float('inf')
        for center in centers:
            dist = distance_matrix[i][center]
            if dist < min_dist:
                min_dist = dist
        #procurando a maior distância entre um ponto e seu centro mais próximo
        if min_dist > max_dist:
            max_dist = min_dist
            s = i
    #quando encontrar, salva
    centers.append(s)
    used[s] = True

radius = calculate_solution_radius(distance_matrix, centers)
end_time = time.time()

labels = assign_clusters(distance_matrix, centers)

if distance_matrix.shape[0] == len(labels):
    silhouette_avg = silhouette_score(distance_matrix, labels, metric='precomputed')
else:
    silhouette_avg = -1
    print("Erro: A matriz de distâncias e os rótulos não possuem o mesmo tamanho.")

time_taken = end_time - start_time

with open('current_results.txt', 'a') as file:
    file.write(f"{filename}, {p_value}, {k_value}, {algorithm}, {radius:.4f}, {time_taken:.4f}, {silhouette_avg:.4f}\n")

print(f"Resultados salvos em 'results.txt'.")
