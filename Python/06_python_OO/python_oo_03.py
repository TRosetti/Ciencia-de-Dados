from datetime import datetime
import re
class Empresa:
    def __init__(self, nome, ticker, ano_criacao, cnpj):
        self.nome = nome    
        self.ticker = ticker
        self.ano_criacao = ano_criacao
        self.cnpj = cnpj
        self.ano_atual = datetime.now().year
    
    def tempo_existencia(self): 
        self.ano_existencia = self.ano_atual - self.ano_criacao
        print(f"A empresa existe há {self.ano_existencia} anos!")
    
    def get_cnpj_limpo(self):
        # return int(self.cnpj.replace('-', '').replace('.', '').replace('/', '').replace(' ', ''))  -- Jeito normal, sem biblioteca 

        return int(re.sub(r'\D', '', self.cnpj)) # Usando a biblioteca re
    
if __name__ == '__main__':
    weg = Empresa(nome="WEG", ticker="WEGE3", ano_criacao=1960, cnpj='84.429.695/0001-11')
    weg.tempo_existencia()

    print(f"O CNPJ da {weg.nome} é {weg.get_cnpj_limpo()}")
    print(weg.ano_existencia)