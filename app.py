# pip install streamlit pandas matplotlib seaborn
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title='Análise  das Ocorencias na cidade do rio de Janeiro ', layout='wide')

df = pd.read_csv('BO_2013_1.csv')

# Metricas 
df_final=df[['NOME_DEPARTAMENTO','ANO','MES','RUBRICA','CONDUTA','SEXO_PESSOA','COR','DESCR_GRAU_INSTRUCAO']]
df_final=df_final.dropna()
df_final=df_final.drop_duplicates()
df_final=df_final.reset_index(drop=True)

# Criando os filtros
st.sidebar.title('Filtros')
st.sidebar.markdown('Escolha os filtros para visualizar os gráficos.')

# Criando os filtros
ano = st.sidebar.multiselect(
    "Selecione o ano:",
    options=df_final['ANO'].unique(),
    default=df_final['ANO'].unique()
)

mes = st.sidebar.multiselect(
    "Selecione o mês:",
    options=df_final['MES'].unique(),
    default=[]
)
rubrica = st.sidebar.multiselect(
    "Selecione a rubrica:",
     options=df_final['RUBRICA'].unique(),
     default=[]
)

conduta = st.sidebar.multiselect(
    "Selecione a conduta:",
    options=df_final['CONDUTA'].unique(),
    default=[]  
)

sexo = st.sidebar.multiselect(
    "Selecione o sexo:",
    options=df_final['SEXO_PESSOA'].unique(),
    default=[]
)
cor = st.sidebar.multiselect(
    "Selecione a cor:",
    options=df_final['COR'].unique(),
    default=[]
)

grau = st.sidebar.multiselect(
    "Selecione o grau de instrução:",
    options=df_final['DESCR_GRAU_INSTRUCAO'].unique(),
    default=[]
)

departamento = st.sidebar.multiselect(
    "Selecione o departamento:",
    options=df_final['NOME_DEPARTAMENTO'].unique(),
    default=[]
)


query_expression = "ANO == @ano"

# df_selection = df_final.query(
#     "ANO == @ano & MES == @mes & RUBRICA == @rubrica & CONDUTA == @conduta & SEXO_PESSOA == @sexo & COR == @cor & DESCR_GRAU_INSTRUCAO == @grau & NOME_DEPARTAMENTO == @departamento"
# )

# if not departamento:
#     df_selection = df_final.query(
#         "ANO == @ano & MES == @mes & RUBRICA == @rubrica & CONDUTA == @conduta & SEXO_PESSOA == @sexo & COR == @cor & DESCR_GRAU_INSTRUCAO == @grau"
#     )
    
# if not grau:
#     df_selection = df_final.query(
#         "ANO == @ano & MES == @mes & RUBRICA == @rubrica & CONDUTA == @conduta & SEXO_PESSOA == @sexo & COR == @cor & NOME_DEPARTAMENTO == @departamento"
#     )

# if (not grau) and (not departamento):
#     df_selection = df_final.query(
#         "ANO == @ano & MES == @mes & RUBRICA == @rubrica & CONDUTA == @conduta & SEXO_PESSOA == @sexo & COR == @cor"
#     )

if mes:
    query_expression += f" & MES == @mes"
if rubrica:
    query_expression += f" & RUBRICA == @rubrica"
if conduta:
    query_expression += f" & CONDUTA == @conduta"
if sexo:
    query_expression += f" & SEXO_PESSOA == @sexo"
if cor:
    query_expression += f" & COR == @cor"
if grau:
    query_expression += f" & DESCR_GRAU_INSTRUCAO == @grau"
if departamento:
    query_expression += f" & NOME_DEPARTAMENTO == @departamento"

df_selection = df_final.query(query_expression)


# Abas 

# ABA 01 - Graficos 

st.dataframe(df_selection)
fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(x='RUBRICA', data=df_selection)
plt.xticks(rotation=90)
st.pyplot(fig)


#ABA 02 - MEDIA



#ABA 03 - Descrição  







# criar grafico de barras
st.header('Gráfico de barras empilhadas')


# criar grafico de barras empilhadas
fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(x='MES', hue='RUBRICA', data=df_final)
st.pyplot(fig)

# criar grafico de barras
st.header('Gráfico de barras horizontais')


# criar grafico de barras horizontais
fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(y='RUBRICA', data=df_final)
plt.xticks(rotation=90)
st.pyplot(fig)


