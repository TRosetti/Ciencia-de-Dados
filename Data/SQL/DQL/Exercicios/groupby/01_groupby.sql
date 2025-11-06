-- Quantos clientes tem email cadastado? 

SELECT sum(flEmail)  
FROM clientes; -- Como nesse caso os quem tem email fica com 1 e os que não tem com 0, 
                     -- somando todos os valores teremos a quantidade de clientes com email
                     -- Esse caso é menos custoso que o segundo (abaixo)

SELECT count(*)
FROM clientes
WHERE flEmail = 1;