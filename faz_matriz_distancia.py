import numpy as np

'''
calcula a distancia entre todos os pontos e salva em 'save_dist_matrix.txt'
'''

def minkowski(p1, p2, p):
    p1 = np.array(p1)
    p2 = np.array(p2)
    result = np.sum(np.abs(p1 - p2) ** p)
    return result ** (1 / p)

filename = 'samples/sample_blobs1.txt' 
data = np.loadtxt(filename)
p = 2 #valor de p

num_points = data.shape[0]
distance_matrix = np.zeros((num_points, num_points))

for i in range(num_points):
    for j in range(num_points):
        distance_matrix[i, j] = minkowski(data[i], data[j], p)

np.savetxt('save_dist_matrix.txt', distance_matrix, fmt='%.4f')