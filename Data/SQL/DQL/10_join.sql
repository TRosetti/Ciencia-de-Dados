SELECT *
FROM transacao_produto

LEFT JOIN produtos 
ON transacao_produto.IdProduto = produtos.IdProduto

-- WHERE t2.IdProduto IS NULL

LIMIT 10;