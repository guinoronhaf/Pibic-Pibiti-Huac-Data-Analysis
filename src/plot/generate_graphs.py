import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from ..aux.auxiliar_functions import *

PATH = 'data/graphs/'
ID_FIELD = 'data_hora'

def generate_graph_1(df):
    df_speciality = group_speciality_quantity(df)

    df_speciality["Percentage"].plot(kind="pie",
                        autopct='%1.1f%%', # Mostra a porcentagem dentro da fatia
                        startangle=90,     # Gira o gráfico para começar no topo
                        figsize=(8, 8),
                        ylabel='')
    
    plt.title("Proporção de Cargos", fontsize=10)

    # Adiciona uma legenda lateral para ficar mais organizado
    plt.legend(df_speciality.index, title="Cargos", loc="upper left", bbox_to_anchor=(1.20, 1.20))

    plt.tight_layout()

    plt.savefig(PATH + "graph1.png", bbox_inches='tight')

    plt.clf()

def generate_graph_2(df):
    df_experiense = group_percentage_years_specialist(df)

    df_traspost = df_experiense.T

    # o pandas aloca o index (linhas) para serem o eixo X do gráfico
    # ele separa as colunas e cria uma série de dados
    # funcionamneto interno:
    # Chamada Interna: O Pandas chama internamente o comando matplotlib.pyplot.gca() (get current axes). Se não houver um gráfico criado, ele cria um.
    # Entrega dos dados: O Pandas converte seus dados (que estão em formato de tabela) em listas de números (arrays) que o Matplotlib entende.
    df_traspost.plot(kind='bar', figsize=(18, 9), 
                          color=['#1f77b4', "#c55f06", "#29cc29", "#6432ee"], 
                          width=0.5,
                          align='center')
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
    
    plt.savefig(PATH + "graph2.png")

    plt.clf()

def generate_graph_3(df: pd.DataFrame):
    title = "Impacto potencial do feedback de IA na tomada de decisão dos Radiologistas que produzem laudos"
    answer_categories = ("Não", "Sim", "Não tenho certeza")
    question_categories = {
            "Você se sentiria mais seguro(a) em relação a seu diagnóstico se um sistema de IA concordasse com sua interpretação?": "mais_seg",
            "Você se sentiria menos seguro(a) em relação a seu diagnóstico se um sistema de IA discordasse de sua interpretação?": "menos_seg",
            "Se uma IA discordasse de sua interpretação de imagens, isso faria você buscar uma segunda opinião em relação à sua decisão inicial?": "ia_descord"
    }
    total_answers = 40
    answer_values = {quest_k: [float((df[df[question_categories[quest_k]] == cat]).nunique()[ID_FIELD]/total_answers)*100 for cat in answer_categories] for quest_k in question_categories.keys()}
   
    x = np.arange(len(answer_categories))
    width = 0.25
    multiplier = 0
    spacing = 0.01

    fig, ax = plt.subplots(layout='constrained', figsize=(12, 8))
    
    total_width = (len(answer_categories) - 1) * width
    adjustment = total_width/2

    for ques, val in answer_values.items():
        offset = (width + spacing) * multiplier
        rects = ax.bar(x + offset, val, width, label=ques)
        ax.bar_label(rects, padding=3, fmt='%1.1f')
        multiplier += 1

    ax.set_ylabel('%')
    ax.set_title(title)
    ax.set_xticks(x + adjustment, answer_categories)
    ax.legend(loc='upper right', ncols=1)
    ax.set_ylim(0, 80)

    plt.savefig(PATH + "graph3.png")

    plt.clf()

def generate_graph_4(df: pd.DataFrame):
    title = "Em uma escala de 0 a 10, o quão confiável você considera so sistemas de IA para uso no auxílio de interpretação de imagens? (0 = sem confiança, 10 = confiança absoluta)"

    total_answers = (df['ia_confiavel']).count()

    categories = range(0, 11)

    values_to_plot = [float((df[df['ia_confiavel'] == cat]).nunique()[ID_FIELD]/total_answers)*100 for cat in categories]

    fig, ax = plt.subplots(figsize=(18, 8))
    rects = ax.bar(categories, values_to_plot, color='w', edgecolor='k', width=0.5, linewidth=1.5)

    ax.bar_label(rects, padding=3, fmt='%1.f')

    ax.set_xticks(range(len(categories)))
    ax.set_ylabel('%')
    ax.set_title(title, pad=20)
    ax.set_ylim(0, max(values_to_plot) + 5)

    plt.savefig(PATH + "graph4.png")

    plt.clf()

def generate_graph_5(df: pd.DataFrame):
    target_field = 'funcionalidades'
    title = "Quais funcionaliades serviriam para aumentar sua confiança em um sistema de IA para diagnóstico por imagem?"

    ans_poss = ("A performance/acurácia do sistema", "Uma explicação visual", "Uma indicação da confiança", "Uma explicação textual", "Uma recomendação para mais imagens/modalidades")
    ans_poss_labels = ("A performance/acurácia\ndo sistema", "Uma explicação visual", "Uma indicação da\n confiança", "Uma explicação textual", "Uma recomendação para \nmais imagens/modalidades")

    ans_values = [int(df[target_field].str.contains(ap).sum()) for ap in ans_poss]

    fig, ax = plt.subplots(figsize=(18, 8))

    ax.barh(ans_poss_labels, ans_values, height=0.5)

    ax.set_xticks(range(0, max(ans_values) + 5, 10))
    ax.set_yticks(range(len(ans_poss_labels)))

    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)

    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    ax.set_yticklabels(ans_poss_labels, ma='center')

    for s in ('left', 'right'):
        ax.spines[s].set_visible(False)

    ax.invert_yaxis()

    ax.set_xlabel('Counts')

    ax.grid(visible=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.2)

    for i in ax.patches:
        plt.text(i.get_width()+0.1, i.get_y()+0.3, str(round((i.get_width()), 2)), fontsize=10, color='black', ma='center')

    ax.set_title(title, pad=10)

    plt.savefig(PATH + "graph5.png")

    plt.clf()

def generate_graph_6(df: pd.DataFrame):
    df_to_plot = get_data_frame_app_rate(df)

    fig, ax = plt.subplots(figsize=(12, 8))

    dict_times_by_rate = map_times_by_rate(df_to_plot)

    rates = list(dict_times_by_rate)
    times_chosen = [dict_times_by_rate[i] for i in rates]

    bar_label = 'Times Chosen'
    bar_color = 'tab:blue'

    ax.bar(rates, times_chosen, label=bar_label, color=bar_color)

    ax.set_xticks(range(len(rates))) # isso permite que todos os valores (eixo-x) de rate apareçam, sem perder os dados
    ax.set_xticklabels(rates)
    ax.set_ylabel('Times Chosen')
    ax.set_xlabel('Rates')
    ax.set_ylim(0, max(times_chosen) + 5)
    ax.set_title('How do you rate the application of artificial intelligence in radiological diagnosis?', fontweight='bold')
    ax.legend(title="Color Mean")

    
    total_votes = sum(times_chosen)
    # O 'r' antes das aspas é fundamental para o LaTeX funcionar -> gemini salvou
    labels = [fr"$\mathbf{{{times}}}$ ({((times / total_votes) * 100):.2f}%)" for times in times_chosen]

    rects = ax.patches
    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2, 
            height + 0.05, 
            label, 
            ha="center", 
            va="bottom"
        )

    plt.savefig(PATH + "graph6.png")

    plt.clf()
