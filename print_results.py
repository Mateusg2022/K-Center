import pandas as pd

#lista de arquivos a serem processados
arquivos = [
  'resultadosGulosoDadosReais/UCI_DF1/results_UCI_1_p1.txt',
  'resultadosGulosoDadosReais/UCI_DF1/results_UCI_1_p2.txt',
  'resultadosGulosoDadosSinteticos/sample1/results_sample1_sqtd0.5_p1.txt',
  'resultadosGulosoDadosSinteticos/sample1/results_sample1_sqtd0.5_p2.txt',
  'resultadosGulosoDadosSklearn/sampleBlobs1/results_sample_blobs1_p1.txt',
  'resultadosGulosoDadosSklearn/sampleBlobs1/results_sample_blobs1_p1.txt'#,
  #'resultadosAjusteDadosReais/UCI_DF1/results_sample_UCIDF1_p1_percent0.01.txt',
  #'resultadosAjusteDadosReais/UCI_DF1/results_sample_UCIDF1_p1_percent0.03.txt',
  #'resultadosAjusteDadosReais/UCI_DF1/results_sample_UCIDF1_p1_percent0.05.txt',
  #'resultadosAjusteDadosReais/UCI_DF1/results_sample_UCIDF1_p1_percent0.08.txt',
  #'resultadosAjusteDadosReais/UCI_DF1/results_sample_UCIDF1_p1_percent0.16.txt',
  #'resultadosAjusteDadosReais/UCI_DF1/results_sample_UCIDF1_p2_percent0.01.txt',
  #'resultadosAjusteDadosReais/UCI_DF1/results_sample_UCIDF1_p2_percent0.03.txt',
  #'resultadosAjusteDadosReais/UCI_DF1/results_sample_UCIDF1_p2_percent0.05.txt',
  #'resultadosAjusteDadosReais/UCI_DF1/results_sample_UCIDF1_p2_percent0.08.txt',
  #'resultadosAjusteDadosReais/UCI_DF1/results_sample_UCIDF1_p2_percent0.16.txt',
  #'resultadosGulosoDadosSinteticos/sample1/results_sample1_sqtd0.5_p1.txt',
  #'resultadosGulosoDadosSinteticos/sample1/results_sample1_sqtd0.5_p2.txt',
  #'resultadosAjusteDadosSklearn/sampleBlobs1/results_sample_blobs1_p1.txt',
  #'resultadosAjusteDadosSklearn/sampleBlobs1/results_sample_blobs1_p1.txt',
]

resultados = []

for arquivo in arquivos:
    df = pd.read_csv(arquivo, sep='\t', header=None)

    df = df[0].str.split(',', expand=True)

    df.columns = ['FileName', 'p_value', 'k_value', 'greedy', 'radius', 'time', 'silhueta', 'rand_score_value', 'k-Means_radius', 'k-Means_elapsedTime']
    
    numeric_columns = ['radius', 'time', 'silhueta', 'rand_score_value', 'k-Means_radius', 'k-Means_elapsedTime']
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')
    
    medias = {
        'FileName': df['FileName'].iloc[0],
        'p_value': df['p_value'].iloc[0],
        'k_value': df['k_value'].iloc[0],
        'algorithm': df['algorithm'].iloc[0],
        'radius': df['radius'].mean(),
        'time': df['time'].mean(),
        'silhueta': df['silhueta'].mean(),
        'rand_score_value': df['rand_score_value'].mean(),
        'k-Means_radius': df['k-Means_radius'].mean(),
        'k-Means_elapsedTime': df['k-Means_elapsedTime'].mean(),
    }
        
    resultados.append(medias)

df_resultados = pd.DataFrame(resultados)

df_resultados.to_csv('result_Table1.txt', sep='\t', index=False)

print("Médias calculadas e salvas em 'result_Table.txt'")