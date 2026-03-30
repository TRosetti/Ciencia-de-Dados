class Empresa:
    """
    GUIA DE ENCAPSULAMENTO PYTHON
    ----------------------------
    Público:        sem underscore (nome)
    Protegido:      _um underscore (_cnpj) -> "Aviso: evite mexer"
    Privado:        __dois underscores (__ticker) -> Ativa o Name Mangling
    """
    
    ano_atual = 2026

    def __init__(self, nome, ticker, cnpj):
        # 1. ATRIBUTO PRIVADO (O Python vai renomear isso internamente)
        self.__nome = nome
        self.__ticker = ticker
        
        # 2. ATRIBUTO PROTEGIDO (Apenas uma convenção visual)
        self._cnpj = cnpj

    # --- GETTERS E SETTERS (O jeito Pythonico: @property) ---

    @property
    def nome(self):
        """Getter: permite ler o valor como se fosse um atributo comum"""
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        """Setter: permite alterar o valor com validações ou formatação"""
        if len(novo_nome) > 2:
            self.__nome = novo_nome.title()
        else:
            print("Erro: Nome muito curto!")

# --- TESTANDO O COMPORTAMENTO ---

if __name__ == '__main__':
    weg = Empresa("WEG", "WEGE3", "84.429.695/0001-11")

    # A) Acesso via Property (O jeito certo)
    print(f"1. Nome via property: {weg.nome}") 
    weg.nome = "Weg S.A" # Chama o @nome.setter
    print(f"2. Nome alterado: {weg.nome}")

    # B) O erro comum com atributos privados (__)
    # Isso NÃO altera o __nome original, isso CRIA um novo atributo chamado __nome no objeto.
    weg.__nome = "Tentativa Invasiva" 
    
    # C) Provando a "farsa":
    print(f"3. Atributo criado na hora: {weg.__nome}") 
    print(f"4. O original continua guardado: {weg.nome}")

    # D) Acessando o "Privado" à força (Name Mangling)
    # Python renomeia para: _NomeDaClasse__nomeAtributo
    print(f"5. Acessando o privado 'na marra': {weg._Empresa__nome}")

    # E) Acessando o Protegido (_)
    # Funciona normal, mas o VS Code ou PyCharm vão te avisar que não deveria.
    print(f"6. CNPJ (protegido): {weg._cnpj}")