# %%
import pandas as pd

df = pd.read_csv("../data/transacao_produto.csv", sep=";")
df
df["IdProduto"].dtype


# %%

filtro = (df["IdProduto"] == "5") | (df["IdProduto"] == "11") # Tive que adicionar "", pois o 'df["IdProduto"].dtype' está retornando "O" (objeto)
df[filtro]

# %%

filtro = df["IdProduto"].isin(["5","11"]) # mesma coisa do de cima, verifica se os itens da lista tem 5 ou 11
df[filtro]

# %%

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()

filtro = clientes["DtCriacao"].notna() # Retorna True quem não for Nulo
# filtro = clientes["DtCriacao"].isna() # Retorna True quem for Nulo
clientes[filtro]

# %%

~clientes["DtCriacao"].isna() # o '~' é um sinal de negação, parecido com o '!'
clientes["DtCriacao"].notna()
# %%
