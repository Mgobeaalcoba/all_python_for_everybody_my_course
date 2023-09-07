from model.turnero import Turnero
from os import system


def inicio():
    system("cls")
    apagar_turnero = False
    area_perfumeria = Turnero("Margaritas", "Perfumeria")
    mi_generador_perfumeria = area_perfumeria.generar_turno()
    mi_generador_decorado_perfumeria = decorar_turno(generar_turno_function, area_perfumeria.area)
    area_farmacia = Turnero("Margaritas", "Farmacia")
    mi_generador_farmacia = area_farmacia.generar_turno()
    mi_generador_decorado_farmacia = decorar_turno(generar_turno_function, area_farmacia.area)
    area_cosmetica = Turnero("Margaritas", "Cosmetica")
    mi_generador_cosmetica = area_cosmetica.generar_turno()
    mi_generador_decorado_cosmetica = decorar_turno(generar_turno_function, area_cosmetica.area)
    while not apagar_turnero:
        system("cls")
        print("*******************************")
        print("*    Bienvenido al Turnero   *")
        print("*******************************")
        print()
        print("[1] - Perfumeria")
        print("[2] - Farmacia")
        print("[3] - Cosmetica")
        print("[0] - Apagar turnero")
        area = int(input("A que area desea dirigirse: "))
        
        if area == 1:
            mi_generador_decorado_perfumeria(mi_generador_perfumeria)
            input()
        elif area == 2:
            mi_generador_decorado_farmacia(mi_generador_farmacia)
            input()
        elif area == 3:
            mi_generador_decorado_cosmetica(mi_generador_cosmetica)
            input()
        else:
            apagar_turnero = True


def decorar_turno(funcion, area):
    def internal_function(turnero):
        if area == "Perfumeria":
            print(f"Su turno es P-{funcion(turnero)}")
            print("Aguarde y sera atendido.")
        elif area == "Farmacia":
            print(f"Su turno es F-{funcion(turnero)}")
            print("Aguarde y sera atendido.")
        elif area == "Cosmetica": 
            print(f"Su turno es P-{funcion(turnero)}")
            print("Aguarde y sera atendido.")
    return internal_function


def generar_turno_function(mi_generador) -> int:
    return next(mi_generador)
