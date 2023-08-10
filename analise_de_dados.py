# Analise de dados

""" 
bibliotecas: pandas
"""

import pandas as pd
import plotly_express as px

""" Carregandos os dados """

dados = pd.read_excel("vendas.xlsx")

"""  Análise Exploratórias """
# ver as primeiras linhas dos dados
dados.read();

# ver as ultimas linhas
dados.tail()

# total de linhas e colunas
dados.shape;

#tipos dos dados
dados.dtypes;

""" Gerar estatisticas """

# Estastísticas
dados.describe();

# Análises
# quantidade de vendas por lojas

dados.loja.value_counts();

# quantidades de vendas
dados.tamanho.value_counts()

# dados por forma de pagamento
dados.forma_pagamento.value_counts()

""" Agrupamentos de dados """
#agrupar por lojas - Faturamento por lojas
dados.groupby("loja").preco.sum().to_frame()

#faturamento medio por lojas
dados.groupby("loja").preco.mean().to_frame()

#agrupamento por mais colunas;
# loja e forma de pagamento;
dados.groupby(["loja", "forma_pagamento"]).preco.sum().to_frame()

#estados

dados.groupby(["estado", "forma_pagamento"]).preco.sum().to_frame()

#cidade e forma de pagamento

dados.groupby(["cidade", "forma_pagamento"]).preco.sum().to_frame()
dados.groupby(["cidade", "forma_pagamento"]).preco.sum().to_excel("analise_forma_pagamentos.xlsx")

#criar gráficos

#visualização de dados

px.histogram(dados, x="loja")


grafico = px.histogram(dados, x="loja", y="preco", text_auto=True, color="forma_pagamento")
grafico.show()

#automatizar 
### Estrutura de repetição
#### estrutura de dados - Lista

colunas = ["loja", "cidade", "estado", "regiao", "local_consumo"]

#lopping

for coluna in colunas:
    print(coluna);
    
for coluna in colunas:
    grafico = px.histogram(dados, x="loja", y="preco", text_auto=True, color="forma_pagamento")
    grafico.show()






