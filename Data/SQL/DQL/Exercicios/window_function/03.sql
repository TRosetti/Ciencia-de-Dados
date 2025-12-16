-- 3. Quantidade de transações acumuladas ao longo do tempo (diário)

with tb_diaria AS (
    SELECT  substr(DtCriacao, 1, 10) AS DtDia,
        COUNT(DISTINCT IdTransacao) AS QtDeTransacoe
    FROM transacoes
    GROUP BY DtDia
    ORDER By DtDia
),
tb_acum AS (
    SELECT 
    *,
    sum(QtDeTransacoe) OVER (ORDER BY DtDia) AS SumQtDeTransacoe
    FROM tb_diaria
    
)
-- Quando o número de tramsações ultrapassou 100.000
SELECT *  
FROM tb_acum 
WHERE SumQtDeTransacoe > 100000
LIMIT 1



 