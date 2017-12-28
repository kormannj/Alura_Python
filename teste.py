#Conta bancária
#No exemplo abaixo encapsulamos as características e ações relativas a "conta" em funções.
#Porém, a ligação das funções abaixo com o objeto "conta" são muito frágeis. Continua sendo possível
#agir sobre a conta sem a necessidade de usar as funções abaixo. Ex: posso dar um comando
# conta = {"numero": 321, "saldo": 200}, ou seja, criar uma conta sem todos os campos.
#Isso vai contra o paradigma OO, que tem por característica forçar que os itens referentes a um
#objeto fiquem agrupados em um único lugar e seja obrigatório o uso dos mesmos.
def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("O saldo da conta {} é {}.".format(conta["numero"], conta["saldo"]))
