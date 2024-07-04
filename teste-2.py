# -*- coding: utf-8 -*-
"""conexão.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q11gDGa6XKVbL3mJI4mN7R9rJ75yjre4
"""

pip install streamlit

import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

try:
    conn = psycopg2.connect(
      dbname="Data_IESB",
      user="Data_IESB",
      password="DATA_IESB",
      host="dataiesb.iesbtech.com.br",
      port="5432"
    )
    print("Conexão bem-sucedida!")
except psycopg2.Error as e:
    print("Erro ao conectar ao PostgreSQL:", e)

cur = conn.cursor()



populacao = pd.read_sql_query("SELECT * FROM populacao", conn)
municipio = pd.read_sql_query("SELECT * FROM municipio", conn)
unidade_federacao = pd.read_sql_query("SELECT * FROM unidade_federacao", conn)
regiao = pd.read_sql_query("SELECT * FROM regiao", conn)

conn.close()

df = populacao.merge(municipio, on='codigo_municipio_dv')
df = df.merge(unidade_federacao, on='cd_uf')
df = df.merge(regiao, on='cd_regiao')

populacao_por_regiao = df.groupby('nome_regiao')['numero_habitantes'].sum().reset_index()

fig_regiao = px.bar(populacao_por_regiao,
                    x='nome_regiao',
                    y='numero_habitantes',
                    labels={'nome_regiao': 'Nome da Região', 'numero_habitantes': 'Número de Habitantes'},
                    title='População por Região')
fig_regiao.show()

