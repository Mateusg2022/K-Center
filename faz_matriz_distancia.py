import numpy as np

'''
calcula a distancia entre todos os pontos e salva em 'save_dist_matrix.txt'
'''

def minkowski(p1, p2, p):
    p1 = np.array(p1)
    p2 = np.array(p2)
    result = np.sum(np.abs(p1 - p2) ** p)
    return result ** (1 / p)

# std_devs = [0.5, 1.5, 3.0]

currSample = 4
# for i in std_devs:
prefixFileName = f'UCI_DATA/UCI_DF{currSample}' 
for h in [1, 2]:
    # for k in std_devs:
        filename = f'{prefixFileName}/resultado.txt'

        data = np.loadtxt(filename, usecols=(0, 1)) #Pegar so as colunas das coordenadas X e Y
        p = h #valor de p

        num_points = data.shape[0]
        distance_matrix = np.zeros((num_points, num_points))

        for i in range(num_points):
            for j in range(num_points):
                distance_matrix[i, j] = minkowski(data[i], data[j], p)

        np.savetxt(f'save_dist_matrix_sample_UCIDF{currSample}_P{p}.txt', distance_matrix, fmt='%.4f')

# currSample = "varied2"
# # for i in std_devs:
# prefixFileName = 'sklearn_samples' 
# for h in [1, 2]:
#     # for k in std_devs:
#         filename = f'{prefixFileName}/sample_{currSample}.txt'

#         data = np.loadtxt(filename, usecols=(0, 1)) #Pegar so as colunas das coordenadas X e Y
#         p = h #valor de p

#         num_points = data.shape[0]
#         distance_matrix = np.zeros((num_points, num_points))

#         for i in range(num_points):
#             for j in range(num_points):
#                 distance_matrix[i, j] = minkowski(data[i], data[j], p)

#         np.savetxt(f'save_dist_matrix_sample_{currSample}_P{p}.txt', distance_matrix, fmt='%.4f')