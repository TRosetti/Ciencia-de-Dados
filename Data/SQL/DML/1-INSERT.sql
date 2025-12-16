-- Inserindo dados de uma função em uma tabela 
DELETE FROM relatorio_diario;


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


INSERT INTO relatorio_diario

SELECT *  
FROM tb_acum ;

SELECT * FROM relatorio_diario;