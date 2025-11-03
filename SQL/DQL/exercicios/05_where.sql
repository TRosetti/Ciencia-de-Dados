--  Selecione produtos que contem 'churn' no nome

SELECT * 
FROM produtos

-- 	Churn_10pp
-- 	Churn_2pp
--	Churn_5pp

/*

WHERE DescNomeProduto = 'Churn_10pp' 
OR DescNomeProduto = 'Churn_2pp'
OR DescNomeProduto =  'Churn_5pp'

*/

-- WHERE DescNomeProduto IN ('Churn_10pp', 'Churn_2pp', 'Churn_5pp')

-- WHERE DescNomeProduto LIKE 'churn%' -- aqui pega todos que começam com churn, se eu quisesse todos que tivesse churn no nome poderia usar '%churn%'
-- WHERE DescNomeProduto LIKE '%pp'; -- termina com 


/*
    IMPORTANTE

O LIKE é muito custoso, pois precisa vericiar cada valor procurando o que você quer 

Se você sabe o que está procurando compensa mais ir no IN, se você não sabe, usa o LIKE  

*/


WHERE DescCategoriaProduto = 'churn_model'; -- Pesquisa menos custosa