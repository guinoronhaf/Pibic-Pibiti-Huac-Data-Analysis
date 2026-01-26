import pandas as pd

df = pd.read_csv('../csv_files/cleaning_data_file.csv')
print(df)

print("-------------------")

# removendo todas as linhas que tem pelo menos um NaN
print(df.dropna())

print("-------------------")

# removendo as linhas que possuem valores nulos (NaN) para a coluna 'Idade'
print(df.dropna(subset='Idade'))

print("-------------------")

# preenchendo os valores nulos com outro valor
media_idade = df['Idade'].mean() # pega a média dos valores da coluna 'Idade'
df['Idade'] = df['Idade'].fillna(media_idade) # substitui os valores NaN em 'Idade' por media_idade
print(df)

print("-------------------")

# alterando o tipo de dado de uma coluna específica
df['Idade'] = df['Idade'].astype(int) # agora, a coluna 'Idade' aceita valores do tipo inteiro
print(df.info())
