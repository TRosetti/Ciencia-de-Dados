# Selecione as duas últimas colunas do dataframe estudado
import pandas as pd

dicionario = pd.DataFrame({
    "empresas": ["Apple", 'Vale', 'Petrobras', 'Weg'],
    "cotacao" : [150.20, 75.40, 32.00, 58.30],
    "volume": [1000, 1200, 1100, 1300],
    "data": pd.date_range("01/01/2025", periods=4)
})

dicionario.columns = ['empresas', 'precos', 'volume', 'data']


duas_ultimas_colunas = dicionario[['volume', 'data']]

print(duas_ultimas_colunas)