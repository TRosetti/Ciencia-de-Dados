-- SELECT  count(DISTINCT idCliente) AS   
-- FROM transacoes AS t1

-- WHERE t1.idCliente IN (
--     SELECT DISTINCT idCliente 
--     FROM transacoes
--     WHERE substr(DtCriacao, 1, 10) = '2025-08-25' -- primeiro dia
-- )
-- AND substr(t1.DtCriacao, 1, 10) = '2025-08-29'

WITH tb_cliente_primeiro_dia AS (

    SELECT DISTINCT IdCliente
    FROM transacoes
    WHERE substr(DtCriacao, 1, 10) = '2025-08-25'

),

tb_cliente_ultimo_dia AS (

    SELECT DISTINCT IdCliente
    FROM transacoes
    WHERE substr(DtCriacao, 1, 10) = '2025-08-29'

),

tb_join AS (
    SELECT t1.idCliente AS primeiro_dia_cliente,
            t2.idCliente AS ultimo_dia_cliente
        FROM    tb_cliente_primeiro_dia AS t1

        LEFT JOIN  tb_cliente_ultimo_dia AS t2
        ON t1.idCliente = t2.idCliente


)

   
SELECT  count(primeiro_dia_cliente),
        count(ultimo_dia_cliente),
        1. * count(ultimo_dia_cliente) /  count(primeiro_dia_cliente) AS proporcao´
FROM tb_join