'''
    Estruturas Condicionais 

A estrutura de condicionais permite o desvio de fluxo de controle, quando
determinadas expressões lógicas são atendidas.

'''

# If

saldo = 2000
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print('Saldo insuficiente!')


# If/Else

saldo = 2000
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")


# If/Elif/Else
saldo = 2000.0

opcao = int(input('Informe a opção: \n[1] Sacar  [2] Extrato \n'))

if opcao == 1:
    saque = float(input('Informe o valor do saque:'))
    if saldo >= saque:
        print("Realizando saque!")
    else:
        print("Saldo insuficiente!")

elif opcao == 2:
    print(saldo)
else:
    print("Opção inválida")


# If Ternário 
''' O if ternário permite escrever uma condição em uma única linha. Ele é composto por três partes, a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira é o retorno caso  expressão não seja atendida.

Exemplo:
'''

status = 'Sucesso' if saldo >= saque else 'Falha'   # Se saldo >= a saque for verdadeiro, status = Sucesso, se não for, stauts = Falha

