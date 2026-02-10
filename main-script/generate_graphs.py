import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

PATH = '../graphs/'

def generate_graph_3(df: pd.DataFrame):
    title = "Impacto potencial do feedback de IA na tomada de decisão dos Radiologistas que laudam"
    total_answers = 40
    question_categories = {
            "Você se sentiria mais seguro(a) em relação a seu diagnóstico se um sistema de IA concordasse com sua interpretação?": "mais_seg",
            "Você se sentiria menos seguro(a) em relação a seu diagnóstico se um sistema de IA discordasse de sua interpretação?": "menos_seg",
            "Se uma IA discordasse de sua interpretação de imagens, isso faria você buscar uma segunda opinião em relação à sua decisão inicial?": "ia_descord"
    }
    answer_categories = ("Não", "Sim", "Não tenho certeza")
    answer_values = {quest_k: [float((df[df[question_categories[quest_k]] == cat]).nunique()['data_hora']/total_answers)*100 for cat in answer_categories] for quest_k in question_categories.keys()}
   
    x = np.arange(len(answer_categories))
    width = 0.25
    multiplier = 0
    spacing = 0.01

    fig, ax = plt.subplots(layout='constrained')
    
    total_width = (len(answer_categories) - 1) * width
    adjustment = total_width/2

    for ques, val in answer_values.items():
        offset = (width + spacing) * multiplier
        rects = ax.bar(x + offset, val, width, label=ques)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    ax.set_ylabel('%')
    ax.set_title(title)
    ax.set_xticks(x + adjustment, answer_categories)
    ax.legend(loc='upper right', ncols=1)
    ax.set_ylim(0, 80)

    plt.show()

generate_graph_3(pd.read_csv('../csv_files/mockup/respostas_questionario.csv'))
