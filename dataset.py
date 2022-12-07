import pandas as pd

# filtrando os dados originais 
## identificando as coluna pelos valores das condições
def loadData():
    dados = pd.read_csv('insurance_cleaned.csv')
    # coluna IMC
    lista = [dados]
    for col in lista:
        col.loc[(col['bmi'] <=16), 'level_bmi'] = 'magreza_grave'

        col.loc[(col['bmi'] >17) & (col['bmi']<=19), 'level_bmi'] = 'magreza_moderada'

        col.loc[(col['bmi'] >20) & (col['bmi'] <=24), 'level_bmi'] = 'saudável'

        col.loc[(col['bmi'] >25) & (col['bmi'] <=29), 'level_bmi'] = 'sobrepeso'

        col.loc[(col['bmi'] >30) & (col['bmi'] <=34), 'level_bmi'] = 'obesidade_grau_I'

        col.loc[(col['bmi'] >35) & (col['bmi'] <=39), 'level_bmi'] = 'obesidade_severa'

        col.loc[(col['bmi'] >40),'level_bmi'] = 'obesidade_morbida'
    
    # coluna faixa etária
    for col in lista:
        col.loc[(col['age'] <=19), 'level_age'] = 'jovem'
        col.loc[(col['age'] >20) & (col['age'] <59), 'level_age'] = 'adulto'
        col.loc[(col['age'] > 60), 'level_age'] = 'idoso'
    return dados