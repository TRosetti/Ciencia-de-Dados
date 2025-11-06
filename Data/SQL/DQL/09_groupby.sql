-- SELECT IdProduto,
--         count(*)

-- FROM transacao_produto

-- GROUP BY IdProduto;


SELECT idCliente
        , SUM(qtdePontos) AS Pontos,
        count(IdTransacao) AS QtdTransacoes
FROM transacoes

WHERE DtCriacao >= '2025-07-01'
AND DtCriacao < '2025-08-01'

GROUP BY idCliente  -- Fazemos isso porque os clientes se repetem na tabela de transacoes, ai conseguimos pegar todos os pontos de cada cliente e somar eles  


HAVING SUM(qtdePontos) >= 4000  -- Filtramos os resultados para trazer apenas os clientes que tiveram mais de 4000 pontos no mês de julho de 2025

-- HAVING é o filtro do GROUP BY, parecido com o WHERE mas esse filtra depois do agrupamento
ORDER BY Pontos DESC

LIMIT 10; 