EXTRATO = []
SALDO = 0
LIMITE = 500
EXCEDE_LIMITE = 0
NUMERO_SAQUES = 0
LIMITE_SAQUES = 3

menu = f"""
.ibank

[d] - Deposito
[s] - Saque
[e] - Extrato

[q] - Encerrar

"""

while True:
    
    opcao = input(menu)

    #SAQUE
    if opcao == "s":
        print("ibank - Saque")
        valor = float(input("Informe o valor do Saque: "))

        excedeu_saldo = valor > SALDO
        excedeu_limite = valor > LIMITE
        excedeu_saques = NUMERO_SAQUES >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            SALDO -= valor
            EXTRATO.append(f"Saque: R$ {valor:.2f}")
            NUMERO_SAQUES += 1
            EXCEDE_LIMITE += valor
            print("Saque - concluido\n")
        
        else:
            print("\nOperação falhou! O valor informado é inválido.\n")

    #DEPOSITO
    elif opcao == "d":
        print("ibank - Depósito")
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            SALDO += valor
            EXTRATO.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito - concluido\n")
        else:
            print("Operação invalida! \nTente novamente\n")

    #EXTRATO
    elif opcao == "e":
        print("\n" + "-"*10 + "EXTRATO" + "-"*10 + "\n")

        if len(EXTRATO) == 0:
            print("Não foram realizadas movimentações.")
        else:
            for i in EXTRATO:
                print(i)

        if SALDO > 0.0:
            print(f"\nSaldo: R$ {SALDO:.2f}\n")
        else:
            print(f"\nSaldo: R$ {SALDO:.2f}\n")
        print("\n" + "-"*27 + "\n")

    #SAIR
    elif opcao == "q":
        break
    else:
        print("Opção inválida, tente novamente!")
