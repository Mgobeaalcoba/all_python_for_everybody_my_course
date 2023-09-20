from tkinter import *

class Calculadora:
    def __init__(self, visor: Entry) -> None:
        self.visor = visor

    # Defino función que va ejecutar la lógica mediante la cual debe accionar la calculadora cada vez que oprimimos un boton
    def click_boton(self, caracter):
        self.visor.insert(END, caracter)

    # Defino funcion para el botón de borrar o "B"
    def borrar(self):
        self.visor.delete(0, END)

    # Defino función para obtener resultado de mi calculadora:
    def obtener_resultado(self):
        resultado = str(eval(self.visor.get()))
        self.visor.delete(0, END)
        self.visor.insert(END, resultado)