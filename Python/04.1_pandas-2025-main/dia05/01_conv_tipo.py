# %%

import pandas as pd

# %%

df = pd.read_csv("../data/clientes.csv", sep=';')

# %%

df["qtdePontos"].astype(float).astype(str) # astype() muda o tipo do dado de acordo com o que você adicionar no (), retona uma série 

# %%

replace = {"0000-00-00 00:00:00.000": "2024-02-01 09:00:00.000"} # fazemos isso pq esse caso "0000-00-00 00:00:00.000" da erro

df["DtCriacao"] = pd.to_datetime(df["DtCriacao"].replace(replace))

# %%

df["DtCriacao"].dt.month

# %%
df["DtCriacao"].dt.daysinmonth
# %%
df["DtCriacao"].dt.day_of_year
# %%
