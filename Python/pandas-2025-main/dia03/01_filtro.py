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

filtro = brinquedo["idade"] >= 18
brinquedo[filtro]

# %%

df = pd.read_csv("../data/transacoes.csv")
df.head()

# %%

# valores maiores que 50
filtro = df["qtdePontos"] >= 50
df[filtro]

# %%
# valores entre 50 (inclusive) e 100
filtro = (df["qtdePontos"] >= 50) & (df["qtdePontos"] < 100)
filtro
df[filtro]

# %%

filtro = (df["qtdePontos"] == 1) | (df["qtdePontos"] == 100)
df[filtro]

# %%
# pontos entre 0 e 50 ou do ano de 2025 para frente

filtro = (df["qtdePontos"] > 0) & (df["qtdePontos"]<=50) | (df["dtCriacao"]>='2025-01-01')
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