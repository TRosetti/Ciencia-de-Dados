import pandas as pd

dicionario = {
    'nomes' : ["Weg", "Itau", "Petrobras", "Vale", "Ambev"],
    "tickers": ["WEGE3", "ITUB4", "PETR4", "VALE3", "ABEV3"],
    "cotacoes": [25.30, 28.50, 22.10, 98.70, 15.20],
    "preco_sobre_lucro": [15.2, 12.5, 8.3, 10.1, 18.4],
    "volume" :  [1500000, 2500000, 3000000, 1200000, 1800000]
}

df_info_empresas = pd.DataFrame(dicionario)
print(df_info_empresas)