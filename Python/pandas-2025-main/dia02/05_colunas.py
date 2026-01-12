# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=';')
df

# %%
df.shape

# %%
df.info(memory_usage="deep")

# %%
df.dtypes

# %%

renamed_columns = {
    "QtdePontos": "qtPontos",
    "descSistemaOrigem": "SistemaOrigem"
}

# df = df.rename(columns=renamed_columns)    # Troca os nomes das colunas selecionadas
df.rename(columns=renamed_columns, inplace=True) # Com o inplace=True, não precisamos reatribuir o dataframe, ele faz automaticamente 

# %%

df["IdCliente"] # retorna uma série 

# %%
colunas = ["IdCliente", "qtPontos"] 
df[colunas] # retorna um data frame 
 
# %%
# SELECT * FROM df
df

# %%
# SELECT idCliente FROM df

df[["IdCliente"]] # retorna um data frame, parece com a linha 29, mas ele é um lista ["IdCliente"], não só uma coluna "IdCliente"

# %%

# SELECT idCliente, qtPontos FROM df LIMIT 5
df[["IdCliente", "qtPontos"]].tail(5)

# %%

# SELECT idCliente, idTransacao, qtPontos
# FROM df
# LIMIT 5

df[["IdCliente", "IdTransacao", "qtPontos"]].head(5)

# %%

colunas = list(df.columns) #df.columns tras as colunas, podemos usar o list(df.columns) para transaforma-las em lista 
colunas.sort() # com isso, podemos usar o sort para deixar em ordem alfabética
colunas

df = df[colunas] # reatribui o dataframe com as colunas ordenadas anteriormente 
df
# %%
