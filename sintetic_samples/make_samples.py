import numpy as np
import matplotlib.pyplot as plt
'''doc:
A segunda abordagem consistirá em
gerar dados em duas dimensões usando a distribuição normal multivariada. Nesse
caso, deverão ser gerados pontos amostrados em torno do número de centros (médias
diferentes para cada centro), controlando o desvio padrão para que a sobreposição
entre os grupos varie entre inexistente até altamente sobrepostos (gere uma
quantidade razoável de pontos em cada centro)
'''
def generate_data(centers, num_points, std_dev):
  data = []
  for center in centers:
      points = np.random.multivariate_normal(center, np.eye(2) * std_dev, num_points)
      data.append(points)
  return np.vstack(data)

k = 5  #define o numero de centros
num_points_foreach_center = 1000 #quantos pontos terao ao redor de cada centro
std_devs = [0.5, 1.5, 3.0] #muda o desvio padrao para controlar a sobreposiçao dos pontos

centers = np.random.uniform(-10, 10, size=(k, 2))

#pra cada std gera 4 amostras
for std_dev in std_devs:
  for i in range(4):
    if std_dev == 0.5:
      data = generate_data(centers, num_points_foreach_center, std_dev)
    elif std_dev == 1.5:
      data = generate_data(centers, 2*num_points_foreach_center, std_dev)
    else:
      data = generate_data(centers, 3*num_points_foreach_center, std_dev)
    
    filename = f"sintetic_samples/sample{i+1}_sqtd{std_dev}.txt"
    np.savetxt(filename, data, fmt="%.4f")
