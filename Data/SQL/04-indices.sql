        Análise do Plano de Execução

-- Ela mos permite examinar as operações realizadas, as tabelas acessadas, os índices utilizados e outras informações importantes para identificar possíveis melhorias de desempenho.

EXPLAIN
    SELECT *
        FROM {{tabela}}
...


- Select_type: "SIMPLE", "SUBQUERY", "JOIN"
- table
- type: 'ALL', 'INDEX' entre outros
- possible_keys: Os índices possíveis que poem ser utilizados na operação
- key: O índice utilizado na operação, se aplicável
- key_len: O comprimento do índice utilizado
- ref: As colunas ou constantes usadas para acessar o índice
- rows


    Ídices de Busca

CREATE INDEX {{nome_index}}
ON {{tabela}} ({{coluna1, coluna2 ...}})
