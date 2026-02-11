
class Empresa:
    def __init__(self, nome, ticker, ano_criacao, cnpj): # construtor
        self.nome = nome    # atributos
        self.ticker = ticker
        self.ano_criacao = ano_criacao
        self.cnpj = cnpj



if __name__ == '__main__': # Isso faz rodar apenas onde criei a classe (main) para teste, quando utilizo essa função em outro lugar se não tivesse esse if ele apareceria tbm
    weg = Empresa(nome="WEG", ticker="WEGE3", ano_criacao=1960, cnpj='84.429.695/0001-11')
    print(weg.nome)