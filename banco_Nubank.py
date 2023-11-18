from dataclasses import dataclass

@dataclass
class Cliente:
    _nome: str
    _idade: int
    _agencia: int
    _numero_conta: int
    _saldo: float
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    
    @property  
    def agencia(self):
        return self._agencia
        
    @property
    def numero_conta(self):  
        return self._numero_conta
     
    @property
    def saldo(self):
        return self._saldo 
    
    
    @saldo.setter
    def sacar(self, valor):
        self._saldo = self._saldo - valor
        
    @saldo.setter
    def depositar(self, valor):
        self._saldo = self._saldo + valor
    
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"({self.nome} Idade: {self.idade} Agencia: {self.agencia} Numero: {self.numero_conta},Saldo: {self.saldo}')"
        return f"{class_name}{attrs}"


class Banco:
    def __init__(
        self,
        clientes: list[Cliente] | None = None,
    ):
        self.clientes = clientes or []

    def __repr__(self):
        attrs = f"({self.clientes})"
        return f"{attrs}"   

    
     
c1 = Cliente('Erick', 25, 122, 45, 0)
c2 = Cliente('Taiga', 30, 122, 86, 0)
banco = Banco()
banco.clientes.extend([c1, c2])
c1.sacar = 30
c1.depositar = 50
print(c1)




