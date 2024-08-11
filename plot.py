import numpy as np
import matplotlib.pyplot as plt
#-------------------------------------------------------------------
#plota os pontos de um arquivo, só para a visualizao da distribuição
#dos pontos antes dos testes
#-------------------------------------------------------------------
def read_and_plot(filename):
    data = np.loadtxt(filename)
    
    x = data[:, 0]
    y = data[:, 1]
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, s=10, c='blue', label='Pontos')
    plt.title('plot')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

filename = 'sintetic_samples/sample3_sqtd0.5.txt'
read_and_plot(filename)
