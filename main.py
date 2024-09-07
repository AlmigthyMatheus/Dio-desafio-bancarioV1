menu = """

[d] Depositar 
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Insira o valor a ser depositado\n"))
        if deposito > 0:
            saldo += deposito
            extrato += f"\nValor depositado: R$ {deposito:.2f}"
            print("Deposito efetuado com sucesso!\n")
            print(f"Saldo atual: R$ {saldo:.2f}\n")
        else:
            print("Operação falhou! O valor informado é inválido")
    elif opcao == "s":
        saque = float(input("Insira o valor que deseja sacar"))
        if (saque <= limite
            and saque <= saldo
                and numero_saques < LIMITE_SAQUES):
            numero_saques += 1
            saldo -= saque
            extrato += f"\nValor sacado: R$ {saque:.2f}"
            print("Saque efetuado com sucesso!")
            print(f"Saldo atual: R$ {saldo:.2f}\n")
        else:
            print("Sinto muito! Você não atende os requisitos para sacar.")
    elif opcao == "e":
        if extrato:
            print(extrato)
        else:
            print("Nenhuma transação realizada")
    elif opcao == "q":
        break
