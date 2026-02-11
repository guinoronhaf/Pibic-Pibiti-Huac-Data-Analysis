import pandas as pd

data = pd.read_csv("test_archive.csv")

df = pd.DataFrame(data)

print("====\n")
print(df[["id_pedido", "produto"]]) # filtrar por colunas
print("\n====\n")

print(df[df["preco_unitario"] > 900]) # filtrar o Data Frame por condições -> recebe uma expressão bolleana
print("\n====\n")

# função que preserva o dataFrame original -> prog. Funcional 
def aumentar_coluna(df):
    copy_dataframe = df.copy()
    copy_dataframe["preco_com_desconto"] = copy_dataframe["preco_unitario"] * 0.90 # função de efeito colateral no Data Frame aumentando uma coluna
    return copy_dataframe

print(aumentar_coluna(df))
print("\n====\n")
print(df)
print("\n====\n")

print(df.describe()) # realiza uma descrição geral do DataFrame 
# count -> conta quantas linhas apresentam dados dessa coluna
# mean -> media dos valores das linhas dessa coluna
# min -> minimo dos valores das linhas dessa coluna
# std -> Desvio padrão dos valores das linhas dessa coluna
print("\n====\n")

print(df.describe(include=[object])) ## realiza a descrição apenas de colunas com valores de String
# count -> conta quantas linhas apresentam dados dessa coluna
# unique -> conta qunatas linhas são unicas
# top -> valor com maior frequencia 
# freq -> frequencia do valor top
print("\n====\n")

print(df["produto"].count()) # existe os metodos para cada detalhe apontado no describe, sendo possivel aplicar para cada coluna
print("\n====\n")
print(df["preco_unitario"].sum())
print("\n====\n")
print(df["produto"].is_unique) # verifica se a coluna tem apenas valores unicos
print("\n====\n")
print(df["preco_unitario"].mean())
print("\n====\n")
print(df["preco_unitario"].median())
print("\n====\n")
print(df["preco_unitario"].max())
print("\n====\n")
print(df["pagamento"].value_counts()) # conta a frequencia de cada valor (Group by ... Count)
print("\n====\n")
print(df.groupby("categoria")["preco_unitario"].mean()) # agrupa as categorias e determina a media de preco entre elas
print("\n====\n")

def group_by_dataframe(df, column_to_group, colum_operation, function_name):
    return df.groupby(column_to_group)[colum_operation].agg(function_name)

print(group_by_dataframe(df, "produto", "quantidade", "mean"))

print("\n====\n")
print(df.dropna()) # retorna um DataFrame que remove todas as linhas que contem NAN
print("\n====\n")
print(df.dropna(subset="quantidade")) # remove apenas as linhas que tem essa coluna com NAN
print("\n====\n")
print(df.dropna(subset=["quantidade", "categoria"])) # remove as linhas que tem pelo menos uma dessas linhas com NAN
print("\n====\n")

# funcao que retorna um dataframe com filtro NAN na coluna 'qauntidade' -> prog. funcional
def fillna_dataframe(df):
    dataframe_copy = df.copy()
    dataframe_copy["quantidade"] = dataframe_copy["quantidade"].fillna(0)
    return dataframe_copy

dataframe_fillNaN = fillna_dataframe(df)
print(dataframe_fillNaN)
print("\n====\n")

df["quantidade"] = df["quantidade"].fillna(0) # mapeia as linhas da coluna que tem valor NAN para 0.

print(df)