import pandas as pd 

series = pd.Series(["Brasil", "França", "Austrália"], index=["América do Sul", "Europa", "Oceania"] )

print(series)
print(series.index)
print(series.index[1])

print('')

dicionario = {"Empresa": ["Weg", "Petrobras", "Vale"], "Cotação": [20.54, 20, 40]}

dataframe = pd.DataFrame(dicionario)
print(dataframe)

print('')
dataframe = dataframe.set_index("Empresa")

print(dataframe)

print('')
dataframe = dataframe.reset_index()
print(dataframe)

print('')
dataframe.index = ['a','b','c']
print(dataframe)


print('')


quatro_dias = pd.date_range("1/4/2000", periods=4)
print(quatro_dias)

fim_de_mes = pd.date_range(start = "1/4/2000", end = "31/12/2000", freq = "ME")

print(fim_de_mes)

print('')



fim_mes_weg = pd.date_range(start="1/1/2000", end="30/4/2000", freq="ME")

# print(fim_mes_weg)

dicionario = {"cotacao": [20.54, 20, 21, 22]}

cotacao_weg = pd.DataFrame(dicionario, index = fim_mes_weg)

print(cotacao_weg)