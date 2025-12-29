# %%

import pandas as pd

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

dfs = pd.read_html(url)
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

uf.apply(classifica_bom, axis=1)

# %%

uf.apply(lambda x: x["PIB per capita (R$) (2015)"], axis=1)