import pandas as pd

df = pd.read_csv('../csv_files/test_file.csv')
print(df)

print("--------------")

print(df.info()) # resumo informativo do DataFrame: tipo dos dados em cada uma das colunas, se tem valores nulos ou não nas colunas

print("--------------")

print(df.describe()) # resumo estatístico das colunas numéricas

print("--------------")

print(df['Salario'].sum()) # resumo estatístico de uma coluna específica
print(df['Salario'].mean()) # média dos salaŕios
