import pandas as pd

df = pd.read_csv('../csv_files/cleaning_data_file.csv')
print(df)

print("--------------")

print(df.sort_values(by='Salario')) # ordem crescente (default)

print("--------------")

print(df.sort_values(by='Salario', ascending=False))
