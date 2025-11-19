--  Qual mês tiemos mais lita de presença assinadas?
SELECT substr(t1.DtCriacao, 1, 7) AS Mes,
        count(DISTINCT t1.IdTransacao) AS TotalListas
FROM transacoes AS t1
        LEFT JOIN transacao_produto AS t2 ON t1.IdTransacao = t2.IdTransacao -- WHERE t2.IdProduto IS NULL
        LEFT JOIN produtos AS t3 ON t2.IdProduto = t3.IdProduto
WHERE DescNomeProduto = 'Lista de presença'
GROUP BY Mes;

-- Quais clientes assinaram a lista de presença no dia 2025/08/25?
SELECT t1.idCliente,
        count(*)
FROM transacoes AS t1
        LEFT JOIN transacao_produto AS t2 ON t1.IdTransacao = t2.IdTransacao
        LEFT JOIN produtos AS t3 ON t2.IdProduto = t3.IdProduto
WHERE substr(t1.DtCriacao, 1, 10) = '2025-08-25'
        AND t3.DescNomeProduto = 'Lista de presença'
GROUP BY t1.IdCliente;