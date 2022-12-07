## Projeto de Sistema Bancário em Python

menu = """

[d] depósito
[s] saque
[e] extrato
[q] sair

=> """

saldo = 0
limite = 500 
extrato = ""
saques_realizados = 0
LIMITE_SAQUES = 4

while True:
    option = input(menu)

    if option == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Operação falhou. Valor inválido.")

    elif option == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = saques_realizados >= LIMITE_SAQUES

        if excedeu_saldo: 
            print ("Falha! Sem saldo suficiente")
        elif excedeu_limite:
            print ("Falha! Limite de valor para saque excedido")
        elif excedeu_saques:
            print ("Falha! Limite de saques excedido, apenas 4 permitidos")
            
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            saques_realizados += 1
    

        else:
            print("Falha! Valor informado é inválido!")
        
    elif option == "e":
        print ("\n=========== EXTRATO ===========")
        print ("Não foram realizadas operações." if not extrato else extrato)
        print (f"\nSaldo: R$ {saldo:.2f}")
        print ("===============================")
    elif option == "q":
        break
    
    else:
        print ("Opção inválida! Por favor selecione uma operação válida")