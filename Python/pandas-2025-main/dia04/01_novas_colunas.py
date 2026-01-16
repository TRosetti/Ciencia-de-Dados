# %%

import pandas as pd
import numpy as np

df = pd.read_csv("../data/clientes.csv", sep=';')
df.head()

# %%

df["pontos_100"] = df["qtdePontos"] + 100
df.head()

# %%

nova_coluna = []   #  Essa é um maneira de fazer, porém não é a mais rápida. A opção de cima é melhor
for i in df["qtdePontos"]:
    nova_coluna.append( i+100)

nova_coluna

# %%
# ver se tem email ou twitch ou os dois (0 = não tem email e twitch), (1 = tem um dos dois), (2 = tem os dois
df["emailTwitch"] = df["flEmail"] + df["flTwitch"]
df.head()

# %%
# Ver se tem os dois (0 = tem nenhum ou tem apenas 1 dos dois), (1 = tem os dois)
df["flEmail"] * df["flTwitch"]

# %%
# Conta a quantidade de redes sociais que possui 
df["qtdeSocial"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df

# %%
# Veriifica se tem todos (0 = não tem pelo meno 1) (1 = Tem todos)
df["todas_social"] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] * df["flInstagram"]
df

# %%
df["qtdePontos"]

# %%

df["logPontos"] = np.log(df["qtdePontos"]+1)
df["logPontos"].describe()

# %%

import matplotlib.pyplot as plt

plt.grid(True)
plt.hist(df["logPontos"])
plt.show()