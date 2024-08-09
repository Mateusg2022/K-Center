from sklearn.datasets import make_blobs
from sklearn import cluster, datasets, mixture
import matplotlib.pyplot as plt


n_samples = 500
seed = 30
noisy_circles = datasets.make_circles(
    n_samples=n_samples, factor=0.5, noise=0.05, random_state=seed
)
#gerar dados sintéticos
X, y = noisy_circles
#nome do arquivo onde os dados serão salvos
filename = 'samples/samples1_circle.txt'
with open(filename, 'w') as file:
    for point in X:
        file.write(f"{point[0]:.6f} {point[1]:.6f}\n")

# Criar o gráfico
plt.figure(figsize=(8, 6))

# Plotar os pontos com cores diferentes para cada cluster
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='viridis', edgecolor='k')

# Adicionar título e rótulos aos eixos
plt.title('Dados Sintéticos Gerados com make_blobs')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

# Exibir a legenda
plt.colorbar(label='Cluster ID')

# Mostrar o gráfico
plt.show()