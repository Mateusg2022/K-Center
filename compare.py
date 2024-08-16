import pandas as pd

file_path = 'result_Table1.txt'

df = pd.read_csv(file_path, sep='\t')

print("Conteúdo do DataFrame:")
print(df.head())

mean_radius = df['radius'].mean()
mean_time = df['time'].mean()

mean_k_means_radius = df['k-Means_radius'].mean()
mean_k_means_elapsed_time = df['k-Means_elapsedTime'].mean()

print("\nMédias calculadas:")
print(f"Média do radius: {mean_radius}")
print(f"Média do k-Means_radius: {mean_k_means_radius}")
print(f"Média do time: {mean_time}")
print(f"Média do k-Means_elapsedTime: {mean_k_means_elapsed_time}")

print("\nComparação:")
print(f"radius vs k-Means_radius: {'Maior' if mean_radius > mean_k_means_radius else 'Menor ou Igual'}")
print(f"time vs k-Means_elapsedTime: {'Maior' if mean_time > mean_k_means_elapsed_time else 'Menor ou Igual'}")
