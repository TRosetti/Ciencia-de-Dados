--      Junções: JOINs
-- São usadas no sql para combinar dados de duas ou mais tabelas relacionadas em uma única consulta


--      Junções: Tipos
> INNER JOIN
> LEFT JOIN OU LEFT OUTER JOIN 
> RIGHT JOIN OU RIGHT OUTER JOIN 
> FULL JOIN OU FULL OUTER JOIN 



            INNER JOIN
-- Retorna apenas as linhas que têm correspondências em ambas as tabelas envolvidas na junção. 
-- A junção é feita com base em uma condição de igualdade especificada na cláusula ON

-- SELECT *
-- FROM tabela1
-- INNER JOIN tabela2 ON tabela1.coluna = tabela2.coluna


SELECT * FROM usuarios_nova us
INNER JOIN  reservas rs ON us.id = rs.id_usuario
-- Aqui retorna todos os usuarios que tem reservas 



            LEFT JOIN
-- Retorna todas as linhas da tabela á esquerda da junção e as linhas correspondentes da tabela á direita.
-- Se não houver correspondência, os valores da tabela á direita serão NULL

SELECT * 
FROM tabela1
LEFT JOIN tabela2 ON tabela1.coluna = tabela2.coluna;



         RIGHT JOIN 
-- Igual o left join mas invertido



        FULL JOIN  (não é aceito em todas plataformas)

-- Retorna todas as linhas de ambas as tabelas envolvidas na junção, combinando-as com base em condição de igualdade.
-- Se não houver correspondência, os valores ausentes serão preenchidos com NULL.

SELECT * 
FROM tabela1
FULL JOIN tabela2 ON tabela1.coluna = tabela2.coluna;





--  Sub Consulta 
--> Elas permitem realizar consultas mais complexas permitindo que você use o resultado de uma consulta como entrada para outra consulta

-- Podem ser usadas em varias parte de una consulta

- SELECT
- FROM
- WHERE
- HAVING
- JOIN 


SELECT * FROM usuarios_nova
WHERE id NOT IN (SELECT id_usuario FROM reservas)

-- Exemplo abaixo retorna o numero de reservas de um usuario

SELECT nome, (SELECT COUNT(*) FROM reservas WHERE id_usuario = usuarios_nova.id) AS total_reservas FROM usuarios_nova;





-- Funções Agregadas
- COUNT : conta o número de registros
- SUM: Soma os valores de uma coluna numérica
- AVG: Calcula a média dos valores de uma coluna numérica
- MIN: Retorna o valor mínimo de uma coluna
- MAX: Retorna o valor máximo de uma coluna


SELECT MAX(TIMESTAMPDIFF(YEAR, data_de_nascimento, CURRENT_DATE())) as maior_idade FROM usuarios_nova;
-- retorna a maior idade entre os usuarios



-- Agrupamento de Resultados
SELECT ...
FROM ...

GROUP BY 
--       ---        ---       --
SELECT COUNT(*), id FROM reservas
GROUP BY id_destino

-- Ordenação de Resultados
SELECT ...
FROM ...

ORDER BY 
--       ---        ---       --
SELECT COUNT(*) AS qtd_reservas, id_destino FROM reservas
GROUP BY id_destino
ORDER BY qtd_reservas



