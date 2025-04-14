# Raspagem de Dados Data SUS Tabnet

📊 Análise de Internações por Município – Dados do DATASUS com Python
Este projeto realiza a análise exploratória de dados públicos do DATASUS, especificamente sobre internações hospitalares por município, utilizando Python e bibliotecas populares para ciência de dados.

📥 Fonte dos Dados
Os dados foram extraídos do TABNET - DATASUS, uma plataforma do SUS (Sistema Único de Saúde) que disponibiliza dados abertos sobre atendimentos hospitalares, ambulatoriais, nascimentos, mortalidade e mais.

link: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/


O arquivo data_sus.csv foi exportado diretamente da plataforma em formato .csv.

🛠️ Tecnologias Utilizadas

pandas
- Biblioteca essencial para manipulação de dados tabulares.

- Permite ler, limpar, filtrar, ordenar e analisar datasets de forma rápida e eficiente.

Neste projeto, foi usada para:

- Ler o arquivo .csv com parâmetros específicos (encoding, sep, skiprows, etc.)

- Ordenar os municípios com mais internações

matplotlib.pyplot
- Usada para criar visualizações gráficas.

- No projeto, foi utilizada para gerar um gráfico de barras mostrando o número total de internações por município.


📌 Funcionalidades

- Importação de dados públicos de saúde

- Tratamento de arquivos com encoding específico e linhas extras

- Visualização dos municípios com maior número de internações

- Gráfico personalizável para análises rápidas


📈 Exemplo de Gráfico Gerado

- Gráfico de barras com os 5 municípios com mais internações hospitalares no período selecionado.


🚀 Possibilidades Futuras

- Automatizar a raspagem de dados diretamente do site TABNET com selenium ou requests + BeautifulSoup

- Comparar internações por ano, faixa etária ou causa

- Cruzar dados com outras fontes como IBGE

- Exportar gráficos e relatórios automáticos em PDF