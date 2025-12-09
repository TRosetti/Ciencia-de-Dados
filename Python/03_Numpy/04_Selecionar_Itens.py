import numpy as np

vetor = np.array([1, 3, 4, 6, 7, 8, 10, 21, 30, 43, 50])
print(vetor[0])  # Primeiro elemento
print(vetor[2])  # Terceiro elemento
print(vetor[-1]) # Último elemento
print(vetor[1:4])  # Elementos do segundo ao quarto

vetor2d = np.array([[1, 2, 3], [4, 5, 6]])
print(vetor2d[0, 1])  # Elemento na primeira linha,
print(vetor2d[:, 1])  # Todos os elementos da segunda coluna


# Filtrando elementos 

maior_que_3 = vetor2d[vetor2d > 3]
print(maior_que_3)  # Elementos maiores que 3

somente_pares = vetor[vetor % 2 == 0]
print(somente_pares)  # Elementos pares do vetor

maior_que_3_menor_que_6 = vetor2d[(vetor2d > 3) & (vetor2d < 6)]
print(maior_que_3_menor_que_6)  # Elementos