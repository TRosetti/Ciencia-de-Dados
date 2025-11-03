-- SUM() retorna a soma dos valores de uma coluna numérica.

SELECT avg(QtdePontos) AS mediaPontos, -- média dos pontos ganhos em julho de 2025
        sum(qtdePontos) / count(idCliente) AS mediaPontos2,
        min(QtdePontos) AS menorPontos,  -- menor valor de pontos ganhos
        max(QtdePontos) AS maiorPontos,   -- maior valor de pontos ganhos
        sum(flTwitch)
FROM clientes;




SELECT round(avg(QtdePontos),2) AS mediaPontos, -- round arredonda a média para 2 casas decimais
        round(1. * sum(qtdePontos) / count(idCliente),2) AS mediaPontos2
FROM clientes; -- na segnda eu adicinei o 1. * para forçar a conversão para decimal, e o round para arredondar para 2 casas decimais