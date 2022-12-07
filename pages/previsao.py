import pickle
import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder

# terceira página com a previsão
st.set_page_config(page_title='Previsão')

st.title('Previsão do seguro de saúde')
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

st.text('Selecione as opções abaixo e veja o valor previsto na cobrança de seguro de saúde')
def tabela():
    col1, col2 = st.columns(2)
    with col1:
        sex = st.selectbox('Sexo:',('male','female'))
        region = st.selectbox('Região',('southwest', 'southeast', 'northwest', 'northeast'))
        age = st.slider('Idade', 18,64,39)  
    with col2:
        smoker = st.selectbox('Fumante', ('yes','no'))
        children = st.radio('Filhos', [0,1,2,3,4,5],horizontal=True)
        bmi = st.slider('BMI',15.96, 53.13, 30.66)

    features = pd.DataFrame({
        'sex':sex,
        'region':region,
        'children':children,
        'smoker':smoker,
        'age':age,
        'bmi':bmi
        },index=[0])
    return features

# chamando a função criada acima
data = tabela()

# carregando os dados
df = pd.read_csv('insurance_cleaned.csv')
df = df.drop(['charges'],axis=1)

# transformando os dados
df1 = pd.concat([data, df], axis=0) 

cat = df1.select_dtypes(include='O')

colunas = cat.columns
le = LabelEncoder()
encode = list(colunas)
df1[encode] = df1[encode].apply(lambda col: le.fit_transform(col))
df2 = df1[:1]

# treinando o modelo
model = pickle.load(open('grade_reg.pkl','rb'))

prediction = model.predict(df2)[0]

# adicionando colunas para a tabela e previsão
col3, col4 = st.columns([2,1])
with col3:
    st.markdown('### 📑 Tabela')
    st.table(data)

with col4:
    st.write('### Previsão de custos médicos')
    st.markdown('💰' + ' ' + '{:.2f}'.format(prediction))