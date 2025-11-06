-- Qual o produto com mais pontos transacionado?

SELECT IdProduto,
        -- count(*) AS QtdeVendas
        sum(QtdeProduto) AS TotalProdutosVendidos,
        sum(vlProduto * QtdeProduto) AS TotalPontos
       
FROM transacao_produto

GROUP BY 1
ORDER BY 3 DESC
LIMIT 10;
