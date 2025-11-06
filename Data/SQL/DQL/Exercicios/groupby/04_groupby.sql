-- Quantos produtos são RPG? 

SELECT count(*) AS TotalRPG
FROM produtos
WHERE DescCategoriaProduto = 'rpg'
;

SELECT 
    DescCategoriaProduto,
    count(*)
FROM produtos
GROUP BY DescCategoriaProduto 
;