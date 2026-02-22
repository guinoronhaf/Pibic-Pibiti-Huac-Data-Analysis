import pandas as pd

def map_times_by_rate(df_to_map):
    times_dict = {}
    for i in range(0, 11):
        times_dict[i] = df_to_map.loc[df_to_map['rate'] == i, 'times_chosen'].values

        if list(times_dict[i]) == []:
            times_dict[i] = 0
        else:
            times_dict[i] = int(times_dict[i][0])

    return times_dict

def get_data_frame_app_rate(df):
    df_rate_group = df["ia_confiavel"].value_counts().reset_index() # tranforma em um DataFrame (Series -> DataFrame)

    df_rate_group.columns = ["rate", "times_chosen"]

    return df_rate_group

# faz o agrupamneto das especialidades demonstrando a quantidade total para cada especialidade
# alem de destacar a porcentagem em relação a quntidade total de respostas
def group_speciality_quantity(df):
    df_group = df.groupby("area_atuacao")["data_hora"].count().rename("Times Chosen").reset_index()

    df_group_percent = add_speciality_percentage_column(df_group)

    df_group_percent.set_index('area_atuacao', inplace=True)

    return df_group_percent.rename(columns={"area_atuacao": "Specialisties"})

# adiciona a coluna de porcentagem sob a quantidade
# retorna um Data Frama que é agupado com quantidade e porcentagem total
def add_speciality_percentage_column(df_group):
    df_sum = df_group["Times Chosen"].sum()

    df_group["Percentage"] = ((df_group["Times Chosen"] / df_sum) * 100)

    return df_group

# corsstab -> reotorna uma matriz em que os valores do primeira coluna é o identificador das linhas
#          -> e que os valores do sgundo parametro são os identificadores das colunas
#          -> as linhas desse DataFrama apresnetam a contagem de ocorrencias entre os valores de linha e coluna
# ex:
#                          1-3 anos  4-7 anos  8-15 anos  Mais de 15 anos  Menos de 1 ano                                                 
# Médico Especialista           0        10         11               11               0
# Médico Residente             10         0          0                0               6
# Técnico em Radiologia         1         0          0                0               1
def group_percentage_years_specialist(df_orig):
    result_percentage = pd.crosstab(df_orig["area_atuacao"], 
                                    df_orig["experiencia"], 
                                    normalize='index') * 100 # realiza o calculo com base no total da linha
    
    map_values_UI = {
        'Não possuo experiência em laudos de exames de Radiologia': 'Nenhuma',
    }
    
    result_percentage.columns = result_percentage.columns.map(lambda x: map_values_UI.get(x, x))
    
    order_column = ["Nenhuma", 
                    "Menos de 1 ano", 
                    "1-3 anos", "4-7 anos", 
                    "8-15 anos", 
                    "Mais de 15 anos"] # ordenar as colunas

    df_order_columns = result_percentage.reindex(columns=order_column).round(2) # a funcao 'reindex' re-indexa/substitui as colunas nessa ordem

    df_order_columns.index.name = None # remove a referencia à coluna original que referencia o index do DataFrame ao fazer o crosstab ("Questão1")
    df_order_columns.columns.name = None # remove a referencia à coluna original que referencia a coluna do DataFrame ao fazer o crosstab ("Questão2")

    return df_order_columns