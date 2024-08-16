import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
'''doc:
A segunda abordagem consistirá em
gerar dados em duas dimensões usando a distribuição normal multivariada. Nesse
caso, deverão ser gerados pontos amostrados em torno do número de centros (médias
diferentes para cada centro), controlando o desvio padrão para que a sobreposição
entre os grupos varie entre inexistente até altamente sobrepostos (gere uma
quantidade razoável de pontos em cada centro)
'''
def generate_points_df(n, m=5, cov=np.eye(2)):
    def generate_points(n, mean, cov):
        points = np.random.multivariate_normal(mean, cov, n)
        return points

    means = np.random.randint(-15, 15, size=(m,2))
    data = []
    labels = []

    for i, mean in enumerate(means):
        cov = np.eye(2)
        cov = np.array([[1, 0.4], [0.4, 1]])
        points = generate_points(n, mean, cov)
        labels += [i] * n
        data.append(points)

    df = pd.DataFrame(np.vstack(data), columns=['x', 'y'])
    df['label'] = labels
    return df

# def generate_data(centers, num_points, std_dev):
#   data = []
#   for center in centers:
#       points = np.random.multivariate_normal(center, np.eye(2) * std_dev, num_points)
#       data.append(points)
#   return np.vstack(data)

k = 5  #define o numero de centros
num_points_foreach_center = int(800/k) #quantos pontos terao ao redor de cada centro
std_devs = [0.5, 1.5, 3.0] #muda o desvio padrao para controlar a sobreposiçao dos pontos

#pra cada std gera 3 amostras
for std_dev in std_devs:
  for i in range(0, 10):
    data = generate_points_df(num_points_foreach_center, k, std_dev)
    filename = f"sintetic_samples/sample{i+1}_sqtd{std_dev}.txt"
    data.to_csv(filename, sep=' ', index=False, float_format='%.4f')

plt.figure(figsize=(10, 6))

# Se você quiser colorir os pontos por label, faça o seguinte:
# for label in data['label'].unique():
#     subset = data[data['label'] == label]
#     plt.scatter(subset['x'], subset['y'], label=f'Label {label}', s=100)  # s=100 para aumentar o tamanho dos pontos

# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Gráfico de Dispersão de X vs Y com Labels')
# plt.legend()
# plt.grid(True)
# plt.show()
