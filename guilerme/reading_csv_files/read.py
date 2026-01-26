import pandas as pd

# instanciando DataFrame a partir de arquivo .csv
df = pd.read_csv('../csv_files/test_file.csv')
print(df)

print("----------------------------")

# printa as primeiras 5 linhas do .csv
print(df.head)

print("----------------------------")

# printa as últimas 5 linhas do .csv
print(df.tail)

print("----------------------------")

# selecionando colunas específicas
two_columns = df[['Nome', 'Idade']]
print(two_columns)

print("----------------------------")

one_column = df['Salario']
print(one_column) # como é só 1 coluna, retorna uma Series

# séries booleanas
print(df['Idade'] > 30)

print("----------------------------")

print(df[df['Idade'] > 30])

print("----------------------------")

# combinando filtros
filtro_maior_que_30 = df['Idade'] > 30
filtro_mais_de_7_mil = df['Salario'] > 7000
print(df[filtro_maior_que_30 & filtro_mais_de_7_mil])
