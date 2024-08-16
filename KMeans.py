import numpy as np
from sklearn.cluster import KMeans
import time

def load_data(filename):
    return np.loadtxt(filename)

def calculate_cluster_radii(points, labels, cluster_centers):
    radii = []
    for i, center in enumerate(cluster_centers):
        # Seleciona os pontos do cluster i
        cluster_points = points[labels == i]
        # Calcula a distância de cada ponto do cluster ao centro do cluster
        distances = np.linalg.norm(cluster_points - center, axis=1)
        # O raio é a distância máxima do ponto mais distante
        radii.append(np.max(distances))
    return radii

def KmeansResult(fileName: str, kV: int):
    X = np.loadtxt(fileName, usecols=(0,1)) #Pegar so as colunas das coordenadas X e Y
    # X = load_data(fileName)
    k = kV

    start_time = time.time()
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(X)
    end_time = time.time()

    cluster_centers = kmeans.cluster_centers_
    predicted_labels = kmeans.labels_

    radius = calculate_cluster_radii(X, predicted_labels, cluster_centers)
    elapsed_time = end_time - start_time

    max_radius = max(radius)

    print(f"Raio da solução: {max_radius}")
    print(f"Tempo de execução: {elapsed_time:.4f} segundos")
    return max_radius, elapsed_time