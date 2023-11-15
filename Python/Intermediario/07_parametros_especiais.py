'''
    Parâmetros Especiais
Por padrão, argumentos podem ser passados para uma função Python 
tanto por posição quanto explicitamente pelo nome.
Para uma melhor legibilidade e desempenho, faz sentido restringir
a maneira pelo qual argumentos possam ser passados, assim um
desenvolvedor precesa apenas olhar para a definição da função
para determinar se os itens são passados.
'''

#   Positional Only

#               ( Positional only   / Positional or keyword)
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

#               ( Positional         /     keyword)
criar_carro("Palio", 1999, "ABC-1234",  marca="Fiat", motor="1.0", combustivel="Gasolina")

# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido



#   Keyword Only    -> Começa com *, pós ele todo precisam de chave  

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido


#  Keyword and Position only

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido



'''
    Objetos de Primeira Classe
Em Python tudo é objeto, dessa forma funções também são objetos 
o que as tornam objetos de primeira classe. Com isso podemos
atribuir funções a variáveis, passá-las com parâmetro para 
funções, usá-la com valores em estruturas de dados(lista , tuplas
dicionários, etc) e usar valores de retorno para uma função(closures)
'''

def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20


'''
    Escopo Local e Escopo Global
Python trabalha com escopo local e global, dentro do bloco da função
o escopo é local. Portanto alterações ali feitas em objetos 
imutáveis serão perdidas quando o método terminar de ser executado. 
Para usar objetos globais utilizamos a palavra-chave global, que 
informa ao interpretador que a variável que está sendo manipulada 
no escopo local é global.
Essa NÃO é uma boa prática e deve ser evitada
'''

salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario



print(salario_bonus(500)) # 2500
