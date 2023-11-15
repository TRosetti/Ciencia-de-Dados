valor_inicial = 1000
taxa_juros = 0.06
periodo = 3

valor_final = valor_inicial

# TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.

def calcular_investimento(valor_inicial, taxa_juros, periodo):
    valor = valor_inicial
    for i in range(periodo):
        valor = valor + (valor * taxa_juros)
    return valor

valor_final = calcular_investimento(valor_inicial, taxa_juros, periodo)

print("%.2f" % round(valor_final, 2)) # Formatação de float 