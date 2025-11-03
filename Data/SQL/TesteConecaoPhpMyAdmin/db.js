require('dotenv').config();
const mysql = require('mysql2/promise');

const pool = mysql.createPool({
    // host: 'localhost', // Mude se a hospedagem fornecer outro host/IP
    host: process.env.ip_host, 
    user: process.env.usuario_db,
    password: process.env.senha_db,
    database: process.env.db, 
    waitForConnections: true,
    connectionLimit: 10,
    queueLimit: 0
});

// Teste rápido para garantir que as credenciais são válidas
(async () => {
    try {
        await pool.getConnection();
        console.log("Conexão com o Banco de Dados estabelecida com sucesso! ✅");
    } catch (e) {
        console.error("ERRO DE CONEXÃO: Verifique as credenciais no db.js!");
        console.error(e.message);
        process.exit(1); // Encerra se a conexão inicial falhar
    }
})();

module.exports = pool;