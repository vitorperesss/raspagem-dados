import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv(
    'data_sus.csv',
    encoding='ISO-8859-1',
    sep=';',
    skiprows=3,
    skipfooter=12,
    engine='python'

)

dados_ordenados = dados.sort_values(by=dados.columns[1], ascending=False).head()

plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.bar(dados_ordenados['Município'], dados_ordenados['Internações'])

plt.title('Total de Internações por Município')
plt.xlabel('Municípios')
plt.ylabel('Total de Internações')

plt.xticks(rotation=45)

plt.show()
