# Peça ao usuário digitar o lucro da Petrobras, Vale e Weg. Mostre os lucros em ordem do maior para o menor. (utilizando arrauys e ferramentas como np.sort, etc)


import numpy as np

empresas = ['Petrobras', 'Vale', 'Weg']
array_lucros = np.array([])

for empresa in empresas:
    lucro = float(input(f'Digite o lucro da {empresa}: '))
    array_lucros = np.append(array_lucros, lucro)

array_lucros = -np.sort(-array_lucros)  # Ordena em ordem decrescente
print("Lucros digitados:", array_lucros)