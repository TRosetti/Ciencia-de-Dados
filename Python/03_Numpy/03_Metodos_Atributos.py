import numpy as np

array = np.arange(10)
print('\n----- ----- ----- -----\n')
print(array)
print(array.nbytes) # Tamanho em bytes do array
print(array.itemsize) # Tamanho em bytes de cada elemento do array


print('\n----- ----- ----- -----\n')

## Numero de dimensões e forma do array
array2d = np.array([[1, 2, 3], [4, 5, 6]])

print(array2d)
print(array2d.ndim) # Número de dimensões do array
print(array2d.shape) # Forma do array (linhas, colunas)
print(array2d.size) # Número total de elementos no array

print('\n----- ----- ----- -----\n')



