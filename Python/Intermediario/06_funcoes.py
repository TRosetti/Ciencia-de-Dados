'''
    Funções 
Funcão é um bloco de código identificado por um nome e pode 
receber uma lista de parâmetros, esses parâmetros podem ou não 
ter valores padrões. Usar funçõe torna o código mais legível e 
possibilita o reaproveitamento de código. Programar baseado
em funções é o mesmo que dizer que sstamos programando de maneira
estruturada.    
'''

#   Primeira função
def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")



'''
    Retornando Valores
Para retornar um valor, utilizamos a palavra reservada return. Toda
função Python retorna None por padrão. Diferente de outras linguagens
de programação, em Python uma função pode retornar mais de um valor.
'''
def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)



'''
    Argumentos Nomeados
Funções também podem ser chamada usando argumentos nomeados da forma chave=valor
'''
def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) # os ** indica que vai receber um dicionário

'''
    Args e Kwargs
Podemos combinar parâmetros obrigatórios com args e kwargs. Quando
esses são definidos (*args e  **kwargs), o método recebe os valores
como tupla e dicionário respectivamente
'''
# def exibir_poema(data_extenso, *args, **kwargs):
def exibir_poema(data_extenso, *tupla, **dicionario):
    texto = "\n".join(tupla)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema(
    "Quinta-feira, 28 de Setembro 2023",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)