# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv" , sep=";")  # Ler arquivo
df  #  sep=";", indica que o csv está sendo separado por ';' 

 # %%

df.to_csv("clientes.csv", index=False) # Salva um dataframe, gerou um arquivo na mesma pasta que estamos, agora com o df clientes.csv
# %%

df.to_parquet("clientes.parquet", index=False) 

# %%

df_2 = pd.read_parquet("clientes.parquet")
df_2

# %%

df.to_excel("clientes.xlsx", index=False)

# %%

df_3 = pd.read_excel("clientes.xlsx")
df_3

