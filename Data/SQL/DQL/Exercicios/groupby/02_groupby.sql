-- Quais os 5 clientes que fizeram mais transações em 2024? 

SELECT  idCliente,
        count(*) AS TotalTransacoes,
        count(DISTINCT idTransacao) AS TotalTransacoesUnicas

FROM transacoes

WHERE DtCriacao >= '2024-01-01' 
AND DtCriacao < '2025-01-01'
AND QtdePontos > 0

GROUP BY idCliente
ORDER BY TotalTransacoes DESC
LIMIT 5 

;
