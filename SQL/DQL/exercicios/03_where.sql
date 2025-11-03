-- Selecione todas os clientes com mais de 500 pontos (Exatos)

SELECT idCliente, qtdePontos 
FROM clientes
WHERE qtdePontos > 500;
