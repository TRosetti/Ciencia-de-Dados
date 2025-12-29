# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")
clientes.head()

# %%

filtro = clientes["qtdePontos"] == 0
clientes_0 = clientes[filtro].copy()

clientes_0["flag_1"] = 1
clientes_0

# %%

A = [1,2]
B = A.copy()
print("A:", A)
print("B:", B)

B.append("fodase")
print("A:", A)
print("B:", B)
