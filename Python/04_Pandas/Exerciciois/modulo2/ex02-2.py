#  Crie uma série de cotação randomica (random walk) para os próximos 30 dias de ação, partindo do preç incial e definido pelo usuário. Pressuponha que a média de retornos da ação é zero e seu desvio padrão (volatilidade) é de 1%
import numpy as np
import pandas as pd 

import matplotlib.pyplot as plt

cotacao_inicial = float(input("Digite o preço inicial da ação: "))

periodo_projecao = 30
lista_cotacoes = [cotacao_inicial]
lista_dias = [0]
volatilidade_diaria = 0.01

for i in range(1, periodo_projecao + 1):
    cotacao_seguinte = lista_cotacoes[-1] * (1 + np.random.normal(0, volatilidade_diaria)) 
    lista_cotacoes.append(cotacao_seguinte)
    lista_dias.append(i)

serie_final = pd.Series(lista_cotacoes, index=lista_dias)
print("Série de Cotações para os próximos 30 dias:")
print(serie_final)

serie_final.plot(title="Projeção de Cotação de Ação para os Próximos 30 Dias", xlabel="Dias", ylabel="Cotação")
plt.show()