SELECT * FROM relatorio_diario;

UPDATE relatorio_diario 
SET QtDeTransacoe = 10000
WHERE DtDia >= '2025-08-25';

SELECT * FROM relatorio_diario; 