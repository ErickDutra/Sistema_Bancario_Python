
menu = """
=========== Bem-Vindo ===========
        Escolha uma opção:
        
        [1] Deposito        
        
        [2] Saque
        
        [3] Extrato
        
        [4] Sair

=================================
"""

texto_numero_de_Saque_excedido = """
=================================
           AVISO

 NÃO FOI POSSIVEL FAZER O SAQUE
    NUMERO DE SAQUE EXCEDIDO


=================================
"""


limite_excedido = """
=================================
           AVISO

 NÃO FOI POSSIVEL FAZER O SAQUE
    LIMITE DE SAQUE EXCEDIDO
    LIMITE : R$ 500,00

=================================
"""

saldo = 400
limite = 500
extrato = []
numero_saque = 0
Limite_saque = 3

print(menu)

while True:

    opcao = int(input("Digite uma opção:"))

    if saldo >= 0:
        if opcao == 1:
            deposito = int(input("Qual valor deseja depositar?"))

            if deposito < 0:
                print("Valor invalido")
            else:
                saldo = deposito + saldo
                extrato.append("Deposito R${:.2f}".format(deposito))

        if opcao == 2:
            saque = int(input("Qual valor deseja Sacar?"))
            numero_saque = numero_saque + 1
            if saque < saldo:
                if numero_saque > Limite_saque:
                    print(texto_numero_de_Saque_excedido)

                elif saque > limite:
                    print(limite_excedido)

                elif saque < 0:
                    print("Valor invalido")

                elif numero_saque < Limite_saque:
                    saldo = saldo - saque
                    extrato.append("Saque R${:.2f}".format(saque))
            else:
                print("Seu Saldo e insuficiente para realizar operação:")

        if opcao == 3:
            print("seu saldo e R$:{:.2f}".format(saldo))
            print(extrato)
        if opcao == 4:
            break
    else:
        print("Seu Saldo e insuficiente!!!")
        print("Obrigado por usar o nosso sistema:")
        break