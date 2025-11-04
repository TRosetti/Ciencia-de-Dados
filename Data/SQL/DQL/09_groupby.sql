SELECT IdProduto,
        count(*)

FROM transacao_produto

GROUP BY IdProduto;