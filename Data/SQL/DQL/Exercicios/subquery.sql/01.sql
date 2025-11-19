-- Dos clientes que começaram SQL no primeiro, qunatos chegaram ao 5º dia? 

SELECT  count(DISTINCT idCliente) AS   
FROM transacoes AS t1

WHERE t1.idCliente IN (
    SELECT DISTINCT idCliente 
    FROM transacoes
    WHERE substr(DtCriacao, 1, 10) = '2025-08-25' -- primeiro dia
)
AND substr(t1.DtCriacao, 1, 10) = '2025-08-29'