import numpy as np
from sklearn import datasets

def save_data_to_file(filename, data):
    np.savetxt(filename, data, fmt='%.6f', comments='')

n_samples = 500
seed = 30
np.random.seed(seed)

#gera amostras de dados com circulos, meia-luas e etc
noisy_circles1 = datasets.make_circles(n_samples=n_samples, factor=0.5, noise=0.05, random_state=30)
noisy_circles2 = datasets.make_circles(n_samples=n_samples, factor=0.5, noise=0.1, random_state=120)

blobs1 = datasets.make_blobs(n_samples=n_samples, random_state=30)
blobs2 = datasets.make_blobs(n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=120)

moons1 = datasets.make_moons(n_samples=n_samples, noise=0.05, random_state=30)
moons2 = datasets.make_moons(n_samples=n_samples, noise=0.1, random_state=120)

aniso = datasets.make_blobs(n_samples=n_samples, random_state=170)
transformation = [[0.6, -0.6], [-0.4, 0.8]]
X_aniso = np.dot(aniso[0], transformation)
aniso = (X_aniso, aniso[1])

varied1 = datasets.make_blobs(n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=120)
varied2 = datasets.make_blobs(n_samples=n_samples, cluster_std=[0.5, 1.5, 0.5], random_state=30)

datasets = [
    (
        noisy_circles1,
        {
            "damping": 0.77,
            "preference": -240,
            "quantile": 0.2,
            "n_clusters": 2,
            "min_samples": 7,
            "xi": 0.08,
        }
    ),
    ( 
        noisy_circles2,
        {
            "damping": 0.77,
            "preference": -240,
            "quantile": 0.2,
            "n_clusters": 2,
            "min_samples": 7,
            "xi": 0.08,
        },
    ),
    (
        moons1,
        {
            "damping": 0.75,
            "preference": -220,
            "n_clusters": 2,
            "min_samples": 7,
            "xi": 0.1,
        },
    ),
    (
        moons2,
        {
            "damping": 0.75,
            "preference": -220,
            "n_clusters": 2,
            "min_samples": 7,
            "xi": 0.1,
        },
    ),
    (
        varied1,
        {
            "eps": 0.18,
            "n_neighbors": 2,
            "min_samples": 7,
            "xi": 0.01,
            "min_cluster_size": 0.2,
        }
    ),
    (
        varied2,
        {
            "eps": 0.18,
            "n_neighbors": 2,
            "min_samples": 7,
            "xi": 0.01,
            "min_cluster_size": 0.2,
        },
    ),
    # (
    #     aniso,
    #     {
    #         "eps": 0.15,
    #         "n_neighbors": 2,
    #         "min_samples": 7,
    #         "xi": 0.1,
    #         "min_cluster_size": 0.2,
    #     },
    # ),
    (
        blobs1, 
        {
            "min_samples": 7, 
            "xi": 0.1, 
            "min_cluster_size": 0.2
        },
    ),
    (
        blobs2,
        {
            "min_samples": 7, 
            "xi": 0.1, 
            "min_cluster_size": 0.2
        },
    )
]

filenames = ['noisy_circles1', 'noisy_circles2', "moons1", "moons2", 'varied1', 'varied2', "blobs1", "blobs2"]
for i, (dataset, algoparams) in enumerate(datasets):
    try:
        X = dataset[0]
        y = dataset[1]
        data = np.concatenate([X, y.reshape(-1, 1)], axis=1)
#Salvar no formato .txt com X Y label em cada linha
        with open(f"sample_{filenames[i]}.txt", 'w') as f:
            for row in data:
                f.write(f"{row[0]} {row[1]} {int(row[2])}\n")
    except:
        X = dataset[0]

#Salvar no formato .txt com X Y em cada linha (sem o label)
        with open(f"df_{i}.txt", 'w') as f:
            for row in X:
                f.write(f"{row[0]} {row[1]}\n")

# save_data_to_file('samples/sample_circles1.txt', noisy_circles1[0])
# save_data_to_file('samples/sample_circles2.txt', noisy_circles2[0])
# save_data_to_file('samples/sample_blobs1.txt', blobs1[0])
# save_data_to_file('samples/sample_blobs2.txt', blobs2[0])
# save_data_to_file('samples/sample_moons1.txt', moons1[0])
# save_data_to_file('samples/sample_moons2.txt', moons2[0])
# save_data_to_file('samples/sample_aniso.txt', aniso[0])
# save_data_to_file('samples/sample_varied1.txt', varied1[0])
# save_data_to_file('samples/sample_varied2.txt', varied2[0])
