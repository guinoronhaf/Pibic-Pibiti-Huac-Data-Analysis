import pandas as pd

# a principal estrutura de dados em Pandas é o DataFrame, que é como se fosse uma tabela (planilha) de Excel

dados = {
        "Nome": ["Ana", "Bruno", "Carlos"],
        "Idade": [25, 47, 32]
}

df = pd.DataFrame(dados)

print(df)

print("======")

# a Series é como se fosse uma coluna do Pandas
s = pd.Series([10, 20, 30])
print(s)
