# %%

import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

# Criamos um "disfarce" (User-Agent) para o Python
header = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Fazemos a requisição usando o requests primeiro
response = requests.get(url, headers=header)

# Agora passamos o conteúdo do texto da resposta para o read_html
dfs = pd.read_html(response.text)

# Para ver a primeira tabela encontrada, por exemplo:
print(dfs[0].head())
# %%

df_uf = dfs[1]
df_uf.to_csv("ufs.csv", sep=";", index=False)

# %%

df = pd.read_csv('ufs.csv', sep=";")
df

