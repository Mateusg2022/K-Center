import matplotlib.pyplot as plt
import pandas as pd


data = {
    #sklearn p2 1, uci8, sintetic samples 1,uci2,uci7,uci5
    'x': [500, 800, 1372, 2111, 3124, 3678],
    'y1': [5.4761, 7.9159, 6.9983, 14.7627, 5.30744, 8.469],
    'y2': [4.214274356806862, 4.214865851944925, 7.9543, 12.027071466180587, 5.96649,  6.22570],
    'y3': [8.7532, 5.7969, 8.4001, 14.7349, 7.41312, 11.045]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))

plt.plot(df['x'], df['y1'], label='2-approach greedy', marker='o')
plt.plot(df['x'], df['y2'], label='k-means', marker='s')
plt.plot(df['x'], df['y3'], label='2-approach ajust', marker='s')

plt.title('Comparação entre as soluçoẽs (dados normalizados)')
plt.xlabel('Quantidade de pontos')
plt.ylabel('Raio encontrado')

plt.legend()

plt.grid(True)
plt.show()
