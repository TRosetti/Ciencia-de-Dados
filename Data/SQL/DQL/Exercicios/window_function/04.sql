-- 3. Quantidade de usuários cadastrado ao longo do tempo

with tb_clientes_dia as (
    SELECT  substr(DtCriacao, 1, 10) AS DtDia,
        count(distinct IdCliente) AS qtCliente
    FROM clientes
    GROUP BY DtDia

),

tb_acumulado_cliente AS (
    
    SELECT *,
        sum(qtCliente) OVER (ORDER BY DtDia) AS sumAcumuladoCliente
        FROM tb_clientes_dia
)

SELECT * 
FROM tb_acumulado_cliente
WHERE sumAcumuladoCliente > 3000
ORDER BY DtDia

