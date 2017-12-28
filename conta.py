#Orientação a Objetos: implementando o conceito de classe
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print('Construindo objeto ... {}.'.format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f'O saldo da conta {self.numero} é {self.saldo}.')

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor
