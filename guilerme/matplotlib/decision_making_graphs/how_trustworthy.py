import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../../csv_files/mockup_respostas.csv')

total_answers = (df['ia_confiavel']).count()
question = "Numa escala de 0 a 10, o quão confiável você considera os sistemas de IA para uso no auxílio de interpretação de imagens?"
categories = [n for n in range(0,11)]
values = [(float((df[df['ia_confiavel'] == n]).nunique()['data_hora']/total_answers))*100 for n in categories]

fig, ax = plt.subplots()
rects = ax.bar(categories, values, color='1', edgecolor='0', width=0.5, linewidth=1.5)

x = range(0, 11)
y = values

ax.bar_label(rects, padding=3, fmt='%.1f')

ax.errorbar(x, y, yerr=2, fmt='o', color='0')

ax.set_xticks(range(len(categories)))
ax.set_ylabel('%')
ax.set_title(question)

plt.show()
