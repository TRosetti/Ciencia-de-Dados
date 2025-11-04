'''
    Operadores Lógicos

São operadores utilizados em conjunto com os operadores de compareção, para montar uma expressão lógica.
Quando um operador de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar oreadores de comparação com os operadores lógicos, por exemplo:

op_comparacao + op_logico + op_comparação... N...
'''

saldo = 1000
saque = 200
limite = 100

verificacao = saldo >= saque   
print(verificacao)      #   _> True

verificacao = saque <= limite     
print(verificacao)      #   _> False


#   Operador E  ( and ) 
verificacao = ( saldo >= saque and saque <= limite )            # Para retornar True as duas comparações tem que ser verdadeiras, se uma não for vai retornar False
print(verificacao)      #   _> False


#   Operador OU  ( or )
verificacao = ( saldo >= saque or saque <= limite )             # Para retornar True pelo menos uma das duas comparações tem que ser verdadeiras
print(verificacao)      #   _> True


#   Operador Negação  (not)

verificacao = not 1000 > 1500
print(verificacao)      #   _> True

contatos = []        
verificacao = not contatos
print(verificacao)      #   _> True         Array vazio retorna False, como estamos usando not então verificação retorna True

verificacao = not 'thiago'    # Pergunta: A string NÃO está preenchida      _> False
print(verificacao)      #   _> False        String preencida retorna True, como estamos usando not, retorna False 

verificacao = not ''    # Pergunta: A string NÃO está preenchida      _> True
print(verificacao)      #   _> True


#   Parênteses
conta_especial = True

verificacao = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(verificacao)      #   _> True

verificacao = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(verificacao)      #   _> True