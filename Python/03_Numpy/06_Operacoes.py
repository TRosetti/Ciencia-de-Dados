import numpy as np

#todas as operações funcionam com os vetores.

array1 = np.array([1, 1, 1, 1])
array2 = np.array([4, 2, 6, 2])
array3 = np.array([2, 2])

lista_normal = [1, 1, 1, 1]
lista_normal2 = [4, 2, 6, 2]

print(array1 + array2)
print(lista_normal + lista_normal2)



#E se eu quiser somar um número só?

soma_a_todos_os_elementos = np.array([1, 1, 1, 1]) + 20

print(soma_a_todos_os_elementos)


#todas as operações funcionam normal
array1 = np.array([1, 1, 1, 1])
array2 = np.array([4, 2, 6, 2])

subtracao = array1 - array2
divisao = array1/array2
multiplicacao = array1 * array2
exponenciacao = array1 ** array2

print(subtracao)
print(divisao)
print(multiplicacao)
print(exponenciacao)


#Operações dentro do próprio vetor

vetor = np.array([1, 4, -4, -1, 2])

print(vetor)
print(vetor.sum())
print(vetor.max())
print(vetor.min())
print(np.abs(vetor))


#Estatisticas descritivas

vetor = np.array([1, 20, -4, -12, 2000])

media = np.mean(vetor)
mediana = np.median(vetor)
desvio_p = np.std(vetor)
var = np.var(vetor)

print(media) #media
print(mediana) #mediana
print(desvio_p) #desvio padrao
print(var) #variancia

#matriz de correlação 

vetor2 = np.array([5, 4, 3, -5, 4])
vetor3 = np.array([2, 6, 7, -5, 1])

correlacao = np.corrcoef((vetor, vetor2, vetor3))

correlacao