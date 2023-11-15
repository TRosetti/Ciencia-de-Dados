'''
    Listas 
     
'''
frutas = ['laranja', 'maça', "uva"]
fruta = []

letras = list('python')
print(letras)               #   _> ['p', 'y', 't', 'h', 'o', 'n']

numeros = list(range(10))
print(numeros)              #   _> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

carro = ['Ferrari', 'F8', 4200000, 2020, 2900, 'São Paulo', True]

'''
    Acesso Direto 
A lista é uma sequência, portanto podemos acessar seus dados utilizando índices. Contamos o índice 
de determinada sequência a partir do zero.

'''
frutas = ['laranja', 'maça', "uva"]
frutas[0]    #   _> laranja
frutas[2]    #   _> uva


''''
    Índices Negativos
Sequências suparta, indexação negativa. A contagem começa em -1

'''
frutas = ['laranja', 'maça', "uva"]
frutas[-1]   #   _> uva
frutas[-3]   #   _> laranja 


'''
    Listas Aninhadas
Listas podem armazenar todos os tipos de objetos Python, portanto
podemos ter lista que armazenam outras listas. Com isso podemos
criar estruturas bidimensionais (tabelas), e acessar informando
os índices de linha e coluna.

'''

matriz = [    
                             # C  
    [1, "a", 2],  # linha    # o      
    ["b", 3, 4],             # l      
    [6, 5, "c"]              # u        
                             # n      
]                            # a  


matriz[0]           # _> [1, "a", 2]
matriz[0][0]        # _> 1
matriz[0][-1]       # _> 2
matriz[-1][-1]      # _> "c"

'''
    Fatiamento
Além de acessar elementos diretamente, podemos extrais um conjunto
de valores de uma sequência. Para isso basta passar o índice inicial
e/ou final para acessar o conjunto. Podemos ainda informar quantas
posições o cursor deve "pular"no acesso.

'''

lista = ['p', 'y', 't', 'h', 'o', 'n']
lista[2:]       # _>  ['t', 'h', 'o', 'n']   
lista[:2]       # _>  ['p', 'y']
lista[1:3]      # _>  ['y', 't']
lista[0:3:2]    # _>  ['p', 't']
lista[::]       # _>  ['p', 'y', 't', 'h', 'o', 'n']
lista[::-1]     # _>  ['n', 'o', 'h', 't', 'y', 'p']

'''
    Iterar Lista
A forma mais comum para percorrer os dados de uma lista é utilizando o comando ( for )

'''
frutas = ['laranja', 'maça', "uva"]

for fruta in frutas:
    print(fruta)    #  _> laranja
                    #  _> maça
                    #  _> uva

'''
    Função Enumerate
Às vezes é necessário saber qual o índice do objeto dentro do laço ( for ). Para isso
podemos usar a função ( enumerate ).

'''
frutas = ['laranja', 'maça', "uva", 'banana', 'melancia']
for indice, fruta in enumerate(frutas):
    print(f'{indice}: {fruta}')     # _>  0: laranja
                                    # _>  1: maça
                                    # _>  2: uva
                                    # _>  3: banana
                                    # _>  4: melancia

'''
    Compreensão de Listas
A compreensão de lista oferece uma sintaxe mais curta quando você deseja: criar
uma nova lista com base nos valores de uma lista existente (filtro) ou gerar
uma nova lista aplicando alguma modificação nos elementos de uma lista existente.
'''


# Filtro versão 1
numeros = [1, 30, 21, 2, 4, 5, 9 ,835, 32]    
pares = [] 

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)        # _> [30, 2, 4, 32]


# Filtro versão 2
numeros = [1, 30, 21, 2, 4, 5, 9 ,82, 10]    
pares2 = [numero for numero in numeros if numero % 2 == 0]      # [retorno(obrigatório) - for(obrigatório) - if(opcional)]
print(pares2)       # _> [30, 2, 4, 82, 10]