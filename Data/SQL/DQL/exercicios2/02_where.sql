-- Pedidos realizados no fim de semana 

SELECT  IdTransacao, DtCriacao,
        strFtime('%w', dateTime(DtCriacao)) AS DiasSemana
        -- dateTime( substr(DtCriacao, 1, 19)) AS DtHora,
FROM transacoes

WHERE DiasSemana IN ('6', '0') -- Domingo (0), sábado (6)
; 