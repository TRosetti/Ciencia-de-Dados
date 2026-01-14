# %%

import pandas as pd

# %%

pontos = [10, 1, 1, 1, 50, 100, 130, 30, 25, 50]
filtro = []

valores_50_mais = []
for i in pontos:
    filtro.append(i>=50)


resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])


resultado
filtro
 # %%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32,35,14],
        "uf": ["sp", "pr", "rj"],     
     }
)

filtro = brinquedo["idade"] >= 18 # retorna uma serie contendo Boolenos 
brinquedo[filtro] # Aqui ele mostra apenas o resultado que tem um bool = true    

# %%

df = pd.read_csv("../data/transacoes.csv", sep=';')
df.head()

# %%

# valores maiores que 50
filtro = df["QtdePontos"] >= 50
df[filtro]

# %%
# valores entre 50 (inclusive) e 100
filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)
filtro
df[filtro]

# %%

filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
df[filtro]

# %%
# pontos entre 0 e 50 ou do ano de 2025 para frente

filtro = (df["QtdePontos"] > 0) & (df["QtdePontos"]<=50) | (df["DtCriacao"]>='2025-01-01')
df[filtro]

# %%

True  and True  = True
True  and False = False
False and True  = False
False and False = False

True  or True  = True
True  or False = True
False or True  = True
False or False = False