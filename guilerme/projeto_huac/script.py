import pandas as pd

df = pd.read_csv('./respostas.csv')
print(df[['data_hora', 'area_atuacao', 'experiencia', 'ia_desm', 'atencao']])
