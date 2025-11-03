SELECT     
    sum(qtdePontos) AS TotalPontosJulho2025,
    sum(
    CASE 
       WHEN qtdePontos > 0 THEN QtdePontos        
    END) AS SaldosPositivos,
    sum(
    CASE 
       WHEN qtdePontos < 0 THEN QtdePontos        
    END) AS SaldosNegativos

FROM transacoes

    WHERE DtCriacao >= '2025-07-01' 
    AND DtCriacao < '2025-08-01'    
;

-- SUM() retorna a soma dos valores de uma coluna numérica.


