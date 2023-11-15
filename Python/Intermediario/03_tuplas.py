'''
    Tuplas
Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que tuplas são 
imutáveis enquanto lista são mutáveis. Podemos criar tuplas através da classe tuple, ou colocando 
valores por vírgula de parenteses.

'''

#   Declarando Tuplas

frutas = ("laranja", "pera", "uva",)    # podemos fazer assim 

frutas = (                                
    "laranja",  
    "pera",        # ou assim, MAS sempre tem que ter , antes do parenteses final
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)       # , antes de fechar o parentese       
print(pais)


#   Como Acessar?

frutas = ("maçã", "laranja", "uva", "pera",)

print(frutas[0])  # maçã
print(frutas[2])  # uva



#   Indices negativos

frutas = (
    "maçã",
    "laranja",
    "uva",
    "pera",
)

print(frutas[-1])  # pera
print(frutas[-3])  # laranja


#   Matriz      - Tuplas Aninhadas -

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])  # (1, "a", 2)
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"



#   Fatiamento  

tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])  # ("t", "h", "o", "n")
print(tupla[:2])  # ("p", "y")
print(tupla[1:3])  # ("y", "t")
print(tupla[0:3:2])  # ("p", "t")
print(tupla[::])  # ("p", "y", "t", "h", "o", "n")
print(tupla[::-1])  # ("n", "o", "h", "t", "y", "p")



#   Interar Tuplas

carros = (
    "gol",
    "celta",
    "palio",
)

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


'''
    Métodos da Classe Tuple
A tupla apresenta poucos métodos, tendo em vista que ela não pode ser alterada

'''

#   Count()

cores = (
    "vermelho",
    "azul",
    "verde",
    "azul",
)

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1



#   Index()

linguagens = ("python", "js", "c", "java", "csharp",)

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0



#   Len()

linguagens = (
    "python",
    "js",
    "c",
    "java",
    "csharp",
)

print(len(linguagens))  # 5