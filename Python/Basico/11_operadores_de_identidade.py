'''
    Operadores de Identidade

São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória.

'''

curso = 'Curso de Python'
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso         #   _> True         pergunta: curso utiliza a mesma posição de memória de nome_curso , retorna True

curso is not nome_curso     #   _> False

print(saldo is limite )     #   _> True