import re
import random

class Empresa:
    ano_atual = 2026


    def __init__(self, nome, ticker, ano_criacao, cnpj):
        self.nome = nome    
        self.ticker = ticker
        self.ano_criacao = ano_criacao
        self.cnpj = cnpj
        
    
    def tempo_existencia(self): 
        self.ano_existencia = self.ano_atual - self.ano_criacao
        print(f"A empresa existe há {self.ano_existencia} anos!")
    
    def get_cnpj_limpo(self):
        # return int(self.cnpj.replace('-', '').replace('.', '').replace('/', '').replace(' ', ''))  -- Jeito normal, sem biblioteca 

        return int(re.sub(r'\D', '', self.cnpj)) # Usando a biblioteca re
    

    # Método de classe 
    ## É referente a classe, não a instância (onjeto específico).
    ## Pode ser usado para construir as instâncias, quando não temos todos os dados necessários.
    ## Nesse caso abaixo, para criar uma instância precisamos do ano de criação, mas só temos o quantos anos a empresa tem.
    ## Então criamos um método de classe para calcular e retornar os valores para criação da instância 

    @classmethod
    def extraindo_empresa_por_ano_existencia(cls, anos_existencia, nome, ticker, cnpj):
        ano_criacao = cls.ano_atual - anos_existencia
        return cls(nome, ticker, ano_criacao, cnpj)
    

    @classmethod
    def construindo_instancia_separando_os_dados_ticker(cls, nome, texto_ticker, codigo_ticker, ano_fundacao, cnpj):
        ticker = texto_ticker + str(codigo_ticker)
        return cls(nome, ticker, ano_fundacao, cnpj)
    

    @staticmethod
    def gerar_id():        
        return random.randint(0, 100)

    @staticmethod
    def recomendacao_investimento(ticker):
        lista_recomendacao = ['Comprar', 'Vender', 'Esperar']
        recomendacao = random.choice(lista_recomendacao)
        return f'Para as ações da {ticker} é recomendado {recomendacao}'


if __name__ == '__main__':
    weg = Empresa.extraindo_empresa_por_ano_existencia(nome="WEG", ticker="WEGE3", anos_existencia=62, cnpj='84.429.695/0001-11')
    petro = Empresa.construindo_instancia_separando_os_dados_ticker(nome="Petrobras", texto_ticker="PETR", codigo_ticker=4, ano_fundacao=1953, cnpj='33.000.167/0001-01')

    id_empresa = Empresa.gerar_id()

    print(weg.ano_criacao)
    print(petro.ticker)
    print(petro.gerar_id())
    print(id_empresa)

    empresa_recomendacao = Empresa.recomendacao_investimento("PETR4")

    print(empresa_recomendacao)