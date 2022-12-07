import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from dataset import loadData

# introdução da página
st.set_page_config(page_title='Gráficos')
dados = loadData()

st.title('Gráfico de custos médicos')
st.markdown(''' Para acessar as outras páginas basta clicar sobre a **seta (>)** logo a esquerda da sua tela.
Para ampliar a imagem, basta colocar o mouse em cima da imagem e do lado esquerdo da tela
verá **duas setas em posições opostas**, clique e a imagem aumentará.
''')

st.markdown(''' ### Sobre os dados
Os dados mostrados abaixo é referente ao seguro de saúde dos beneficiários, apresento também a tabela do IMC para poder
identificar os níveis e a relação que existem com os gastos médicos, além disso, os dados trazem os atributos
dos envolvidos, como os dependentes, a região, a idade, o gênero e se os beneficiários são fumante ou não.''')
st.write('''
    IMC - Classificação do IMC

    - Menor que 16 - Magreza grave
    - 16 a menor que 17 - Magreza moderada
    - 17 a menor que 18,5 - Magreza leve
    - 18,5 a menor que 25 - Saudável
    - 25 a menor que 30 - Sobrepeso
    - 30 a menor que 35 - Obesidade Grau I
    - 35 a menor que 40 - Obesidade Grau II (considerada severa)
    - Maior que 40 - Obesidade Grau III (considerada mórbida)
    ---
''')
#* agrupamento dos dados para filtragem
fumantes = dados[['sex','age','charges',
'smoker','bmi']].groupby(['sex','age','charges','smoker','bmi']).count().reset_index()

#? ------- função ----------
def comfiltro(data=dados):
    tab1, tab2, tab3, tab4 = st.tabs(['gráfico 1','gráfico 2', 'gráfico 3', 'gráfico 4'])
    with tab1:
        fig1 = plt.figure(figsize=(14,7))
        sns.pointplot(x=data['age'], y=data['charges'], hue=data['sex'], ci=None, palette='Set2')
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=14)
        plt.xlabel('AGE', fontsize=16)
        plt.ylabel('CHARGES', fontsize=16)
        plt.legend(fontsize=12)
        st.pyplot(fig1)

    with tab2:
        fig2 = plt.figure(figsize=(14,7))
        sns.pointplot(x=data['age'], y=data['bmi'], hue=data['sex'], ci=None, palette='Set2')
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=14)
        plt.xlabel('AGE', fontsize=16)
        plt.ylabel('BMI', fontsize=16)
        plt.legend(fontsize=12)
        st.pyplot(fig2)

    with tab3:
        fig3, axes = plt.subplots(1,2,figsize=(16,7))
        sns.histplot(x=data['bmi'],ax=axes[0])
        axes[0].set_xlabel('BMI',fontsize=16)
        axes[0].tick_params(axis='x', labelsize=14)

        sns.histplot(x=data['bmi'], hue=data['sex'],ax=axes[1])
        axes[1].set_xlabel('BMI', fontsize=16)
        axes[1].tick_params(axis='x', labelsize=14)
        plt.legend(fontsize=12)
        st.pyplot(fig3)

    with tab4:
        fig4,axes = plt.subplots(1,2,figsize=(14,7))
        sns.barplot(x=data['sex'], y=data['charges'],palette='Set2',ax=axes[0])
        axes[0].set_xlabel('SEX',fontsize=16)
        axes[0].set_ylabel('CHARGES',fontsize=16)
        axes[0].tick_params(axis='x', labelsize=14)

        sns.boxplot(x=data['sex'], y=data['charges'], palette='Set2',ax=axes[1])
        axes[1].set_xlabel('SEX',fontsize=16)
        axes[1].set_ylabel('CHARGES',fontsize=16)
        axes[1].tick_params(axis='x', labelsize=14)
        st.pyplot(fig4)

st.text('Marque para ver gráfico com filtro e desmarque para ver o gráfico geral')
comfiltro1 = st.checkbox('Com filtro')
if comfiltro1:
    fumante = st.selectbox('Fumante',fumantes['smoker'].unique())
    smokings = fumantes[fumantes['smoker'] == fumante]
    st.write('#### Análise com dados filtrados') 
    comfiltro = comfiltro(smokings)
else:
    st.write('### Análise geral dos dados')
    semfiltro = comfiltro()
#? ----------- fim ----------------

st.write('---')

