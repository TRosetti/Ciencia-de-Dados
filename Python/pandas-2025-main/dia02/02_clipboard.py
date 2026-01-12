# %%

import pandas as pd

df = pd.read_clipboard(sep=";") # usamos o clipboard para pegar os dados que estão copiados no teclado do pc, ex.: Copiei um csv (ctrl C + ctrl V), se eu rodar essa linha de código, ele vai criar um dataframe com os dados 
df