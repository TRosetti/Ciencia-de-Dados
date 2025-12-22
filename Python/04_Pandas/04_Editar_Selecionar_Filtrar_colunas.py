import pandas as pd 

df_cambio = pd.DataFrame({
    "moeda": ['dolar/real', 'libra/real'] * 2,
    "price": [5.24, 4.15, 5.26, 4.23],
    "data": sorted(list(pd.date_range("1/5/2014", periods= 2)) * 2)
})

print(df_cambio)

# Mudando o nome das colunas


df_cambio.columns = ["moeda", "cotacao", "data"]

print(df_cambio)




# Selcionar coluna 

cotacao = df_cambio['cotacao'] # retorna uma serie 

print(cotacao)

cotacao = df_cambio.cotacao # mesma coisa que a anterior 

print(cotacao)

# Selcionar 2 colunas

cotacao_e_data = df_cambio[['cotacao','data']] 

print(cotacao_e_data)

# Adicionadno a data como indice 
print()
df_cambio = df_cambio.set_index("data")
cotacao = df_cambio['cotacao']
print(cotacao)


# Selecionando colunas por condições

cambio_menor_que_5 = df_cambio[df_cambio["cotacao"] < 5]

print()
print(cambio_menor_que_5)

# Selecionando cambio 

cambio_dolar = df_cambio[df_cambio['moeda'] == 'dolar/real']
print()
print(cambio_dolar)


# Selecionando colunas com duas condições (operadores & e | )

cambio_dolar_e_maior_que_525 = df_cambio[(df_cambio["moeda"] == 'dolar/real') & (df_cambio["cotacao"] > 5.25)]

print(cambio_dolar_e_maior_que_525)