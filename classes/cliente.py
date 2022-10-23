class Pessoa:
    ListaClientes = []
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None
    
    def inserirconta(self, conta):
        self.conta = conta