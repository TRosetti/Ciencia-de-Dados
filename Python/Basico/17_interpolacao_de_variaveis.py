'''
    Interpolação de Variáveis

'''
nome = 'Thiago'
idade = 21
profissao = "Programador"
linguagem = "Python"
pessoa = {"nome": "Thiago", "idade" : 21, "profissao": "Programador", "linguagem": "Python"}

#   Old Style ( % )    ,    %s -> string, %d -> inteiro, %f -> float
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

#    Método Format
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}." .format(nome, idade, profissao, linguagem))
print("Olá, me chamo {2}. Eu tenho {0} anos de idade, trabalho como {3} e estou matriculado no curso de {1}." .format(idade, linguagem, nome, profissao))   # podemos escolher a ordem
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(**pessoa)) 

#   f-string
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}")

#   Formatar string com f-string
PI = 3.14159
print(f"Valor de PI: {PI: .2f}")
print(f"Valor de PI: {PI: 10.3f}")   # antes do . é o width (largura), depois do ponto antes do f é quantidade de numeros depois do ponto