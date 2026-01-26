import pandas as pd

df = pd.read_csv('../csv_files/test_file.csv')

# criando novas colunas
df['Salario Anual'] = df['Salario'] * 12
print(df)

print("-----------------")

# removendo colunas
df = df.drop('Salario Anual', axis=1) # axis 
print(df)
