
-- Criação de tabela -- 


-- Comando: CREATE TABLE

CREATE TABLE {{nome}}
({{coluna}}{{tipo}}{{opções}} COMMENT {{'comentario'}} )


CREATE TABLE nome_da_tabela (
    id INT, -- INT = inteiro, o id vai ser do tipo inteiro
    nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuário',  -- VARCHAR é um tipo de string 
    email VARCHAR(100) NOT NULL UNIQUE COMMENT 'Email do usuário',  -- NOT NULL -> não pode ser vazio,  -- UNIQUE  -> É único, não pode ter outro igual
    data_de_nascimento DATE NOT NULL COMMENT 'Data de aniversario'  -- DATE é o tipo do dado(data_de_nascimento)
)  

-- TIPOS DE DADOS:

Inteiro             (Integer)
Decimal/Numérico    (Decimal / Numeric)
Caractere/Varchar   (Character / Varchar)
Data/Hora           (Date / Time)
Booleano            (Boolean)
Texto longo         (Text)

-- OPÇÕES
-- Restrições de valor:
    -- NOT NULL 
    -- UNIQUE
    -- DEFAULT 
-- Chaves primárias e estrangeiras
-- Auto incremento

\

-- Comando: INSERT

INSERT INTO 
{{nome-da-tabela}}   
([coluna1, coluna2, ...]) *** você pode ocultar as colunas
VALUES
([valor-coluna1,valor-coluna2, ...])

-- --------------------------------------------------------------- -- 

INSERT INTO usuarios (id, nome, email,  data_de_nascimento, endereco) VALUES (1, "Thiago Rosetti", "thiagorosetti1234@gmail.com", '2001-12-28', 'Av Anisio Fernandes Coelho, 1580, Vitória ES')

INSERT INTO destinos ( id, nome, descricao) VALUES (1, 'Vitória - ES', 'Localizada no Espirito Santo');

INSERT INTO reservas (id, id_usuario, id_destino, data, status) VALUES (1, 1, 1, '2024-01-15', 'pendente') 

-- --------------------------------------------------------------- -- 


--  CRUD    (CREATE - READ - UPDATE - DELETE) 


-- Até agora acima ja temos a parte do CREATE, falta o resto RUD


-- Comando: SELECT 

SELECT{{lista_colunas}}
FROM tabela;

-- Onde * retorna todas as colunas



-- Comando: SELECT com WHERE

SELECT {{lista_colunas}}
FROM tabela
WHERE {{condicao}}



SELECT * FROM `reservas`
WHERE status = 'pendente' OR status = 'confirmada';     --> Mostra todas as reservas pendentes e confirmadas



-- Comando: Select - Operadores

=           ( igualdade )
<> ou !=    ( desigualdade )
>           ( maior que )
<           ( menor que)
>=          ( maior ou igual que )
<=          ( menor ou igual que )
LIKE        ( comparação de padrões )
IN          ( pertence a uma lista de valores )
BETWEEN     ( dentro de um intervalo )
AND         ( e lógico )
OR          ( ou lógico )



-- Comando: UPDATE

UPDATE {{tabela}}
SET
{{coluna_1}} = {{novo_valor_1}}
{{coluna_2}} = {{novo_valor_2}}

WHERE
{{condicao}};


UPDATE reservas 
SET id = 4
WHERE data = '2023-09-20'

-- Comando: DELETE

DELETE FROM
{{tabela}}

WHERE
{{condicao}};

DELETE FROM reservas
WHERE id = 4;  




-- DROP TABLE -> remove a tabela do banco de dadps
--> Exclui permanentemente a tabela

DROP TABLE {{tabela}}



--  ALTER TABLE -> modifica a estrutura da tabela
-- Permite 
--> Adicionar, alterar ou excluir colunas 
--> Modificar as restrições, índices
--> Renomear a tabela entre outras aletrações 


ALTER TABLE usuarios_nova MODIFY COLUMN endereco VARCHAR(150)


--  CHAVE PRIMARIA 
--> identifica exclusivamente
--> nao pode conter valore nulos (NULL)
--> uma tabela pode ter apenas uma chave primária

Chaves Primarias

CREATE TABLE {{tabela}}
(id PRIMARY KEY AUTOINCREMENT, ...);
ALTER TABLE {{tabela}}
MODIFY COLUMN ID INT PRIMARY KEY;


-- CHAVES ESTRAGEIRAS
-- usado para estabelecer e manter a integridade dos dados entre tabelas relacionadas
--> pode ser nula ( NOT NUL ), ** registro órfão 
--> é possicel ter mais de uma ( ou nenhuma ) em uma tabela

Chaves Estrangeiras

CREATE TABLE {{tabela}} (
    id INT PRIMARY KEY,
    chave_estrangeira INT, 
    FOREIGN KEY (chave_estrangeira) REFERENCES {{outra tabela}} (id)
);

-- Alterar tabela ja criada para usaar uma Chave Estrangeira

ALTER TABLE {{tabela}}
ADD CONSTRAINT {{nome_constraint}}
FOREIGN KEY (ID_)
REFERENCES {{outra_tabela}}(ID)


-- CHAVES ESTRAGEIRAS - Restrições
--> ON DELETE - especifica o que acontece com os registros dependentes quando um registro pai é excluído
--> ON UPDATE - define o comportamento dos registros dependentes quando um registro pai é atualizado
--> CASCADE, SET NULL, SET DEFAULT e RESTRICT

 
ALTER TABLE usuarios_nova
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id);


ALTER TABLE reservas 
ADD CONSTRAINT fk_reservas_usuarios
FOREIGN KEY (id_usuario) REFERENCES usuarios_nova (id)
ON DELETE CASCADE;