import time

Visual_Inicio_Sistema = """
==============================

          Bem-Vindo
             ao
         Banco Python 

==============================
[1] Iniciar 

[0] Sair
==============================
"""

Menu_Principal = """
==============================
    Menu Principal
==============================
[1]Fazer Login

[2]Cadastrar Usuario

[0]Cancelar operação"
==============================
"""

Visual_Login = """
==============================
    Login
==============================

Informe seu ID:

==============================
"""

visual_Cadastro = """
==============================
        Cadastro:
==============================
[1]Cadastrar.

[0]Cancelar.
==============================
"""

visual_login = """
==============================
        Login:
==============================
[1]Iniciar login 

[0]Canecelar
==============================
"""

visual_Conta = """
==============================
    Escolha uma operação:
==============================
[1]Saque.

[2]Deposito.

[3]Extrato.

[0]Sair.
==============================
"""

def tempo():
    print("Carregando.")
    time.sleep(1)
    print("Carregando..")
    time.sleep(1)
    print("Carregando...")
    time.sleep(1)

def deposito(Valor_Deposito):
    if Valor_Deposito < 0:
        return print("Valor invalido")
    else:
        return saldo_Cliente + Valor_Deposito

def saque(Valor_Saque):

    if Valor_Saque < saldo_Cliente:
        if numero_saque > Limite_saque:
            print("saque excedido")

        elif Valor_Saque > limite:
            print("limite excedido")

        elif Valor_Saque < 0:
            print("Valor invalido")

        elif numero_saque < Limite_saque:
            return saldo_Cliente - Valor_Saque
    else:
        print("Seu Saldo e insuficiente para realizar operação:")

def extrato():
        return print("seu saldo e R$:{:.2f}".format(saldo_Cliente))

def cadastro(nome,data_nascimento,cpf,endereco):
    usuario_cadastrando.append(nome)
    usuario_cadastrando.append(data_nascimento)
    usuario_cadastrando.append(cpf)
    usuario_cadastrando.append(endereco)
    usuario_cadastrando.append(0)

id = 0
usuarios_do_banco = []
usuario_cadastrando = []
quantidade_lista = len(usuarios_do_banco)
while True:
    sistema_banco = int(input(Visual_Inicio_Sistema))
    tempo()
    if sistema_banco == 1:
        while True:
            menu = (int(input(Menu_Principal)))
            x = 0

            if menu == 1:
                menu_login = 3
                x = 9
                navegar = input(Visual_Login)
                break
            elif menu == 2:
                menu_cadastro = 4
                x = 8
                break
            elif menu == 0:
                x = 0
                break

        # cadastro do usuario #
        x_cadastro = 0
        while x == 8 and x_cadastro == 0:
            tempo()
            x = int(input(visual_Cadastro))
            if x == 1:
                while True:
                    x_nome = input("Nome Completo:")
                    x_data = input("Data de Nascimento:")
                    x_cpf = input("CPF:")
                    if (x_cpf in usuario_cadastrando) == True:
                        print("não foi possivel fazer o cadastro!!")
                        break
                    x_endereco = input("Endereço:")
                    cadastro(x_nome, x_data, x_cpf, x_endereco)
                    print(f"Seu ID:{id}")
                    id += 1
                    usuarios_do_banco.append(id)
                    usuarios_do_banco.append(usuario_cadastrando)
                    x = 9
                    break
            elif x == 0:
                break

        quantidade_lista = len(usuarios_do_banco)

        # login #
        x_login = 0
        while x == 9 and x_login == 0:
            tempo()
            x_login = int(input(visual_login))
            if int(quantidade_lista) == 0:
                print("não possui usuarios cadastrados")
                break
            elif x_login ==1:
                selecao_id_usuario = int(input("Digite seu ID:"))
                posicao_id = (usuarios_do_banco[selecao_id_usuario + 1])
                print("Login Efetuado!!")
                break

        if int(quantidade_lista ) != 0:
            saldo_Cliente = usuarios_do_banco[selecao_id_usuario + 1][4]
        else:
            saldo_Cliente = 0

        limite = 500
        numero_saque = 0
        Limite_saque = 3
        extrato = []
        # menu principal saque, deposito, extrato #

        x_menu = 0
        while x != 0 or x_menu != 0:
            tempo()
            x_menu = int(input(visual_Conta))
            if x_menu == 1:
                Valor_Saque = saque(int(input("Qual Valor deseja sacar?")))
                saque_cliente = saldo_Cliente - Valor_Saque
                usuarios_do_banco[selecao_id_usuario + 1][4] = saque_cliente
                extrato.append("Saque R${:.2f}".format(Valor_Saque))

            elif x_menu == 2:
                Valor_Deposito = deposito(int(input("Qual Valor deseja Depositar?")))
                deposito_cliente = saldo_Cliente + Valor_Deposito
                usuarios_do_banco[selecao_id_usuario + 1][4] = deposito_cliente
                extrato.append("Deposito R${:.2f}".format(Valor_Deposito))

            elif x_menu == 3:
                print("seu saldo e R$:{:.2f}".format(saldo_Cliente))
                print(extrato)
            elif x_menu == 0:
                break

    elif sistema_banco == 0:
        break

print(usuarios_do_banco)