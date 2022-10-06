from tokenize import blank_re
import plotly.express as px
import pandas as pd
tabela = pd.read_csv('telecom_users.csv')
# print(tabela)


# Passo 1: Importar bases de Dados da empresa
# Passo 2: Visualizar as bases de Dados
# - Entender quais são as informações
# - Descobrir as cagadas da Base de Dados
# axis = 0 -> Linha, axis=1 -> coluna
tabela = tabela.drop('Unnamed: 0', axis=1)
print(tabela)
# Passo 3: Tratamento de dados
# valores são reconhecidos da forma errada
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')
# valores vazios
# colunas vazias
# linhas completamente vazias
tabela = tabela.dropna(how='all', axis=1)
# linhas com pelo menos 1 valor vazio
tabela = tabela.dropna(how='any', axis=0)


print(tabela.info())
# Passo 4: Analise Inicial (Como estão os cancelamentos)
print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format))

# Passo 5: Análise Completa (Entender o motivo do cancelamento)
# Churn = Cancelamento
# Como cada coluna da nossa base de dados impacta no cancelamento

# plotLy
# Histograma
# para cada coluna da minha tabela criar gráfico for = loop
for coluna in tabela.columns:
    # criar o gráfico
    grafico = px.histogram(tabela, x=coluna, color='Churn', text_auto=True)
    # exibir o gráfico
    grafico.show()

# Conclusão:
    # Novos clientes são os quem mais cancelam.
    # Clientes Não casados cancelam mais do que casados
    # Clientes que usam fibra cancelam mais do que os outros serviços
