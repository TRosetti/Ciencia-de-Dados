# %%

import pandas as pd
import requests
url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

# Definimos um User-Agent para o site achar que somos um navegador (Chrome/Safari)
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36"
}

# Fazemos a requisição primeiro
r = requests.get(url, headers=header)

# Passamos o texto da resposta para o pandas
# O Pandas pode dar um aviso se passarmos a string direto, então usamos io.StringIO
import io
dfs = pd.read_html(io.StringIO(r.text))
uf = dfs[1]
uf
# %%

def str_to_float(x:str):
    x = (x.replace(" ", "")
          .replace(",", ".")
          .replace("\xa0", "")
            )
    return float(x)

# %%

uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)

# %%
uf.dtypes

# %%

def exp_to_anos(exp:str):
    return float(exp.replace(",", ".")
                    .replace(" anos", ""))

uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(exp_to_anos)

# %%

def uf_to_regiao(uf):

    # tartar uf
    # uf = uf

    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"
    elif uf in ["Alagoas","Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return "Nordeste"
    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
       return "Norte"
    elif uf in ["Espírito Santo","Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"
    elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return "Sul"
    
uf["Região"] = uf["Unidade federativa"].apply(uf_to_regiao)

# %%

def mortalidade_to_float(x:str):
    x = float(x.replace("‰", "")
               .replace(",", ".")
              )
    return x

uf["Mortalidade infantil (/1000)"] = uf["Mortalidade infantil (2016)"].apply(mortalidade_to_float)

# %%

# %%

# Se PIB / Capita > 30.000
# +
# Mort Infantil < 15 / 1000
# +
# IDH (2010) > 700
# -> "Parece bom"

# Nao parece bom

# %%

def classifica_bom(linha):
    return (linha["PIB per capita (R$) (2015)"] > 30000 and
            linha["Mortalidade infantil (/1000)"] < 15 and 
            linha["IDH (2010)"] > 700)

# %%

uf.apply(classifica_bom, axis=1) # o axis=1 faz com que a função 'classifica_bom' seja aplicado a cada linha 
    # axis=0 passa cada coluna 
    # axis=1 passa todas as linhas  
# %%

uf.apply(lambda x: x["PIB per capita (R$) (2015)"], axis=1)