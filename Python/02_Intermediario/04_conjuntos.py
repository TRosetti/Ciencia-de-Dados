'''
    Conjuntos - Set
Um set é uma colecão que não possui objetos repetidos, usamos
sets para representar conjuntos matemáticos ou eliminar itens
duplicados de um iterável

'''

#   Declarando conjuntos

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}        Não mostra na ordem

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

linguagens = {"python", "java", "python"}   # Se usarmos chaves ele automaticamente tira o duplicado, não precisa escrever set
print(linguagens)   # {"java", "python"}



'''
    Acessando os Dados
Conjuntos em python não suportam indexação e nem fatiamento, caso 
queira acessar os seu valores é necessário converter o conjunto
para lista    
'''

numeros = {1, 2, 3, 2}
# print(numeros[0])         _> TypeError: 'set' object is not subscriptable

numeros = list(numeros)

print(numeros[0])       # 1


#   Interar Conjuntos

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro , end=' ')  # palio gol celta 
print()

#   Enumerate()

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}", end=' ')    # 0: gol 1: celta 2: palio 
print()


'''
    Métodos da Classe Set

'''

#   Union()     -> Junta os conjuntos 

conjunto_a = {1, 2}
conjunto_b = {3, 4}

resultado = conjunto_a.union(conjunto_b)
print(resultado)    # {1, 2, 3, 4}



#   Intersection()      ->  Junta os que apresentam nos dois conjuntos

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b)
print(resultado)    # {2, 3}


#   Difference  -> Tudo que tem em um conjunto e não no outro

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)   # Tem no A e não tem no B
print(resultado)    # {1}

resultado = conjunto_b.difference(conjunto_a)   # Tem no B e não tem no A
print(resultado)    # {4}


#   Symmetric_difference()    -> Todos os elementos que não são iguais dos dois conjuntos

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)  # {1, 4}


#   Issubset()     -> Subespaço       

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b) # Todos os elementos A pertecem ao conjunto B?
print(resultado)     # True

resultado = conjunto_b.issubset(conjunto_a)  # Todos os elementos B pertecem ao conjunto A?
print(resultado)     # False


#   Issuperset()     -> contrario anterior   

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # Todos os elementos B pertecem ao conjunto A?
print(resultado)    # False

resultado = conjunto_b.issuperset(conjunto_a)  # Todos os elementos A pertecem ao conjunto B?
print(resultado)     # True


#   Isdisjoint      -> Verifica se tem algum valor igual em dois conjuntos, se Não tiver é True, se tiver é False

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # O conjunto A -NÃO- apresenta valores iguais ao B?
print(resultado)    # True

resultado = conjunto_a.isdisjoint(conjunto_c)  # O conjunto A -NÃO- apresenta valores iguais ao C?
print(resultado)    # False


#   Add()     -> Adiciona um item ao conjunto, caso não tenha

sorteio = {1, 23}

sorteio.add(25)  
print(sorteio)  # {1, 23, 25}

sorteio.add(42)
print(sorteio)  # {1, 23, 25, 42}

sorteio.add(25)
print(sorteio)  # {1, 23, 25, 42}



#   Clear()     -> Limpa o conjunto

sorteio = {1, 23}

print(sorteio)  # {1,23}

sorteio.clear()

print(sorteio)  # {}



#   Copy()     -> Copia o conjunto

sorteio = {1, 23}

print(sorteio)  # {1, 23}

sorteio.copy()

print(sorteio)  # {1, 23}



#   Discard()     -> Discarta um valor do conjunto, se não existir um valor que colocou ele ignora

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1)
numeros.discard(45) # não existe na lista, ele ignora

print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}



#   Pop()       ->  Retira o primeioro valor

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.pop())  # 0
print(numeros.pop())  # 1
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9}



#   Remove()       ->  Remove o valor que vc escolheu, Se tentarmos remover um numero que não existe ele da erro

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))  # 0
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}


#   Len()       -> Mostra o tamanho do conjunto

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(len(numeros))  # 10


#   In()       ->   Verifica se está no conjunto

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(1 in numeros)  # True
print(10 in numeros)  # False