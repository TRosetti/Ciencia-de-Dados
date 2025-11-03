-- Intervalos
-- De 0 a 500           -> Ponei
-- De 501 a 1000        -> Ponei Premium
-- De 1001 a 5000       -> Mago Aprendiz
-- De 5001 a 10000      -> Mago Mestre
-- +10001               -> Mago Supremo

-- SELECT idCliente, QtdePontos,
    
--        CASE 
--            WHEN QtdePontos <= 500  THEN 'Ponei'
--            WHEN QtdePontos > 500 AND QtdePontos <= 1000 THEN 'Ponei Premium'
--            WHEN QtdePontos > 1000 AND QtdePontos <= 5000 THEN 'Mago Aprendiz'
--            WHEN QtdePontos > 5000 AND QtdePontos <= 10000 THEN 'Mago Mestre'
--            WHEN QtdePontos > 10000 AND QtdePontos > 10000 THEN 'Mago Supremo'
--        END AS Categoria
    
-- FROM clientes
-- ORDER BY QtdePontos DESC ;




---- OBS: Um case gera apenas uma Coluna de saída


SELECT idCliente, QtdePontos,
    
        CASE -- Gera uma coluna
            WHEN QtdePontos <= 500  THEN 'Ponei'
            WHEN QtdePontos <= 1000 THEN 'Ponei Premium'
            WHEN QtdePontos <= 5000 THEN 'Mago Aprendiz'
            WHEN QtdePontos <= 10000 THEN 'Mago Mestre'           
            ELSE 'Mago Supremo'
        END AS NomeGurpo,

        CASE -- Gera uma coluna
            WHEN QtdePontos <= 1000 THEN 1
            Else 0
        END AS flPonei,

        CASE -- Gera uma coluna 
            WHEN QtdePontos > 1000 THEN 1
            Else 0
        END AS flMago

FROM clientes
ORDER BY QtdePontos DESC ;


