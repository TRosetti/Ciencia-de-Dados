# Maiúsculas, minúsculas e títulos

curso = 'pYthOn'

print()
print(curso.upper(), end='\n \n')     # _> PYTHON

print(curso.lower(), end='\n \n')    # _> python

print(curso.title(), end='\n \n')    # _> Python


# Eliminando espaços em branco

curso = '     python '

print()
print(curso.strip())        # _> "python"           , .strip() remove todos os espaços em branco
print() 
print(curso.lstrip())       # _> "python "          , .lstrip() remove todos os espaços em branco da esquerda
print()
print(curso.rstrip())       # _> '     python'      , .rstrip() remove todos os espaços em branco da direita


# Junção e Centralização 

curso = 'Python'

print(curso.center(10, '#'))    # _> "##Python##""

print('.'.join(curso))          # _> "P.y.t.h.o.n"