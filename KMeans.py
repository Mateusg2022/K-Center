import numpy as np
from sklearn.cluster import KMeans
import time

def load_data(filename):
    return np.loadtxt(filename)

def calculate_solution_radius(X, centers, labels):
    max_radius = 0
    for i in range(len(centers)):
        cluster_points = X[labels == i]
        center = centers[i]
        max_dist = np.max([np.linalg.norm(point - center) for point in cluster_points])
        if max_dist > max_radius:
            max_radius = max_dist
    return max_radius

def main():
    
    filename = 'samples/sample_blobs1.txt'
    X = load_data(filename)

    k = 5

    kmeans = KMeans(n_clusters=k, random_state=0, n_init='auto')
    start_time = time.time()
    kmeans.fit(X)
    end_time = time.time()

    centers = kmeans.cluster_centers_
    labels = kmeans.labels_

    radius = calculate_solution_radius(X, centers, labels)
    elapsed_time = end_time - start_time

    print(f"Raio da solução: {radius}")
    print(f"Tempo de execução: {elapsed_time:.4f} segundos")

if __name__ == '__main__':
    main()
