'''
    Estruturas de Repetição

São estruturas utilizadas para repetir um trecho de código um determinado números de vezes. Esse 
número pode ser conhecido previamente ou determinado através de uma expressão lógica.

'''

#   Exemplo Sem Repetição
#   -> Receba um número do teclado e exiba o 2 números seguintes

# numero = int(input("Digite um número: "))

# numero += 1
# print(numero)

# numero += 1
# print(numero)


'''
    Comando FOR

O comando for é usado para percorrer um objeto interável. Faz sentido usar (for) quando sabemos o número exato de vezes que que o nossa bloco de código deve ser executado, ou quando queremos percorrer um objeto interável.

'''

texto = input("Digite um texto: ")
VOGAIS = 'AEIOU'
n = 0
for letra in texto:
    if letra.upper() in VOGAIS:
        n += 1
        print(letra, end=" ")
print(n)


''' 
    Função Range

Range é uma função built-in do Python, ela é usada pra produzir uma sequência de números inteiros a partir de um início 
(inclusivo) para um fim (exclusivo). Se usarmos range(i, j) será produzido i, i+1, i+2, ..., j-1.

Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step (opcional).

'''
# range(stop) -> range object
# range(start, stop[, step]) -> range object

for numero in range(0, 11):
    print(numero, end=' ')
else:
    print() #Quebra de linha


# Exibindo a tabuada de 5 

for n in range(0, 51, 5):
    print(n, end=' ')
else:
    print() 


'''
    Comando While

O comando while é usado para repetir um bloco de código vária vezes. Faz sentido usar while quando não sabemos
o número de vezes que nosso bloco de código deve ser executado.

'''

opcao = -1

while opcao != 0:
    opcao = int(input('Informe o número: \n[1] Sacar \n[2] Extrato \n[0] Sair \n'))
    if opcao == 1:
        print('\nSacar \n')
        
    elif opcao == 2:
        print("\nExtrato\n")
    elif opcao == 0:
        print("\nVolte Sempre\n")
    else: 
        print("\nNúmero inválido!\n")


# While TRUE  -> O cógigo vai rodar para sempre, até a condição for quebrada (break),

while True:
    opcao = int(input('Informe o número: \n[1] Sacar \n[2] Extrato \n[0] Sair \n'))
    if opcao == 1:
        print('\nSacar \n')
        
    elif opcao == 2:
        print("\nExtrato\n")
        
    elif opcao == 0:
        print("\nVolte Sempre\n")
        break

    else: 
        print("\nNúmero inválido!\n")

# Temos a opção de usar (continue), ela vai ignorar um certo codigo e continuar 

for numero in range(10):
    if numero == 3:
        continue
    print(numero, end=' ')  # aqui ele ignora o 3 