# Mude o nome da coluna do dataframe do exercício de "cotacoes" para "precos"
import pandas as pd


dicionario = pd.DataFrame({
    "cotacao" : [150.20, 155.40, 152.00, 158.30],
    "volume": [1000, 1200, 1100, 1300],
    "data": pd.date_range("01/01/2025", periods=4)
})

dicionario.columns = ['precos', 'volume', 'data']

print(dicionario)