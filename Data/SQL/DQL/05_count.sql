SELECT 
    count(*),   -- Retorna a contagem total de registros na tabela clientes
    count(1),   -- Mesma coisa
    count(IdCliente)  -- Conta o número de registros onde IdCliente não é NULL
    
from clientes;


SELECT 
    DISTINCT flTwitch, flEmail
From clientes;


SELECT 
    DISTINCT flTwitch -- Retorna valores distintos na coluna IdCliente
From clientes;

SELECT 
    COUNT(DISTINCT DtCriacao)
From clientes;