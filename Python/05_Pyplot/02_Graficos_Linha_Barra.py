# %% 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# %%

params = {"ytick.color" : "w",
          "xtick.color" : "w",
          "axes.labelcolor" : "w",
          "axes.edgecolor" : "w"}
plt.rcParams.update(params)

# %% 

x = ["1T", "2T", "3T", "4T"]
y = [2000, 2200, 1100, 3540]

# %% 
plt.plot(x, y)

# %%
#vai ter uma aula sobre cada característica dessa.

plt.plot(x, y, color="green", marker='o')

#quer uma super customização? Crie gráficos como objetos. 
# %%


cotacoes = yf.download("WEGE3.SA")['Adj Close']

cotacoes.plot()
# %%
