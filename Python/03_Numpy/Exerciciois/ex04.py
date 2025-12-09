# Faça um programa que gere um vertor de retornos positivos ou negativos entre -1 e 1 na quantidade de dias que o usuário escolher. Devolva um vetor de retrornos posiivos, o priomerio e o último retorno

import numpy as np

dias = int(input("Digite quantos retornos devem ser gerados: "))
retorno_aleatorio = np.random.uniform(-1, 1, dias)
retornos_positivos = retorno_aleatorio[retorno_aleatorio > 0]

print(f'''Os retornos positivos são: {retornos_positivos}
O primeiro retorno é: {retorno_aleatorio[0]}
O último retorno é: {retorno_aleatorio[-1]}''')