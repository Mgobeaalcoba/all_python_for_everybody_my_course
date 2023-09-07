from model.cliente import Cliente
from random import randint
import os


def inicio():
    os.system("cls")
    mi_cliente = crear_cliente()
    exit : bool = False
    while not exit:
        os.system("cls")
        choicen_option : int = int(input(
            f"""
Bienvenido!
{mi_cliente}
¿Que desesa realizar?
[1] - Depositar
[2] - Retirar
[3] - Salir del programa

"""
        ))
        if choicen_option == 1:
            monto : int = int(input("Ingrese el importe a depositar: "))
            mi_cliente.depositar(monto)
        elif choicen_option == 2:
            monto : int = int(input("Ingrese el importe a retirar: "))
            mi_cliente.retirar(monto)
        else:
            exit = True


def crear_cliente() -> Cliente:
    nombre : str = input("Ingrese su nombre: ")
    apellido : str = input("Ingrese su apellido: ")
    num_cuenta : int = randint(100000,999999)
    balance : int = 0
    return Cliente(nombre, apellido, num_cuenta, balance)
