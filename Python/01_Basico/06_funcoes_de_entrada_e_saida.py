#   Funções de Entrada e Saída


#   Função Input
#   -> A função buitin input é utilizada quando queremos ler dados de entrada padrão(teclado).
#   -> Recebe argumento do tipo string, que é exibido ao usuário na saída padrão(tela).
#   -> A fução lê a entrada, converte em string e retorna o valor.

nome = input("Informe seu nome: ")


#   Função Print
#   -> A função buitin(vem da linguagem) print é utilizada quando queremos exibir dados na tela (saída padrão)
#   -> Recebe um argumento obrigatório do tio varangs de objeto e 4 argumentos opcionais ( sep, end, file, flush)
#   -> Todos objetos são convertidos para string, separados por sep e terminados por end. A string final é exibida para o usuário.

nome = "Thiago"
sobrenome = "Rosetti"

print(nome, sobrenome)                  #   _> Thiago Rosetti
print(nome, sobrenome, end="...\n")     #   _> Thiago Rosetti...  ( \n ) -> quebra a linha
print(nome, sobrenome, sep="#")         #   _> Thiago#Rosetti


print(nome, sobrenome, end="... ") 
print("Como não tem o \+n no end ele não quebra a linha")       # _> Thiago Rosetti... Como não tem o \+n no end ele não quebra a linha
