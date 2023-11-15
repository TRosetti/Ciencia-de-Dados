'''
    Operadores de Associação

São operadores utilizados para verificar se um objeto está presente em uma sequência.

'''

curso = "Curso de Python"
frutas = ["larenja", "uva", "limão"]
saques = [1500, 700]


#   Está Em ( in )
"Python" in curso  # A string "Python" está presente em curso?     Sim

verificacao = "Python" in curso        
print(verificacao)      #   _> True



200 in saques         # 200 está presente em saque?     Não

verificacao = 200 in saques         
print(verificacao)      #   _> False



#   Não Está Em ( not in )

"maçã" not in frutas         # A string "maçã" não está presente em frutas?     Sim

verificacao = "maçã" not in frutas         
print(verificacao)      #   _> True


