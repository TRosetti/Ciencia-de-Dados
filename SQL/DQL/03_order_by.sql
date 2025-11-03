SELECT * FROM clientes
ORDER BY QtdePontos DESC -- Oderna decrescente 
LIMIT 10;


SELECT * FROM clientes
ORDER BY DtCriacao -- Quando não especificado, o padrão é ASC
LIMIT 10;


SELECT * FROM clientes
WHERE flTwitch = 1
ORDER BY DtCriacao ASC, QtdePontos DESC 
LIMIT 10;