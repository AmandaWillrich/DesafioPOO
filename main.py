from classes.conta import ContaPoupanca, ContaCorrente
from classes.banco import Banco
from classes.cliente import Cliente

banco = Banco()

cliente1 = Cliente('Amanda', 27)
cliente2 = Cliente('Cristiane', 26)

conta1 = ContaPoupanca(1111, 24352, 0)
conta2 = ContaCorrente(2222, 24354, 0)

cliente1.inserirconta(conta1)
cliente2.inserirconta(conta2)

banco.inserircliente(cliente1)
banco.inserirconta(conta1)

if banco.autenticacao(cliente1):
    cliente1.conta.deposito(320)
    cliente1.conta.saque(50)
else:
    print('Cliente não autenticado.')

if banco.autenticacao(cliente2):
    cliente2.conta.deposito(200)
    cliente2.conta.saque(300)
else:
    print('Cliente não autenticado.')