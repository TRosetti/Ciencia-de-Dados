import timeit

# Teste Lista x Numpy Array

#  Lista

tempo_list = timeit.timeit('''x = range(1000); y = range(1000); [x[i] + y[i] for i in range(len(x))]''', number=100)

#  Array 
tempo_array = timeit.timeit('''x = np.arange(1000); y = np.arange(1000); x + y''', number=100, setup='import numpy as np')

print(f'Tempo de execução lista: {tempo_list}')
print(f'Tempo de execução array: {tempo_array}')
