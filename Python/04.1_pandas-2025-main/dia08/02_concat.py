# %%

import pandas as pd

df = pd.DataFrame({
    "cliente": [1,2,3,4,5],
    "nome": ["teo", "jose", "nah", "mah", "lah"],
})

df_02 = pd.DataFrame({
    "cliente": [6,7,8],
    "nome": ["kozato", "laura", "dan",],
    "idade":[32,29,31],
})

df_03 = pd.DataFrame({
    "idade": [32,34,19,54,33]
})

# %%

dfs = [df, df_02] # pd.concat() -> espera uma lista de dataframes 

pd.concat(dfs, ignore_index=True)

# %%

df_03 = df_03.sort_values(by='idade').reset_index(drop=True)
df_03

# %%

pd.concat([df, df_03], axis=1) # axis -> muda a direção do concat, normalmente ele adiciona o segundo dataframe em baixo do primeiro, quando adicionamos o axis=1 ele adiciona ao lado do primeiro 
# %%
