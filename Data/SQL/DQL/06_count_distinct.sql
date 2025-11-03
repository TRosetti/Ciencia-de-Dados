SELECT count(*),
        count(DISTINCT IdTransacao) AS TotalTransacoesJulho2025,
        count(DISTINCT IdCliente) AS TotalClientesQueFizeramTransacoesJulho2025
FROM transacoes

    WHERE DtCriacao >= '2025-07-01' 
    AND DtCriacao < '2025-08-01'

ORDER BY DtCriacao DESC;


SELECT sum(qtdePontos)
FROM transacoes

    WHERE DtCriacao >= '2025-07-01' 
    AND DtCriacao < '2025-08-01'
;