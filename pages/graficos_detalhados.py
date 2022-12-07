import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from dataset import loadData

# segunda página com gráficos mais detalhados
st.set_page_config(page_title='Gráficos mais detalhados')

dados = loadData()

st.write('## Gráfico mais detalhado')

with st.expander('Quantos fumantes e não fumantes por gênero tem em cada região?'):
    g = sns.FacetGrid(data=dados, col='sex',row='region',height=5,sharex=False, sharey=False)
    g.map_dataframe(sns.countplot, x='smoker')
    g.set_titles(fontsize=14)
    g.set_xticklabels(fontsize=14, color='black')
    g.set_titles(size=14)
    st.pyplot(g)

with st.expander('Quantos filhos ambos os sexos fumante ou não fumante tem por região?'):
    g = sns.FacetGrid(data=dados, col='sex',row='region',height=5,sharex=False, sharey=False)
    g.map_dataframe(sns.countplot, x='children', hue='smoker', palette='icefire')
    g.set_titles(fontsize=14)
    g.set_xticklabels(fontsize=14, color='black')
    g.set_titles(size=14)
    g.add_legend()
    st.pyplot(g)

with st.expander('BMI por gênero: o custos médicos aumenta sobre fumantes e não fumantes?'):
    g = sns.FacetGrid(data=dados, col='smoker', row='sex',height=5,sharex=False, sharey=False)
    g.map_dataframe(sns.regplot, x='bmi', y='charges',ci=None)
    g.set_titles(fontsize=14)
    g.set_xticklabels(fontsize=13, color='black')
    g.set_yticklabels(fontsize=13, color='black')
    g.set_titles(size=14)
    g.add_legend()
    plt.tight_layout()
    st.pyplot(g)

with st.expander('Nível de BMI por gênero: custos médicos pela idade do fumante ou não fumante'):
    g = sns.FacetGrid(data=dados, row='level_bmi',col='sex', height=6, sharex=False, sharey=False)
    g.map_dataframe(sns.scatterplot, x='age',y='charges',hue='smoker')
    g.add_legend(bbox_to_anchor=(1.05,1), fontsize=16)
    g.set_titles(size=16)
    plt.tight_layout()
    st.pyplot(g)

with st.expander('Qual região separado por fumantes e não fumantes, medido pela BMI, apresentou aumento nos custos médicos?'):
    g = sns.FacetGrid(data=dados, col='smoker', row='region',height=5,sharex=False, sharey=False)
    g.map_dataframe(sns.regplot, x='bmi', y='charges',ci=None)
    g.set_titles(fontsize=14)
    g.set_xticklabels(fontsize=13, color='black')
    g.set_titles(size=14)
    g.add_legend()
    st.pyplot(g)

with st.expander('Regiões que apresenta aumento no custos médicos pelo BMI?'):
    g = sns.FacetGrid(data=dados, col='region', col_wrap=2,height=5,sharex=False, sharey=False)
    g.map_dataframe(sns.scatterplot, x='bmi', y='charges', hue='sex',palette='icefire')
    g.set_titles(fontsize=14)
    g.set_xticklabels(fontsize=13, color='black')
    g.set_titles(size=14)
    g.add_legend()
    st.pyplot(g)


with st.expander('Qual região pela idade do gênero fumante e não fumante teve aumento nos custos médicos?'):
    g = sns.FacetGrid(data=dados, col='sex',row='region',height=5,sharex=False, sharey=False)
    g.map_dataframe(sns.scatterplot, x='age', y='charges', hue='smoker',palette='icefire')
    g.set_titles(fontsize=14)
    g.set_xticklabels(fontsize=12, color='black')
    g.set_yticklabels(fontsize=12, color='black')
    g.set_titles(size=14)
    g.add_legend()
    plt.tight_layout()
    st.pyplot(g)

