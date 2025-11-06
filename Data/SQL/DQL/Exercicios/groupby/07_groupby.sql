-- Qual o produto campeão de vendas?

SELECT IdProduto,
        -- count(*) AS QtdeVendas
        sum(QtdeProduto) AS TotalProdutosVendidos
FROM transacao_produto

GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;
