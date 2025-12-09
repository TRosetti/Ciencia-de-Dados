-- Qual o dia com maior engajamento de cada aluno que iniciou uo curso no dia 01? 


WITH alunos_dia_01 AS (

    SELECT DISTINCT idCliente
    FROM transacoes
    WHERE substr(DtCriacao, 1, 10) = '2025-08-25'

),
tb_dia_clientes AS (
    SELECT t1.idCliente, 
        substr(t2.DtCriacao,1,10) AS dtDia, 
        count(*) AS quant_interacoes
    FROM alunos_dia_01 AS t1 

    LEFT JOIN transacoes AS t2
    ON t1.idCliente = t2.idCliente
    AND t2.DtCriacao >= '2025-08-25'
    AND t2.DtCriacao < '2025-08-30'

    GROUP BY t1.idCliente, dtDia
    ORDER BY t1.idCliente, dtDia
),
tb_rn AS (
    SELECT * ,
        row_number() OVER (PARTITION BY idCliente ORDER BY quant_interacoes DESC, dtDia) AS rn 
        -- Essa linha acima, está enumerando as linhas Particioando por idCliente, e ordenando pelo quantidad e interações de forma decresecente. Com isso o maior numero de interações sempre estara no rn 1 (conseguindo assim filtrar para pegar só o maior)
    FROM tb_dia_clientes
)


SELECT * 
FROM tb_rn
WHERE rn = 1
