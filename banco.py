saldo = 0
depositos = []
saques = []

limite_saques = 3
numero_saques = 0

while True:
    print("\n=== MENU ===")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[0] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            depositos.append(valor)
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: R$ "))

        if numero_saques >= limite_saques:
            print("Limite de 3 saques diários atingido.")

        elif valor > 500:
            print("O limite máximo por saque é de R$500.00.")

        elif valor <= 0:
            print("Valor de saque inválido.")

        elif valor > saldo:
            print("Saldo insuficiente.")

        else:
            saldo -= valor
            saques.append(valor)
            numero_saques += 1
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    elif opcao == "3":
        print("\n=== EXTRATO ===")

        if len(depositos) == 0:
            print("Nenhum depósito realizado.")
        else:
            print("DEPÓSITOS:")
            for deposito in depositos:
                print(f"R${deposito:.2f}")

        if len(saques) == 0:
            print("Nenhum saque realizado.")
        else:
            print("SAQUES:")
            for saque in saques:
                print(f"R${saque:.2f}")

        print(f"\nSALDO: R${saldo:.2f}")

    elif opcao == "0":
        print("Obrigado por utilizar nosso sistema!")
        break

    else:
        print("Opção inválida.")
