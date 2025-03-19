# Sistema Bancário

saldo = 0
limite = 500
numeros_saque = 0
limites_saque = 3
valorDeposito = 0
valorSaque = 0
saqueTotal = 0
depositoTotal = 0


def Deposito():
    global saldo
    global valorDeposito
    global depositoTotal
    valorDeposito = float(input("Digite o valor do depósito: "))
    if valorDeposito < 0:
        print("Valor inválido! Tente novamente.")
        return
    else:
        print(f"Depósito de R${valorDeposito:.2f} realizado com sucesso!")
        saldo += valorDeposito
        depositoTotal = valorDeposito + valorDeposito
        return depositoTotal


def Saque():
    global saldo
    global numeros_saque
    global valorSaque
    global saqueTotal
    valorSaque = float(input("Digite o valor do saque:"))
    if valorSaque < 0:
        print("Valor inválido! Tente novamente.")
        return
    elif valorSaque > saldo:
        print("Saldo insuficiente.")
        return
    elif numeros_saque >= limites_saque:
        print("Limite de saques diários excedido.")
        return
    else:
        print(f"Saque de R${valorSaque:.2f} realizado com sucesso!")
        saldo -= valorSaque
        numeros_saque += 1
        saqueTotal = valorSaque + valorSaque
        return saqueTotal


def Saldo():
    global saldo
    print(f"Saldo atual: R${saldo:.2f}")
    return saldo


def Extrato():
    global valorDeposito
    global saqueTotal
    if valorDeposito == 0 and saqueTotal == 0:
        print("Não foram realizadas movimentações.")
        return
    else:
        print("---------EXTRATO----------")
        print(f"Depósito: R${depositoTotal:.2f}")
        print(f"Saque: R${saqueTotal:.2f}")
        print("--------------------------")


def Menu():
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Saldo")
    print("4 - Extrato")
    print("5 - Sair")
    escolha = int(input("Digite a opção: "))
    while True:
        if escolha == 1:
            Deposito()
        elif escolha == 2:
            Saque()
        elif escolha == 3:
            Saldo()
        elif escolha == 4:
            Extrato()
        elif escolha == 5:
            print("Sessão encerrada.")
            break
        else:
            print("Opção inválida! Tente novamente.")
        escolha = int(input("Digite a opção: "))


Menu()
