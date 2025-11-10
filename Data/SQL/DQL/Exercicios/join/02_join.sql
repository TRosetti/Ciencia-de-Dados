-- Em 2024, quantas transações de 'lovers' tivemos? 

SELECT 
        t3.DescCategoriaProduto 
        , count(DISTINCT t1.IdTransacao)
FROM transacoes as t1


LEFT JOIN transacao_produto AS t2
ON t1.IdTransacao = t2.IdTransacao

LEFT JOIN produtos AS t3
ON t2.IdProduto = t3.IdProduto

WHERE t1.DtCriacao >= '2024-01-01'
AND t1.DtCriacao < '2025-01-01'
AND t3.DescCategoriaProduto = 'lovers'

;