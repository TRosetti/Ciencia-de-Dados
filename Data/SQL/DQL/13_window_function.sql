-- 13. Função de Janela: Soma Acumulada de Transações Diárias
WITH tb_sumantio_dias AS (

    SELECT substr(DtCriacao, 1, 10) AS dtDia,
        COUNT(distinct IdTransacao) AS qtDeTransacoes
    FROM transacoes 
    WHERE DtCriacao >= '2025-08-25'
    AND DTCriacao < '2025-08-30'

    GROUP BY dtDia
)

SELECT *,
    SUM(qtDetransacoes) OVER (ORDER BY dtDia) AS qtDeTransacoesAcumuladas
FROM tb_sumantio_dias;


