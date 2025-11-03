--  Normalização de Dados 
-- > A normalização de dados é um processo no qual se organiza e estrutura um banco relacional de forma a eliminar redundância e anomalias, garantido a consistência e integridade dos dados

-- Formas Normais
-- 1FN: Atomicidade de Dados
-- Indivisivel, exemplo, adicionar o endereço, em vez de colocar 
-- Endereço: Rua XXXXXX, n 1580, Vitória - ES
-- Colocar separado
--> Rua: Rua XXXXXX
--> numero: 1580
--> Cidade: Vitória
--> Estado: Espirito Santo 




-- Função SUBSTRING

-- Adicionar colunas de endereço à tabela "usuarios_nova"
ALTER TABLE usuarios_nova
ADD rua VARCHAR(100),
ADD numero VARCHAR(10),
ADD cidade VARCHAR(50),
ADD estado VARCHAR(50);

-- Copia os dados da tabela original para a nova tabela
UPDATE usuarios_nova
SET rua = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 1), ',', -1),
    numero = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 2), ',', -1),
    cidade = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 3), ',', -1),
    estado = SUBSTRING_INDEX(endereco, ',', -1);

-- Exclusão da coluna "endereco" da tabela original
ALTER TABLE usuarios_nova
DROP COLUMN endereco;





-- 2FN
--> Para a 2ª Forma Normal, é preciso que a tabela esteja na 1ª F.N.
--> Todos os atributos não chave devem depender totalmente da chave primária


-- 3FN
--> Para a 3ª Forma Normal, é preciso que a tabela esteja na 1ª e 2ª F.N.
--> Nenhuma coluna não-chave pode depender de uma outra coluna não-chave
-- Exemplo: Relação Estado > Cidade




