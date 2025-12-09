-- 2 Função para calcular média de frenquencia de todos os clientes do canal 

WITH cliente_dias AS (

    SELECT DISTINCT IdCliente,
        substr(DtCriacao, 1, 10) AS dtDia

    FROM transacoes
    WHERE substr(DtCriacao,1 ,4) = '2025'
    
    GROUP BY idCliente, dtDia
),

tb_lag AS (
    SELECT *,
        lag(dtDia) OVER (PARTITION BY IdCliente ORDER BY DtDia) AS lagDia
    FROM cliente_dias
),

tb_diff AS (SELECT *,
    julianday(dtDia) - julianday(lagDia) AS DtDiff
FROM tb_lag
),

avg_clientes as (
        SELECT IdCliente, avg(DtDiff) AS recorrencia_no_canal

    FROM tb_diff 
    GROUP BY IdCliente
)

SELECT AVG(recorrencia_no_canal) AS media_recorrencia_clientes
FROM avg_clientes;

