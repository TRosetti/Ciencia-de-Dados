-- 1. Função para saber quanto cada pessoa transacionou por dia, depois pegar o acumulado 

WITH tb_cliente_dias AS (

    SELECT IdCliente,
        substr(DtCriacao, 1, 10) AS dtDia,
        count(distinct IdTransacao) AS qtDeTransacoes
    FROM transacoes
    WHERE DtCriacao >= '2025-08-25'
    AND DTCriacao < '2025-08-30'
    GROUP BY idCliente, dtDia
),

tb_lag  AS(
    SELECT *,
        SUM(qtDeTransacoes) OVER (PARTITION BY IdCliente ORDER BY dtDia) AS acumnulado,
        lag(qtDeTransacoes) OVER (PARTITION BY IdCliente ORDER BY dtDia) AS lagTransacoes 
    FROM tb_cliente_dias 
)

SELECT *,
    1. * qtDeTransacoes / lagTransacoes AS engajamento
FROM tb_lag;
