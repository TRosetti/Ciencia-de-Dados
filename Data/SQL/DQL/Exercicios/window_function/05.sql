-- Qual o dia da semana mais ativo de cada usuário?

WiTH tb_cliente_semana AS (
        SELECT  IdCliente,       
                strftime('%w' , substr(DtCriacao, 1, 10)) AS DiasSemana, -- 0 (dom), 1 (seg) ...
                count(DISTINCT IdTransacao) AS qntTransacao
        FROM transacoes
        GROUP BY IdCliente, DiasSemana
),

tb_rn AS (
        SELECT *,
                CASE 
                 WHEN DiasSemana = '2' THEN 'TERÇA'
                 WHEN DiasSemana = '3' THEN 'QUARTA'
                 WHEN DiasSemana = '4' THEN 'QUINTA'
                 WHEN DiasSemana = '5' THEN 'SEXTA'
                 WHEN DiasSemana = '6' THEN 'SÁBADO'
                 ELSE 'DOMINGO'
                 END AS descDiaSemana,
                 
                ROW_NUMBER() OVER (PARTITION BY IdCliente ORDER BY qntTransacao DESC) AS rn
        FROM tb_cliente_semana
)


SELECT * 
FROM tb_rn 
WHERE rn = 1
