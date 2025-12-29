# %%

import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv")
df_clientes


# %%
## AMOSTRAS

df_clientes.head(n=10)

# %%
df_clientes.tail(10)

# %%
df_clientes.sample(10)

# %%
df_clientes.shape

# %%
df_clientes.columns

# %%
df_clientes.index

# %%
df_clientes.info(memory_usage='deep', max_cols=2)

# %%
df_clientes.dtypes