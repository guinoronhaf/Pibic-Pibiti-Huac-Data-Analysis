import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import pandas as pd
from demographic_table import group_percentage_years_specialist, group_speciality_quantity

def graph_bars_experiense(df):
    df_experiense = group_percentage_years_specialist(df)

    df_traspost = df_experiense.T

    # o pandas aloca o index (linhas) para serem o eixo X do gráfico
    # ele separa as colunas e cria uma série de dados
    # funcionamneto interno:
    # Chamada Interna: O Pandas chama internamente o comando matplotlib.pyplot.gca() (get current axes). Se não houver um gráfico criado, ele cria um.
    # Entrega dos dados: O Pandas converte seus dados (que estão em formato de tabela) em listas de números (arrays) que o Matplotlib entende.
    df_traspost.plot(kind='bar', figsize=(12, 6), 
                          color=['#1f77b4', '#ff7f0e', '#2ca02c'], width=0.8)
    # "aloca para o espaço na memória em que o modulo de pyplot do matplotlib mostra o grafico" 
    
    # 3. Personalização
    plt.title("Quantidade de Respostas por Tempo de Experiência Por Cargo", fontsize=10)
    plt.xlabel("Tempo de Experiência", fontsize=8)
    plt.ylabel("Quantidade de Respostas", fontsize=8)
    
    # Melhora a legenda
    plt.legend(title="Cargos", bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Rotaciona os anos no eixo X para ficarem retos ou levemente inclinados
    plt.xticks(rotation=0) 
    
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    plt.savefig("graphs/gráfico_experiência_cargo.png")

def graph_occurrence_area_percentage(df):
    df_speciality = group_speciality_quantity(df)

    df_speciality["Percentage"].plot(kind="pie", 
                        autopct='%1.1f%%', # Mostra a porcentagem dentro da fatia
                        startangle=90,     # Gira o gráfico para começar no topo
                        figsize=(8, 8),
                        ylabel='')
    
    plt.title("Proporção de Cargos", fotsize=10)

    # Adiciona uma legenda lateral para ficar mais organizado
    plt.legend(df_speciality.index, title="Cargos", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.tight_layout()

    plt.savefig("graphs/gráfico_porcentagem_cargo.png")

if __name__ == "__main__":
    df = pd.read_csv("questionary_sheet.csv")
    
    # graph_bars_experiense(df)

    graph_occurrence_area_percentage(df)