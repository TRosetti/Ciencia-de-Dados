
/*

SELECT *
 FROM clientes
 LIMIT 10;

--  Selecione todas as colunas da tabela 'clientes', limite de 10 linhas

*/


SELECT  idCliente,
        DtCriacao,
        DtAtualizacao
 FROM clientes
 LIMIT 10;

--  Selecione todas as colunas da tabela 'clientes', limite de 10 linhas

/*
SELECT IdProduto, DescNomeProduto
FROM produtos
LIMIT 10;
*/

SELECT *
FROM produtos
WHERE DescCategoriaProduto = 'rpg'
-- ' ' (acessar valor de um campo 'registro')
-- " " (acessar o campo)
LIMIT 10;



-- SELECT COL

SELECT idCliente,
        QtdePontos,
        QtdePontos + 10 AS QtdePonstosPlus10, -- Cria uma coluna (não altera no banco), somando 10 aos pontos
        QtdePontos * 2 AS QtdePonstosDouble ,  -- Cria uma coluna (não altera no banco), multipicando 2 aos pontos
        DtCriacao,

        -- Criando colunas (apenas na visualição - não altera o banco de dados)

        -- substr(DtCriacao, 1, 19) AS DtSubstring, -- substr (fatia a string do 1 ao 10 'nesse caso')
        dateTime( substr(DtCriacao, 1, 19)) AS DtHora, -- Transforma em data
        strftime('%w', dateTime( substr(DtCriacao, 1, 19))) AS diaSemana
FROM clientes;