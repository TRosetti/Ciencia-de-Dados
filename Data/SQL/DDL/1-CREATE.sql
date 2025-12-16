-- Criando Tabela a partir de funções 

DROP TABLE IF EXISTS relatorio_diario; -- caso queria recriar a tabela para atualizar alguma coisa esse drop está aqui pra isso (apaga a tablea caso exista)

CREATE TABLE IF NOT EXISTS relatorio_diario AS 

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

SELECT *  
FROM tb_acum ;



SELECT * FROM relatorio_diario;