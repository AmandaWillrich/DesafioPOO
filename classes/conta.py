from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numeroconta, saldo, tipo):
        self.__agencia = agencia
        self.__numeroconta = numeroconta
        self.__saldo = saldo
        self.__tipo = tipo

    @property
    def agencia(self):
        return self.__agencia

    @property
    def numeroconta(self):
        return self.__numeroconta

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def tipo(self):
        return self.__tipo


    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do Saldo precisa ser numérico.")

        self.__saldo = valor

    def deposito(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do Depósito precisa ser numérico.")
        
        self.__saldo += valor
        self.detalhes()
        

    def detalhes(self):
        print(f'\nAgência: {self.agencia}', end=' ')
        print(f'Conta: {self.numeroconta}', end=' ')
        print(f'Saldo: R${self.saldo}', end=' ')
        print(f'Tipo de Conta: {self.tipo}', end=' ')
   
   
    @abstractmethod
    def saque(self, valor):
        pass

class ContaPoupanca(Conta):
    def __init__(self, agencia, numeroconta, saldo, tipo='Conta Poupança'):
        super().__init__(agencia, numeroconta, saldo, tipo)

    def saque(self, valor):
        if self.saldo < valor:
            print('Saldo Insuficiente.')
            return
        
        self.saldo -= valor
        self.detalhes()

class ContaCorrente(Conta):

    def __init__(self, agencia, numeroconta, saldo, tipo='Conta Corrente', limite=200):
        super().__init__(agencia, numeroconta, saldo, tipo)
        self.__limite = limite

        @property
        def limite(self):
            return self.__limite

    def saque(self, valor):
        if (self.saldo + self.__limite) < valor:
            print('Saldo Insuficiente.')
            return

       
        self.saldo -= valor
        self.detalhes()