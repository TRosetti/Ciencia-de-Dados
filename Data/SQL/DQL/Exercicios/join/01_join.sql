-- Qual a categoria tem mais produtos vendidos? 

SELECT
        t2.DescCategoriaProduto,
        count(DISTINCT t1.IdTransacao)
FROM transacao_produto AS t1

LEFT JOIN produtos AS t2
ON t1.IdProduto = t2.IdProduto

GROUP BY t2.DescCategoriaProduto
;


