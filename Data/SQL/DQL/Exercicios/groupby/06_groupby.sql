-- Qual dia da semana tem mais pedidos em 2025?

SELECT 
        strftime('%w', substr(DtCriacao, 1, 10)) AS DiaDaSemana, -- 0 (dom), 1 (seg), 2(ter)...
        count(DISTINCT IdTransacao) AS TotalTransacoes
FROM transacoes

WHERE substr(DtCriacao, 1, 4) = '2025'

GROUP BY 1 -- group by 1 -> agrupa pelo primeiro campo do select
ORDER BY 2 DESC;