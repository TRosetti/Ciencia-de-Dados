SELECT t1.IdTransacao,
        t1.DtCriacao,
        t3.DescNomeProduto 
FROM transacoes AS t1

LEFT JOIN transacao_produto AS t2
ON t1.IdTransacao = t2.IdTransacao

-- WHERE t2.IdProduto IS NULL
LEFT JOIN produtos AS t3
ON t2.IdProduto = t3.IdProduto
 
WHERE DescNomeProduto  = 'Lista de presença'
 ;