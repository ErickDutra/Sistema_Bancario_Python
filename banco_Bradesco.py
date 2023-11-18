import abc
from dataclasses import dataclass


@dataclass
class Conta(abc.ABC):
    agencia: int
    conta: int
    saldo: float

    @abc.abstractmethod
    def sacar(self):
        ...

    def depositar(self, valor):
        self.saldo += valor


class Corrente(Conta):
    def sacar(self, valor):
        saldo_corrente = self.saldo
        saldo_corrente = self.saldo - valor
        if saldo_corrente >= (-100):
            self.saldo = saldo_corrente
            return self.saldo
        else:
            print(f"Ultapassou limite de saque:{-100}")
            return self.saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"({self.agencia},{self.conta},{self.saldo})"
        return f"{class_name}{attrs}"


class Poupanca(Conta):
    def sacar(self, valor):
        saldo_poupanca = self.saldo
        saldo_poupanca -= valor
        if saldo_poupanca >= (0):
            self.saldo = saldo_poupanca
            return self.saldo
        else:
            print(f"Ultapassou limite de saque:{0}")
            return self.saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"({self.agencia},{self.conta},{self.saldo})"
        return f"{class_name}{attrs}"


@dataclass
class Pessoa(abc.ABC):
    nome: str
    idade: int


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta: Conta | None


class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[Pessoa] | None = None,
        contas: list[Conta] | None = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def checar(self, cliente, conta):
        validar = False
        while True:
            if conta is cliente.conta:
                validar = True
            else:
                validar = False
                print("Cliente não Passou na checagem")
                return validar
            if conta.agencia in self.agencias:
                validar = True
            else:
                validar = False
                print("Cliente não Passou na checagem")
                return validar

            if cliente in self.clientes:
                validar = True
            else:
                validar = False
                print("Cliente não Passou na checagem")
                return validar

            if conta in self.contas:
                validar = True
                return validar
            else:
                validar = False
                print("Cliente não Passou na checagem")
                return validar

    def __repr__(self):
        attrs = f"({self.agencias},{self.clientes},{self.contas})"
        return f"{attrs}"


c1 = Cliente("Erick", 25)
corrente_c1 = Corrente(111, 122, 0)
c1.conta = corrente_c1

c2 = Cliente("Joao", 25)
corrente_c2 = Corrente(112, 122, 0)
c2.conta = corrente_c2

banco = Banco()
banco.clientes.extend([c1, c2])
banco.contas.extend([corrente_c1, corrente_c2])
banco.agencias.extend([112, 111])
print(banco)
validar = banco.checar(c2, corrente_c2)
print(validar)

if validar:
    corrente_c2.depositar(30)
    print(c2.conta)
