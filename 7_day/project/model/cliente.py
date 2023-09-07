from .persona import Persona

class Cliente(Persona):
    def __init__(self, nombre: str, apellido: str, num_cuenta: int, balance: int) -> None:
        super().__init__(nombre,apellido)
        self.num_cuenta = num_cuenta
        self.balance = balance

    def __str__(self):
        return (f"""

Datos del cliente:
nombre : {self.nombre}
apellido: {self.apellido}
numero de cuenta : {self.num_cuenta}
balance: {self.balance}

""")
    
    def depositar(self, monto: int):
        self.balance += monto 

    def retirar(self, monto: int):
        if (self.balance - monto) < 0:
            print("No es posible retirar ese monto dado que su saldo es insuficiente. ")
            input()
        else:
            self.balance -= monto
        