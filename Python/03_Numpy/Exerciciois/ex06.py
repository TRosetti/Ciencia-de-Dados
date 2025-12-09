'''
* Exercício 35: Faça um programa que o usuário digite a rentabilidade de ações, com quantas ações o usuário quiser. Transforme essas listas em arrays e devolva pro usuário:

    A média de rentabilidade da carteira.
    O Desvio padrão da carteira.
    A mediana de retornos da carteira.
    O maior retorno.
    O menor retorno.

'''

import numpy as np

continuar = True

array_rentabilidade = np.array([])

while continuar:

    rent = float(input("Digite uma rentabilidade: "))

    array_rentabilidade = np.append(array_rentabilidade, rent)

    deseja_continuar = str(input("Deseja cadastrar mais rentabilidades? [S/N]")).lower()

    if deseja_continuar != "n" and deseja_continuar != "s":

        invalido = True

        while invalido:

            deseja_continuar = str(input("Por favor, digite um comando válido: [S/N]")).lower()

            if deseja_continuar == "n" or deseja_continuar == "s":

                break

    if deseja_continuar == "n":

        break

media = np.mean(array_rentabilidade)
mediana = np.median(array_rentabilidade)
desvio_padrao = np.std(array_rentabilidade)
rent_max = array_rentabilidade.max()
rent_min = array_rentabilidade.min()

media = "{:.0%}".format(media)
mediana = "{:.0%}".format(mediana)
desvio_padrao = "{:.0%}".format(desvio_padrao)
rent_max = "{:.0%}".format(rent_max)
rent_min = "{:.0%}".format(rent_min)

print("")
print("Aqui estão as estatísticas das rentabilidades:")
print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Desvio padrão: {desvio_padrao}")
print(f"Rentabilidade máxima: {rent_max}")
print(f"Rentabilidade mínima: {rent_min}")