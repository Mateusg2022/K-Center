import numpy as np
from sklearn import datasets

# Função para salvar os dados em um arquivo
def save_data_to_file(filename, data):
    np.savetxt(filename, data, fmt='%.6f', comments='')

# Definir o número de amostras e o estado aleatório
n_samples = 500
seed = 30
np.random.seed(seed)

# Gerar amostras de dados
noisy_circles1 = datasets.make_circles(n_samples=n_samples, factor=0.5, noise=0.05, random_state=seed)
noisy_circles2 = datasets.make_circles(n_samples=n_samples, factor=0.5, noise=0.1, random_state=seed)

blobs1 = datasets.make_blobs(n_samples=n_samples, random_state=seed)
blobs2 = datasets.make_blobs(n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=seed)

moons1 = datasets.make_moons(n_samples=n_samples, noise=0.05, random_state=seed)
moons2 = datasets.make_moons(n_samples=n_samples, noise=0.1, random_state=seed)

aniso = datasets.make_blobs(n_samples=n_samples, random_state=170)
transformation = [[0.6, -0.6], [-0.4, 0.8]]
X_aniso = np.dot(aniso[0], transformation)
aniso = (X_aniso, aniso[1])

varied1 = datasets.make_blobs(n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=170)
varied2 = datasets.make_blobs(n_samples=n_samples, cluster_std=[0.5, 1.5, 0.5], random_state=170)

# Salvar os dados em arquivos
save_data_to_file('samples/sample_circles1.txt', noisy_circles1[0])
save_data_to_file('samples/sample_circles2.txt', noisy_circles2[0])
save_data_to_file('samples/sample_blobs1.txt', blobs1[0])
save_data_to_file('samples/sample_blobs2.txt', blobs2[0])
save_data_to_file('samples/sample_moons1.txt', moons1[0])
save_data_to_file('samples/sample_moons2.txt', moons2[0])
save_data_to_file('samples/sample_aniso.txt', aniso[0])
save_data_to_file('samples/sample_varied1.txt', varied1[0])
save_data_to_file('samples/sample_varied2.txt', varied2[0])
