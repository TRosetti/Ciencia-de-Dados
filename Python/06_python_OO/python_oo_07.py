'''
    Associação 

    Na Associação uma classe usa ou tem outra
'''
class Escritorio:
    """Classe que representa um local físico"""
    def __init__(self, cidade, andar):
        self.cidade = cidade
        self.andar = andar

    def detalhes_local(self):
        return f"Escritório em {self.cidade}, {self.andar}º andar"


class Funcionario:
    """Classe que representa uma pessoa"""
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo
        # Atributo que guardará a ASSOCIAÇÃO
        self._local_de_trabalho = None 

    @property
    def local_de_trabalho(self):
        return self._local_de_trabalho

    @local_de_trabalho.setter
    def local_de_trabalho(self, escritorio_obj):
        """Associa um objeto da classe Escritorio a este funcionário"""
        if isinstance(escritorio_obj, Escritorio):
            self._local_de_trabalho = escritorio_obj
        else:
            print("Erro: Você só pode associar um objeto da classe Escritorio!")

    def onde_trabalho(self):
        if self._local_de_trabalho:
            print(f"{self.nome} trabalha no: {self._local_de_trabalho.detalhes_local()}")
        else:
            print(f"{self.nome} ainda não tem um escritório definido.")


# --- TESTANDO A ASSOCIAÇÃO ---

if __name__ == '__main__':
    # 1. Criamos os objetos de forma independente
    tiago = Funcionario("Tiago", "Desenvolvedor")
    sede_sp = Escritorio("São Paulo", 15)
    filial_rj = Escritorio("Rio de Janeiro", 2)

    # 2. Antes da associação
    tiago.onde_trabalho()

    # 3. Fazendo a ASSOCIAÇÃO (Ligando os dois objetos)
    # O objeto 'tiago' agora contém o objeto 'sede_sp' dentro dele
    tiago.local_de_trabalho = sede_sp
    tiago.onde_trabalho()

    # 4. Mudando a associação dinamicamente
    tiago.local_de_trabalho = filial_rj
    tiago.onde_trabalho()