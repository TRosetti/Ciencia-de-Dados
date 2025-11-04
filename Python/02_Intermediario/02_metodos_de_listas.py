'''
    Métodos da Classe list
'''

# [].append()       -> adiciona no fim da lista 

lista = []
lista.append(1)
lista.append('Nome')
lista.append(['Thiago', 21, '28/10/2001'])

print(lista)        #   _> [1, 'Nome', ['Thiago', 21, '28/10/2001']]


# [].clear()      -> limpa a lista

lista = [1, 'Nome', ['Thiago', 21, '28/10/2001']]

lista.clear()

print(lista)        #   _> []


# [].copy()      -> copia a lista           O bom disso é que podemos mexer nela sem alterar a original

lista = [1, 'Nome', ['Thiago', 21, '28/10/2001']]

l2 = lista.copy()

print(l2)       #   _> [1, 'Nome', ['Thiago', 21, '28/10/2001']]            


# [].count()       -> conta quantas vezes um obejto aparece na lista

cores = ['azul', 'vermelho', 'verde', 'verde', 'preto', 'vermelho' ]

print(cores.count('vermelho'))       # _> 2
print(cores.count('azul'))           # _> 1



# [].extend()       -> junta uma lista na outra (no final)

linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]



# [].index()       -> fala em qual posição está o objeto que quero ( começando do 0 ), mas só fala a primeira ocorrencia, se tiver outro ele não vai indicar

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0



# [].pop()          -> Retira o ultimo elemento da lista, caso queira tirar outro que não seja o ultimo basta passar o indice 


linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens.pop())  # java
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python



# [].remove()       -> Remove o primeiro item que vc escrever, se tiver repetido o que vc quer tirar precisa utilizar um for pra percorrer

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp"]



# [].reverse()      -> Espelhar a lista 

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens)  # ["csharp", "java", "c", "js", "python"]



# [].sort()          -> ordena a lista  

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]           # Ordem Alfabetica
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]     # Reverso da Ordem Alfabetica
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]        # Ordena do menor pro maior
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]    # Ordena do maior pro menor
print(linguagens)



# [].len()          -> tamanho da lista 

linguagens = ["python", "js", "c", "java", "csharp"]

print(len(linguagens))  # 5 



# [].sorted()       -> ordena a lista  (Função)

linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]
print(sorted(linguagens)) # ["c", "js", "java", "python", "csharp"]