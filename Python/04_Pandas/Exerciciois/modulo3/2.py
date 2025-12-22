# Crie um DataFrame que as colunas tenham informações ficticias de cotações, volumes e data de cada dado. Utilize pd.date_range para criar a coluna de datas, use set_index

import pandas as pd


dicionario = {
    "cotacao" : [150.20, 155.40, 152.00, 158.30],
    "volume": [1000, 1200, 1100, 1300],
    "data": pd.date_range("01/01/2025", periods=4)
}

dataframe = pd.DataFrame(dicionario)

print(dataframe)

dataframe = dataframe.set_index("data")

print(dataframe)