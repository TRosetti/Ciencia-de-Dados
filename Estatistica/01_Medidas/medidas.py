# %% 
import pandas as pd 

# %% 
df = pd.read_csv("../../Data/Dados-teo-me-why/transacoes.csv", sep=';')

# %%
df.sample(10)
# %%
df['QtdePontos'].unique()
# %%