#? --------- gráfico ------------
#* agrupando dados para filtragem
genero = dados[['charges','smoker','age','bmi','sex']].groupby(['charges','smoker','age','bmi','sex']).count().reset_index()

st.write('### BMI vs Custo')
def bmi_charges(data=dados):
    tab1, tab2, tab3 = st.tabs(['gráfico1','gráfico2','gráfico3'])
    with tab1:
        fig5 = plt.figure(figsize=(14,7))
        sns.scatterplot(x='bmi', y='charges', hue='smoker', data=data, palette='Set2')
        plt.title('BMI vs Custo: Relação Fumantes',fontsize=18)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.xlabel('BMI', fontsize=16)
        plt.ylabel('CHARGES', fontsize=16)
        plt.legend(fontsize=12)
        st.pyplot(fig5)
    with tab2:
        fig6 = plt.figure(figsize=(14,7))
        sns.regplot(x='bmi', y='charges', data = data[data['smoker'] == 'yes'],ci=None)
        plt.title('Fumante: BMI vs Custo', fontsize=18)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.xlabel('BMI', fontsize=16)
        plt.ylabel('CHARGES', fontsize=16)
        plt.legend(fontsize=12)
        st.pyplot(fig6)
    with tab3:
        fig7 = plt.figure(figsize=(14,7))
        sns.regplot(x='bmi', y='charges', data = data[data['smoker'] == 'no'],ci=None)
        plt.title('Não Fumantes: BMI vs Custo', fontsize=18)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.xlabel('BMI', fontsize=16)
        plt.ylabel('CHARGES', fontsize=16)
        plt.legend(fontsize=12)
        st.pyplot(fig7)


st.text('Marque para ver gráfico com filtro e desmarque para ver o gráfico geral')
comfiltro2 = st.checkbox('Selecionar para ver gráfico com filtro?')
if comfiltro2:
    col1, col2 = st.columns(2)
    sexo = col1.selectbox('Gênero', genero['sex'].unique())
    idade = col2.slider('Idade',18,64,39)
    gen = genero[(genero['sex'] == sexo) & (genero['age'] == idade)]
    st.write('### Análise com dados filtrados')
    comfiltro3 = bmi_charges(gen)
else:
    st.write('### Análise geral dos dados')
    semfiltro1 = bmi_charges()

#? ---------- fim ---------------

st.write('---')

