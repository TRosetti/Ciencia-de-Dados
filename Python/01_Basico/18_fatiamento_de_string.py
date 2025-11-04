'''
    Fatiamento de Strings

Fatiamento de strings é uma técnica utilizada para retornar substrings (partes da string original), 
informando inicio (start), fim (stop) e passo (step): [start: stop[, step]]

'''

nome = "Thiago Rosetti Miranda"

print(nome[0])
print(nome[:10])        # Quando coloca os dois pontos antes do número, ele conta de 0 ao número e printa essas letras
print(nome[15:])        # Se colocar os dois ponto após o número, ele conta até o númeroe printa as letras após o número
print(nome[8:15:2])     # Aqui ele começa após o 8(9 pois começa a contar em 0) vai até o 15(16) e vai de 2 em 2 (steps)
print(nome[:])          # Retorna a string
print(nome[::-1])       # Espelha a string, fica de trás pra frente