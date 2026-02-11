# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=';')
clientes

# %%

clientes.dropna(how="any") # apaga todas as linhas com NA 

# Tipos de dropna

# how="any"   -  Apaga todas as linhas que tem pelo menos um NA
# how="all"   -  Apaga todas as linhas que tem todas as colunas com NA

# %%

df = pd.DataFrame(
    {
        "nome": ["Téo", None, "Nah", "Marcio"],
        "idade": [None, None, 43, 52],
        "salario": [3453,4324,None,5423]
    }
)

# df
df.dropna(how="all", subset=["idade", "nome"]) # subset - filtra quais colunas quero ver ser tem NA

# %%

df["idade"] = df["idade"].fillna(0) # fillna() - adiciona o valor desejado nos itens da coluna escolhida
df

# %%

df.fillna({"nome": "alguem", "idade": 0}) # Aqui estamos passando valores definidos para mais de uma coluna, nesse caso é para coluna de nome e idade 

# %%
medias = df[['idade', 'salario']].mean() # mean() - pega a média dos valores das colunas selecionadas
df.fillna(medias)

# %%

df["idade"].fillna(df["idade"].mean()).mean()