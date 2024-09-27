-- Verificar registros da tabela
SELECT * 
FROM estudantes;

-- Gravar um registro de teste
INSERT INTO estudantes(matricula, nome)
VALUES('1234', 'João da Silva');

-- Testando Update
UPDATE estudantes
SET nome = 'Antônio dos Santos'
WHERE matricula = '1234';

-- Verificar os registros da tabela
SELECT *
FROM estudantes;

-- Excluindo  registro da tabela
DELETE FROM estudantes
WHERE matricula = '1234';

-- Verificar registros na tabela
SELECT *
FROM estudantes;