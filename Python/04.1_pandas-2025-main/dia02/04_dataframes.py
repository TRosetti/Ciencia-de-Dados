# %%

import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=';')
df_clientes


# %%

## AMOSTRAS

df_clientes.head(n=10) # .head() é parecido com o LIMIT no SQL, ele traz uma certa quantidade apenas (o default é 5)
# Pega as primeiras 
# %%
df_clientes.tail(10) # Parecido com o head, mas pega o final da lista 

# %%
df_clientes.sample(10) # Pega uma amostra aleatória

# %%
df_clientes.shape # retorna uma tupla com quantidade de linhas e colunas 

# %%
df_clientes.columns # Retorna o nome das colunas

# %%    
df_clientes.index # Retorna os Indices do data frame

# %%
df_clientes.info() # Retorna informações sobre o data frame
print()
df_clientes.info(memory_usage='deep', max_cols=2)  # Retorna a quantidade exata de memória ram utilzada pelo Data Frame

# %%
df_clientes.dtypes # Retorna uma serie mostrando as colunas e os tipos
df_clientes.dtypes['idCliente'] # Tipo object, retrna 'O'
df_clientes.dtypes['flEmail']
# %%
