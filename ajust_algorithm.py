import matplotlib.pyplot as plt
import numpy as np
import random
import KMeans 
import time
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

def max_dist(S, pvalordoscrias):
    max_distance = -1
    for i in S:
        for j in S:
            curr = minkowski(i, j, pvalordoscrias)
            if not np.array_equal(i, j) and curr > max_distance:
                max_distance = curr
    return max_distance

def load_distance_matrix(filename):
    matrix = np.loadtxt(filename)
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("A matriz de distâncias deve ser quadrada.")
    return matrix

def assign_clusters(points, centers, pvalordoscrias):
    labels = []
    for point in points:
        min_distance = float('inf')
        cluster_label = -1
        for i, center in enumerate(centers):
            dist = minkowski(point, center, pvalordoscrias)
            if dist < min_distance:
                min_distance = dist
                cluster_label = i
        labels.append(cluster_label)
    return np.array(labels)
#calcula o raio da solução
def calculate_solution_radius(points, centers, pvalordoscrias):
    max_radius = 0
    for point in points:
        min_distance = float('inf')
        for center in centers:
            dist = minkowski(point, center, pvalordoscrias)
            if dist < min_distance:
                min_distance = dist
        if min_distance > max_radius:
            max_radius = min_distance
    return max_radius

# def calculate_solution_radius(distance_matrix, centers):
#     max_radius = 0
#     for i in range(distance_matrix.shape[0]):
#         min_distance = float('inf')
#         for center in centers:
#             dist = distance_matrix[i][center]
#             if dist < min_distance:
#                 min_distance = dist
#         if min_distance > max_radius:
#             max_radius = min_distance
#     return max_radius

# def calculate_solution_radius(distance_matrix, centers):
#     max_radius = 0
#     for i in range(distance_matrix.shape[0]):
#         min_distance = float('inf')
#         for center in centers:
#             dist = distance_matrix[i][center]
#             if dist < min_distance:
#                 min_distance = dist
#         if min_distance > max_radius:
#             max_radius = min_distance
#     return max_radius
    
'''
tem q ajustar para o usuario passar o caminho do arquivo como parametro
'''
#ler dados do arquivo

percentList=[0.01, 0.03, 0.05, 0.08, 0.16]
currBase = 5
filePrefix = f"UCI_DATA/UCI_DF{currBase}"

filename = filePrefix + f'/resultado.txt' 
trueLabels = np.loadtxt(filename, usecols=(2)) #Pegar so as colunas das coordenadas X e Y
data = np.loadtxt(filename)

x = data[:, 0]
y = data[:, 1]

# dist_matrix_file = f'save_dist_matrix_sample_UCIDF{currBase}_P{pValue}.txt'
# distance_matrix = load_distance_matrix(dist_matrix_file)

filename = filePrefix + '/nCentros.txt' 
kValue = np.loadtxt(filename)
for pvalordoscrias in [1, 2]: #Rodando pros dois p
    rmax = max_dist(data[:,:2], pvalordoscrias)

    for percent in percentList:
        with open(f'results_sample_UCIDF{currBase}_p{pvalordoscrias}_percent{percent}.txt', 'a') as file:
            file.write(f"FileName, p_value, k_value, algorithm, radius, time, silhueta, rand_score_value, k-Means_radius, k-Means_elapsedTime\n")

        for i in range(0, 29):
            #inicialização
            algorithm = 'adjust'
            k = kValue
            r = float('inf')
            left = 0
            right = rmax
            print('rmax:', rmax)
            C = []

            start_time = time.time()

            #enquanto os L e R nao convergirem para valores proximos
            while r / rmax > percent:
                r = (left + right) / 2
                C = []
                S = data.copy()
                
                while len(S) > 0 and len(C) < k:
                    s = random.randint(0, len(S) - 1)
                    C.append(S[s])
                
                    to_remove = [p for p in range(len(S)) if minkowski(S[p], S[s], pvalordoscrias) <= 2 * r]
                    S = np.delete(S, to_remove, axis=0)
                
                if len(C) <= k:
                    right = r
                else:
                    left = r

            centers_x = [center[0] for center in C]
            centers_y = [center[1] for center in C]

            points = list(zip(x, y))
            centers = list(zip(centers_x, centers_y))

            radius = calculate_solution_radius(points, centers, pvalordoscrias)
            print(f"Raio da solução: {radius}")

            #atribuir cores diferentes aos pontos de cada cluster
            end_time = time.time()

            labels = assign_clusters(points, centers, pvalordoscrias)

            #indice de rand

            rand_score_value = adjusted_rand_score(trueLabels, labels)

            #silhueta
            silhouette_avg = silhouette_score(data, labels)
            print(f"Coeficiente de Silhueta: {silhouette_avg}")

            time_taken = end_time - start_time

            (kMeansRadius, elapsed_time) = KMeans.KmeansResult(filePrefix + f'/resultado.txt', int(kValue))

            with open(f'results_sample_UCIDF{currBase}_p{pvalordoscrias}_percent{percent}.txt', 'a') as file:
                file.write(f"{filename}, {pvalordoscrias}, {kValue}, {algorithm}, {radius:.4f}, {time_taken:.4f}, {silhouette_avg:.4f}, {rand_score_value:.4f}, {kMeansRadius:.4f}, {elapsed_time:.4f}\n")
























# plt.figure(figsize=(8, 6))
# scatter = plt.scatter(x, y, c=labels, cmap='viridis', edgecolor='k')
# plt.scatter(centers_x, centers_y, color='red', marker='x', s=100, label='Centros')

# plt.title('Clusters e Centros')
# plt.xlabel('Feature 1')
# plt.ylabel('Feature 2')
# plt.legend()
# plt.colorbar(scatter, label='Cluster ID')
# plt.show()
