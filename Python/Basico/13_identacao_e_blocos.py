'''
    Identação e Blocos

-> Forma de mater o código fonte mais legível e manutenível.
-> Através da identação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

'''

#     Utilizando Espaços

# Existe uma convenção em Python,, que define as boas práticas para escrita de código na linguagem. Nesse documento é 
# indicado utilizar 4 espaços em branco, tab serve tbm, por nível de identação, ou seja, a cada novo bloco adicionamos 4 novos espaços
# em branco.  Exemplo:

def sacar(self, valor: float) -> None:  # início do bloco do método

    if self.saldo >= valor:      # início do bloco do if
        
        self.saldo -= valor

    # fim do bloco do if

# fim do bloco do método



def sacar(valor):
    saldo = 500

    if saldo >= valor: 
        print(f'Seu saque é de {valor} reais')
        print('Retire o seu dinheiro.')
    print("Obrigo, volte sempre!")


sacar(100)