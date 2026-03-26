from email.policy import strict
from re import split
import string
import pandas as pd
from scipy.stats import spearmanr, kendalltau, kruskal

# campo identificador da base de dados de repostas
ID_FIELD = "data_hora"

def modularizating_data(df: pd.DataFrame, fields: tuple):
    global ID_FIELD

    # Evitar Warning de Pandas
    strict_df = df[list(fields)].copy() 
    # Excluir valores NaN
    strict_df = strict_df.dropna() 

    mapping = dict()

    # Ordenando dados (alfabeticamente) no set para evitar inconsistências no mapeamento
    possible_answers = sorted(set(strict_df[fields[0]]))

    idx = 0

    for ans in possible_answers:
        mapping[ans] = idx
        idx += 1

    strict_df[fields[0]] = strict_df[fields[0]].map(mapping)
    strict_df[fields[1]] = strict_df[fields[1]].map(mapping)

    strict_df = strict_df.dropna()
    
    # Restaura a ordem dos índices
    strict_df = strict_df.reset_index(drop=True)

    return strict_df

def filter_by_sector_avaliation(df: pd.DataFrame, sector_name, avaliation_columnn):
    sector_df = df[df["area_atuacao"] == sector_name]

    return list(sector_df[avaliation_columnn])

def calculate_kruskal_av_ai_app(df: pd.DataFrame) -> tuple[float, float]:
    av_app_ai_physics = map(lambda x: int(x.split(" - ")[0]), filter_by_sector_avaliation(df, "Médico Especialista", "av_aplicacao_ia"))
    av_app_ai_physics = list(av_app_ai_physics)
    
    av_app_ai_resident = map(lambda x: int(x.split(" - ")[0]), filter_by_sector_avaliation(df, "Médico Residente", "av_aplicacao_ia"))
    av_app_ai_resident = list(av_app_ai_resident)

    av_app_ai_tecnics = map(lambda x: int(x.split(" - ")[0]), filter_by_sector_avaliation(df, "Técnico em Radiologia", "av_aplicacao_ia"))
    av_app_ai_tecnics = list(av_app_ai_tecnics)

    mn, p = kruskal(av_app_ai_physics, av_app_ai_resident, av_app_ai_tecnics)

    return (float(mn), float(p))



def calculate_spearmanr(df: pd.DataFrame, fields: tuple) -> tuple[float, float]:
    """
    Calcula o coeficiente de correlação de Spearman em relação a duas colunas específícas.  

    Nesta função, é realizado um mapeamento das possíveis repostas para valores numéricos, o que permite o cálculo efetivo do coeficiente.
    Além disso, são excluídos valores nulos, o que facilita o cálculo estatístico.

    Parâmetros:
        df (pd.DataFrame): DataFrame original, contendo os dados e o identificador geral.
        fields (tuple): Tupla contendo as duas colunas a serem analisadas.
    Retorno:
        tuple[float, float]: Tupla contendo o coeficiente de correlação e o valor de "p" (rho, p).
    """
    strict_df = modularizating_data(df, fields)
    sp, p = spearmanr(strict_df[fields[0]], strict_df[fields[1]])

    return (float(sp), float(p))


def calculate_kendallt(df: pd.DataFrame, fields: tuple) -> tuple[float, float]:
    """
    Calcula o coeficiente de correlação de Kendall em relação a duas colunas específícas.  

    Nesta função, é realizado um mapeamento das possíveis repostas para valores numéricos, o que permite o cálculo efetivo do coeficiente.
    Além disso, são excluídos valores nulos, o que facilita o cálculo estatístico.

    Parâmetros:
        df (pd.DataFrame): DataFrame original, contendo os dados e o identificador geral.
        fields (tuple): Tupla contendo as duas colunas a serem analisadas.
    Retorno:
        tuple[float, float]: Tupla contendo o coeficiente de correlação e o valor de "p" (tau, p).
    """
    strict_df = modularizating_data(df, fields)
    kt, p = kendalltau(strict_df[fields[0]], strict_df[fields[1]])

    return (float(kt), float(p))

if __name__ == "__main__":
    CSV_PATH = "data/csv_files/respostas.csv"
    
    df = pd.read_csv(CSV_PATH)
    ks_stats = calculate_kruskal_av_ai_app(df)

    print(f"ks: {ks_stats[0]:.4f}, p: {ks_stats[1]:.15f}")
