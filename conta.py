#Orientação a Objetos: implementando o conceito de classe
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print('Construindo objeto ... {}.'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'O saldo da conta {self.__numero} é {self.__saldo}.')

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar): #__ indica que é um método privado
        valor_disponivel_saque = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_saque

    def saca(self, valor):
        if self.pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} ultrapassou o limite.")

    def transfere(self, valor, conta_destino):
        self.saca(valor)
        conta_destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod
    def codigo_banco():
        return "001" #Supondo que o sistema construído é do Banco do Brasil

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
