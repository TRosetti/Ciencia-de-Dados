import re

class Empresa:
    ano_atual = 2026


    def __init__(self, nome, ticker, ano_criacao, cnpj):
        self.nome = nome    
        self.ticker = ticker
        self.ano_criacao = ano_criacao
        self.cnpj = cnpj
        
    
    def get_cnpj_limpo(self):
        return int(re.sub(r'\D', '', self.cnpj))
    
    @property
    def ano_criacao(self):
        return self._ano_criacao
    
    @ano_criacao.setter
    def ano_criacao(self, ano):
        self._ano_criacao = int(ano)
    

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()



if __name__ == '__main__':
  
    weg = Empresa(nome="WEG", ticker="WEGE3", ano_criacao=1960, cnpj='84.429.695/0001-11')

    print(type(weg.ano_criacao))
    print(f"Valor: {weg.ano_criacao}")

    weg = Empresa(nome="WEG", ticker="WEGE3", ano_criacao="1960", cnpj='84.429.695/0001-11')

    print(type(weg.ano_criacao))
    print(f"Valor: {weg.ano_criacao}")

    print(weg.nome)