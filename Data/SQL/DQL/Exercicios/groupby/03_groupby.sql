-- Quais os 5 clientes que juntaram  mais pontos positivos em 2025-05? 

SELECT  idCliente,
        SUM(QtdePontos) AS TotalPontos
FROM transacoes

WHERE DtCriacao >= '2025-05-01' 
AND DtCriacao < '2025-06-01'
AND QtdePontos > 0

GROUP BY idCliente
ORDER BY TotalPontos DESC

LIMIT 5
;
