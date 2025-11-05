import numpy as np;

lista = [1, 2, 3, 4, 5]
tupla = (6, 7, 8, 9, 10)

array_from_list = np.array(lista)
array_from_tuple = np.array(tupla)

print(array_from_list)
print()
print(array_from_tuple)


# Usando range para crear arrays

SimpleArray = np.arange(10) # range from 0 to 9
SequencialArray = np.arange(5, 15) # range from 5 to 14
StepArray = np.arange(0, 20, 2) # range from 0 to 18 with step of 2

print()
print(SimpleArray)
print()
print(SequencialArray)
print()
print(StepArray)



# Criando arrays de zeros e uns

ZerosArray = np.zeros((3, 4)) # 3 rows and 4 columns
OnesArray = np.ones((2, 5)) # 2 rows and 5 columns

print()
print(ZerosArray)
print()
print(OnesArray)



# Craindo vetores aleatórios

RandomArray = np.random.rand(3, 2) # 3 rows and 2 columns with random floats between 0 and 1
RandomIntArray = np.random.randint(1, 100, size=(5,)) # 5 random integers between 1 and 99
RandomIntArray2 = np.random.randint(low = 1, high = 10, size = (3,2)) # 3x2 array with random integers between 1 and 9
RandomUniformArray = np.random.uniform(10, 50, size=(3, 3)) # 3x3 array with random floats between 10 and 50

print()
print(RandomArray)
print()
print(RandomIntArray)
print()
print(RandomIntArray2)
print()
print(RandomUniformArray)



# Array bi ou tri dimensionais

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]

array2d = np.array([lista1, lista2]) # 2D array
array3d = np.array([lista1, lista2, lista3]) # 3D array

print()
print(array2d)
print()
print(array3d)



# Matriz

matriz = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print()
print(matriz)


# Lista vs Numpy Array

print()
print(lista1 + lista2) # Concatenation of lists
print()
print(np.array(lista1) + np.array(lista2)) # Element-wise addition of numpy arrays
