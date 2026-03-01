import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Graph 1: "Potential impact of AI feedback on reporting radiographers' decision making"
# Graph 2: "On a scale 0-10, how trustworhty do you consider AI systems for use in image interpretation decision support (0 = no trust, 10 = absolute trust)"
# Graph 3: "Which features might serve to enhance your trust in an AI system for diagnostic image interpretation?" 

OUTPUT_PATH = "../data/graphs/"
ID_FIELD = "data_hora"

def generate_graph1(df: pd.DataFrame):
    title = "Impacto potencial do feedback de IA na tomada de decisão dos Radiologistas que produzem laudos"
    answer_categories = ("Não", "Sim", "Não tenho certeza")
    question_categories = {
            "Você se sentiria mais seguro(a) em relação a seu diagnóstico se um sistema de IA concordasse com sua interpretação": "mais_seg",
            "Você se sentiria menos seguro(a) em relação a seu diagnóstico se um sistema de IA discordasse de sua interpretação?": "menos_seg",
            "Se uma IA discordasse de sua interpretação de imagens, isso faria você buscar uma segunda opinião em relação à sua decisão inicial?": "ia_descord"
    }
    total_answers = df.nunique()[ID_FIELD]
    answer_values = {quest_k: [float((df[df[question_categories[quest_k]] == cat]).nunique()[ID_FIELD]/total_answers)*100 for cat in answer_categories] for quest_k in question_categories.keys()}

    x = np.arange(len(answer_categories))
    rect_width = 0.25
    rect_spacing = 0.01
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained', figsize=(16, 8))

    total_width = (len(answer_categories) - 1) * rect_width
    adjustment = total_width/2

    for ques, val in answer_values.items():
        offset = (rect_width + rect_spacing) * multiplier
        rects = ax.bar(x + offset, val, rect_width, label=ques)
        ax.bar_label(rects, padding=3, fmt='%1.1f')
        multiplier += 1

    ax.set_ylabel('%')
    ax.set_title(title)
    ax.set_xticks(x + adjustment, answer_categories)
    ax.legend(loc='upper right', ncols=1)
    ax.set_ylim(0, max([max(v) for v in answer_values.values()]) + 20)

    plt.savefig(OUTPUT_PATH + "graph_1.png")

    plt.clf()


def generate_graph2(df: pd.DataFrame):
    DF_TARGET_FIELD = "ia_confiavel"

    title = "Em uma escala de 0 a 10, o quão confiável você considera os sistemas de IA para uso no auxílio de interpretação de imagens? (0 = sem confiança, 10 = confiança absoluta)"
    total_answers = df.nunique()[ID_FIELD]

    categories = range(0, 11)

    values_to_plot = [float((df[df[DF_TARGET_FIELD] == cat]).nunique()[ID_FIELD]/total_answers)*100 for cat in categories]

    fig, ax = plt.subplots(figsize=(18, 8))
    rects = ax.bar(categories, values_to_plot, color='w', edgecolor='k', width=0.5, linewidth=1.5)

    ax.bar_label(rects, padding=3, fmt='%1.f')

    ax.set_xticks(range(len(categories)))
    ax.set_ylabel('%')
    ax.set_title(title, pad=20)
    ax.set_ylim(0, max(values_to_plot) + 5)

    plt.savefig(OUTPUT_PATH + "graph_2.png")

    plt.clf()

# corrigir o limite do eixo x aqui!!
def generate_graph3(df: pd.DataFrame):
    DF_TARGET_FIELD = "funcionalidades"

    title = "Quais funcionalidades serviriam para aumentar sua confiança em um sistema de IA para diagnóstico por imagem?"

    ans_possibilities = ("A performance/acurácia do sistema", "Uma explicação visual", "Uma indicação da confiança", "Uma explicação textual", "Uma recomendação para mais imagens/modalidades")
    ans_possibilities_labels = ("A performance/acurácia\ndo sistema", "Uma explicação visual", "Uma indicação da\n confiança do sistema\nem seus diagnósticos", "Uma explicação textual", "Uma recomendação para \nmais imagens/modalidades")

    ans_values = [int(df[DF_TARGET_FIELD].str.contains(ap).sum()) for ap in ans_possibilities]

    fig, ax = plt.subplots(figsize=(18,8))

    ax.barh(ans_possibilities_labels, ans_values, height=0.5)

    ax.set_xticks(range(0, max(ans_values) + 5, 5))
    ax.set_yticks(range(len(ans_possibilities_labels)))

    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    ax.set_yticklabels(ans_possibilities_labels, ma='center')

    for s in ('left', 'right'):
        ax.spines[s].set_visible(False)

    ax.invert_yaxis()

    ax.set_xlabel('Counts')

    ax.grid(visible=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.2)

    for i in ax.patches:
        plt.text(i.get_width()+0.1, i.get_y()+0.3, str(round((i.get_width()), 2)), fontsize=10, color='black', ma='center')

    ax.set_title(title, pad=10)

    plt.savefig(OUTPUT_PATH + "graph_3.png")

    plt.clf()
