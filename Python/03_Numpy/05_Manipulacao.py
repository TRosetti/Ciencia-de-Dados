import numpy as np

# Juntar dois arrays

array1 = np.arange(20, 25) 
array2 = np.arange(15)

array_completo = np.concatenate((array1, array2))
print("Array completo:", array_completo)


# Separar um array em dois

## Separando na metade
array_separado1, array_separado2 = np.split(array_completo, 2)  # Precisamos passar duas variáveis para armazenar os arrays separados 
print("Array separado 1:", array_separado1)
print("Array separado 2:", array_separado2)

## Separando em índices específicos
array_separado3, array_separado4= np.split(array_completo, [5])
print("Array separado 3:", array_separado3)
print("Array separado 4:", array_separado4)


# Colocar novos dados em um array

array_completo = np.append(array_completo, 100)
array_completo = np.insert(array_completo, 1, 2) 
print(array_completo)


# Deletando dados de um array 

array_completo = np.delete(array_completo, -1) #remove o último elemento
print(array_completo)


# Reshap de de arrays

array_reshaped = np.arange(9).reshape(3, 3)
print("Array reshaped:\n", array_reshaped)


# Trocando números dentro de uma condição 

array_inicial = np.array([1,2,3,4,5,6,7,8,9,10,11,22,33,44,55,66,77,88,99])
array_boolean = (array_inicial % 2 == 0)  # Cria um array booleano onde a condição é verdadeira
print(array_boolean)

array_boolean = array_inicial.copy()

array_boolean[array_inicial < 10] = 0  # Cria um array booleano onde a condição é verdadeira
array_boolean[array_inicial >= 10] = 1 
print(array_boolean)



# Ordenação de um array

array_desordenado = np.array([5, 2, 9, 1, 5, 6])
array_ordenado = np.sort(array_desordenado)
print("Array ordenado:", array_ordenado)