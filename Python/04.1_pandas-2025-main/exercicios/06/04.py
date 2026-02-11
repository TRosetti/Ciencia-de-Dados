# %%
# 06.04 - Quem teve mais transações de Streak?

import pandas as pd

# %%

transacoes = pd.read_csv("../../data/transacoes.csv")
transacoes.head()

# %%
transacao_produto = pd.read_csv("../../data/transacao_produto.csv")
transacao_produto.head()

# %%
produtos = pd.read_csv("../../data/produtos.csv")
produtos.head()

# %%

cliente_transacao_produto = transacoes.merge(
    transacao_produto,
    on="idTransacao",
    how="left",
)[['idTransacao', "idCliente", "idProduto"]]

df_full = cliente_transacao_produto.merge(
    produtos,
    on=['idProduto'],
    how='left',
)

df_full = df_full[df_full["descProduto"]=="Presença Streak"]

(df_full.groupby(by=["idCliente"])["idTransacao"]
        .count()
        .sort_values(ascending=False)
        .head(1)
)

# %%

produtos = produtos[produtos["descProduto"]=="Presença Streak"]

(transacoes.merge(transacao_produto, on=["idTransacao"], how="left")
           .merge(produtos, on=["idProduto"], how="inner")
           .groupby(by="idCliente")["idTransacao"]
           .count()
           .sort_values(ascending=False)
           .head(1)
)