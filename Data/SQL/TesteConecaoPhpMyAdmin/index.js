// index.js
const pool = require('./db');
const bcrypt = require('bcrypt');

/**
 * Função para cadastrar um novo usuário na tabela 'usuarios_teste'.
 * @param {string} nome
 * @param {string} email
 * @param {string} senhaPura Senha em texto simples, que será criptografada.
 */
async function cadastrarUsuario(nome, email, senhaPura) {
    let connection;
    try {
        // Criptografar a senha (Hashing)
        const saltRounds = 10;
        const senhaHash = await bcrypt.hash(senhaPura, saltRounds);

        // Comando SQL (Prepared Statement)
        const sql = "INSERT INTO usuarios_teste (nome, email, senha) VALUES (?, ?, ?)";
        const valores = [nome, email, senhaHash];

        connection = await pool.getConnection();

        // Executa a query
        const [results] = await connection.execute(sql, valores);
        
        console.log(`\nUsuário '${nome}' cadastrado com sucesso! ID: ${results.insertId}`);
    } catch (error) {
        // Se for um erro de duplicidade (ex: email repetido, se tivesse unique index)
        if (error.code === 'ER_DUP_ENTRY') {
            console.error("\nERRO: Este e-mail já está cadastrado.");
        } else {
            console.error("\nErro ao cadastrar usuário:", error.message);
        }
    } finally {
        // Libera a conexão
        if (connection) {
            connection.release();
        }
    }
}

// --- Execução do Teste ---
(async () => {
    // 1. Tente cadastrar o primeiro usuário
    await cadastrarUsuario("Testador Node 1", "teste1@sistema.com", "senha123");
    
    // 2. Tente cadastrar o segundo usuário
    await cadastrarUsuario("Testador Node 2", "teste2@sistema.com", "senha456");

    // 3. Encerra o processo após as operações
    process.exit(0); 
})();