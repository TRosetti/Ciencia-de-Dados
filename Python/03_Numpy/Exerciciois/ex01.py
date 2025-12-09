#  Peça ao usuário para imputar a cotação de 3 ações e armazene-as em um array NumPy
import numpy as np

acoes = [] 

# for i in range(3):
#     acao = input(f"Digite a cotação da {i + 1}ª ação: ")
#     acoes = np.append(acao)

acao1 = input ("digite a cotação da ação 1: ")
acao2 = input ("digite a cotação da ação 2: ")
acao3 = input ("digite a cotação da ação 3: ")

acoes = np.array([acao1, acao2, acao3])


print(acoes)