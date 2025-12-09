import pandas as pd 
import numpy as np

# Argumentos: listas/vetores

serie_inicial = pd.Series(np.random.randn(5))

print(serie_inicial)

serie_inicial = pd.Series(np.random.randn(5), index={'A', 'B', 'C', 'D', 'E'})
serie_lista = pd.Series(["Python", "SQL", "VBA"])

print(serie_inicial)
print(serie_lista)

print('--- ' * 10)

# Argumentos: dicionários

dicionario_cotacao = {'WEG3': 20.20, 'PETR4': 28.50, 'VALE3': 98.30, 'ITUB4': 30.10}

serie_cotacao = pd.Series(dicionario_cotacao)   
print(serie_cotacao)

print(serie_cotacao['PETR4'])
print(serie_cotacao.iloc[2])  # Acessa pelo índice posicional


# DataFrame

dicionario_dados = {
    "empresa": pd.Series(["WEG", "PETROBRAS", "VALE", "ITAU"], index = ["2019", "2020", "2021", "2022"]),
    "price": pd.Series([20.20, 28.50, 98.30, 30.10], index = ["2019", "2020", "2021", "2022"]),
    "volume": pd.Series([1000, 1500, 2000, 2500], index = ["2019", "2020", "2021", "2022"]) 
}

dados_diario = pd.DataFrame(dicionario_dados)
print(dados_diario)

## caso 2
dicionario_dados = {
    "empresa": ["WEG", "PETROBRAS", "VALE", "ITAU"],
    "price": [20.20, 28.50, 98.30, 30.10],
    "volume": [1000, 1500, 2000, 2500]
}

dados_diario = pd.DataFrame(dicionario_dados, index=["2019", "2020", "2021", "2022"])
print(dados_diario)

## caso 3
dicionario_dados = {
    "empresa": ["WEG", "PETROBRAS", "VALE", "ITAU"],
    "price": [20.20, 28.50, 98.30, 30.10],
    "volume": [1000, 1500, 2000, 2500]
}

dados_diario = pd.DataFrame(dicionario_dados, index=["2019", "2020", "2021", "2022"], columns=["volume", "price", "empresa"])
print(dados_diario)