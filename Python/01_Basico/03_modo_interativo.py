#   Modo interativo
#   -> Digite python no terminal para abrir
#   -> Para sair, escreva exit()
#   -> python -i NOME_DO_PROGRAMA abre o programa no modo interativo


#   Função dir
#   -> Sem argumento, retorna a lista de nomes no escopo local atual
#   -> Com argumento, retorna uma lista de atributos válidos para o objeto

dir()       # Sem atributo

dir(100)    # Com atributo, nesse caso vai retornar todos os metos que o objeto 100 tem, ele leva em conta o tipo, nesse caso, int


#   Função help
#   -> Invoca o sistema de ajuda integrado. 
#   -> É possivel fazer buscas no modo interativo ou informar por parâmetro qual o nome do módulo, fução, classe, método ou variável. Exemplo:

help()          # Nesse caso podemos buscar o que queremos 

help(100)       # Nesse caso vai mostrar a documentação do números inteiros, uma vez que 100 é um int

#   -> Para sair do help no modo interativo apertamos a letra   q   e damos Enter
#   -> Pode ser usado no modo offline 