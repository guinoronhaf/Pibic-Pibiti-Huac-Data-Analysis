import pandas as pd

df = pd.read_csv('../csv_files/cleaning_data_file.csv')
print(df)

print("-----------------")

# contando ocorrências
print(df['Ativo'].value_counts())
print(df['ID Departamento'].value_counts())

print("-----------------")

# agrupando e agregando
print(df.groupby('ID Departamento')) # retorna um DataFrame Group By
print("-----------------")
print(df.groupby('ID Departamento')['Salario'].mean()) # média dos salaŕios dos funcionários agrupados pelo ID do departamento
print("-----------------")
print(df.groupby('ID Departamento')['Salario'].sum())
print(df.groupby('ID Departamento')['Salario'].max())
