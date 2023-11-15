#   Convertendo Tipos
#   -> Em alguns momentos podemos precisar converter algum tipo de varivel
#   -> Se tiver alguma variavel do tipo string armazenando um número e precisamos usa-lo em alguma operação matemática



#   Inteiro para Float

preco = 10
print(preco)               # 10     _> Int

preco = float(preco)   
print(preco)               # 10.0   _> Float

preco = 10 / 2
print(preco)               # 5.0    _> Float  


#   Float para Inteiro

preco = 10.30
print(preco)               # 10.3   _> Flaot

preco = int(preco)
print(preco)               # 10     _> Int
print(type(preco))


#   Conversão por Divisão

preco = 10
print(preco)               # 10     _> Int

print(preco / 2)           # 10.0   _> Float

print(preco // 2)          # 10.0   _> Int


#   Número para String

preco = 10.5
idade = 21

print(str(preco))          # 10.5     _> Str

print(str(idade))          # 21       _> Str

texto = f"idade {idade} preco {preco}"

print(texto)               # idade 10.5 preco 21    _> Str


#   String para Número 

preco = '10.50'            # 10.5     _> Str
idade = "21"               # 21       _> Str

print(preco)
print(float(preco))        # 10.5     _> Float

idade = int(idade)  
print(idade)          # 21       _> Int

print(type(idade))