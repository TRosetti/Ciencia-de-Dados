-- Qual o valor médio de pontos positivos por dia?

SELECT sum(QtdePontos) AS TotalPontos,
        -- count(substr(DtCriacao, 1, 10)) AS qtDeDiasRepetindos,
        count(DISTINCT substr(DtCriacao, 1, 10)) AS qtDeDiasDestintos,
        sum(QtdePontos) / count(DISTINCT substr(DtCriacao, 1, 10)) AS MediaPontosPorDia
FROM transacoes

WHERE QtdePontos > 0
;