#? ------- tabela 2 ---------
st.write('### Região')
tab5, tab6, tab7, tab8 = st.tabs(['gráfico1','gráfico2','gráfico3','gráfico4'])
with tab5:
    fig6 = plt.figure(figsize=(16,8))
    sns.boxplot(x=dados['region'],y=dados['bmi'],palette='Set2')
    plt.title('BMI em cada região', fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('REGION', fontsize=16)
    plt.ylabel('BMI', fontsize=16)
    plt.legend(fontsize=12)
    st.pyplot(fig6)

with tab6:
    fig7,ax = plt.subplots(figsize=(16,8))
    sns.barplot(x=dados['region'], y=dados['charges'], palette='Set2',ci=None)
    plt.title('Custo médico em cada região', fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('REGION', fontsize=16)
    plt.ylabel('CHARGES', fontsize=16)
    plt.legend(fontsize=12)
    for n in ax.containers:
        ax.bar_label(n, label_type='center', fontsize=16, bbox=dict(facecolor='white', alpha=0.5))
    st.pyplot(fig7)

with tab7:
    fig8 = plt.figure(figsize=(16,8))
    sns.boxplot(x=dados['region'], y=dados['charges'], palette='Set2')
    plt.title('Média do custo médico em cada região', fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('REGION', fontsize=16)
    plt.ylabel('CHARGES', fontsize=16)
    plt.legend(fontsize=12)
    st.pyplot(fig8)

with tab8:
    fig9 = plt.figure(figsize=(16,8))
    sns.countplot(x=dados['region'], hue=dados['smoker'], palette='Set2')
    plt.title('Fumantes e não fumantes em cada região', fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('REGION', fontsize=16)
    plt.ylabel('SMOKER', fontsize=16)
    plt.legend(fontsize=12)
    st.pyplot(fig9)
#? --------- fim ------------

#? ---------- tabela 3 ------------
st.write('### Dependentes')
tab5,tab6,tab7,tab8,tab9,tab10 = st.tabs(['gráfico1','gráfico2','gráfico3','gráfico4','gráfico5','gráfico6'])

with tab5:
    fig10 = plt.figure(figsize=(16,8))
    sns.countplot(x=dados['children'], hue=dados['sex'], palette='Set2')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('CHILDREN', fontsize=16)
    plt.legend(fontsize=12)
    st.pyplot(fig10)

with tab6:
    fig11,ax1 = plt.subplots(figsize=(16,8))
    sns.barplot(x=dados['children'], y=dados['charges'],palette='Set2',ci=None)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('CHILDREN', fontsize=16)
    plt.ylabel('CHARGES', fontsize=16)
    plt.legend(fontsize=12)
    for n in ax1.containers:
        ax1.bar_label(n, label_type='center', fontsize=16, bbox=dict(facecolor='white', alpha=0.5))
    st.pyplot(fig11)

with tab7:
    fig12 = plt.figure(figsize=(16,8))
    sns.boxplot(x=dados['children'], y=dados['charges'], palette='Set2')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('CHILDREN', fontsize=16)
    plt.ylabel('CHARGES', fontsize=16)
    plt.legend(fontsize=12)
    st.pyplot(fig12)

with tab8:
    fig13,ax2 = plt.subplots(figsize=(16,8))
    sns.barplot(x=dados['children'], y=dados['charges'],hue=dados['sex'],palette='Set2',ci=None)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('CHLIDREN', fontsize=16)
    plt.ylabel('CHARGES', fontsize=16)
    plt.legend(fontsize=12)
    for n in ax2.containers:
        ax2.bar_label(n, label_type='center', fontsize=16, rotation=90,bbox=dict(facecolor='white', alpha=0.5))
    st.pyplot(fig13)

with tab9:
    fig14 = plt.figure(figsize=(16,8))
    sns.boxplot(x=dados['children'], y=dados['charges'], hue=dados['sex'],palette='Set2')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('CHILDREN', fontsize=16)
    plt.ylabel('CHARGES', fontsize=16)
    plt.legend(fontsize=12)
    st.pyplot(fig14)

with tab10:
    fig15 = plt.figure(figsize=(16,8))
    sns.boxplot(x=dados['children'], y=dados['charges'], hue=dados['region'],palette='Set2')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('CHILDREN', fontsize=16)
    plt.ylabel('CHARGES', fontsize=16)
    plt.legend(fontsize=12)
    st.pyplot(fig15)
#? --------- fim ------------

#* filtrando apenas pelo niel do IMC
dados = dados.dropna()

st.write('## Nível de BMI')
nivel = dados[['charges','bmi','sex','smoker',
'children','region','level_bmi']].groupby(['charges','bmi','smoker','sex',
'children','region','level_bmi']).count().reset_index()

level = st.radio('Selecione o Nível de IMC:', dados['level_bmi'].unique(),  horizontal=True)

level_bmi = nivel[nivel['level_bmi'] == level]

tab11, tab12, tab13 = st.tabs(['gráfico1','gráfico2','gráfico3'])
with tab11:
    fig5 = plt.figure(figsize=(14,7))
    sns.scatterplot(x='bmi', y='charges', hue='smoker', data=level_bmi, palette='Set2')
    plt.title('BMI vs Custo: Relação Fumantes',fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('BMI', fontsize=16)
    plt.ylabel('CHARGES', fontsize=16)
    plt.legend(fontsize=12)
    st.pyplot(fig5)

with tab12:
    fig13,ax2 = plt.subplots(figsize=(16,8))
    sns.barplot(x=level_bmi['children'], y=level_bmi['charges'],hue=level_bmi['sex'],palette='Set2',ci=None)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('CHLIDREN', fontsize=16)
    plt.ylabel('CHARGES', fontsize=16)
    plt.legend(fontsize=12)
    for n in ax2.containers:
        ax2.bar_label(n, label_type='center', fontsize=16, rotation=90,bbox=dict(facecolor='white', alpha=0.5))
    st.pyplot(fig13)
with tab13:
    fig8 = plt.figure(figsize=(16,8))
    sns.boxplot(x=level_bmi['region'], y=level_bmi['charges'], palette='Set2')
    plt.title('Média do custo médico em cada região', fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('REGION', fontsize=16)
    plt.ylabel('CHARGES', fontsize=16)
    plt.legend(fontsize=12)
    st.pyplot(fig8)