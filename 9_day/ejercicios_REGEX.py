# Ejercicio 1:

"""
Crea una función llamada verificar_email para comprobar si una dirección de email es correcta, que verifique si el email dado como argumento contiene "@" (entre el nombre de usuario y el dominio) y finaliza en ".com" (aunque aceptando también casos que cuentan con un dominio adicional, tal como ".com.br" para el caso de un usuario de Brasil).

Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el mensaje "Ok", pero si detecta que la frase no contiene los elementos indicados, debe informarle al usuario "La dirección de email es incorrecta" imprimiendo el mensaje.
"""

import re

def verificar_email(email):
    patron = r'.{1,15}@\w{1,30}[.]com\W?\w*'
    verificacion = re.search(patron, email)
    if verificacion != None:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")
    
email1 = "mariano_gobea@hotmail.com"
email2 = "gobeamariano@gmail.com.ar"
email3 = "Ohh lala senior frances!!!"
email4 = "usuario@hostcom"
email5 = "usuario@host.com"

verificar_email(email1)
verificar_email(email2)
verificar_email(email3)
verificar_email(email4)
verificar_email(email5)

# Ejercicio 2:

"""
Crea una función llamada verificar_saludo para verificar si una frase entregada como argumento inicia con la palabra "Hola". Si se encuentra el patrón, la función debe finalizar mostrando el mensaje "Ok", pero si detecta que la frase no contiene "Hola", debe informarle al usuario "No has saludado" imprimiendo el mensaje en pantalla.
"""

import re

def verificar_saludo(frase):
    patron = r'^[Hola]'
    verificacion = re.search(patron, frase)
    if verificacion != None:
        print("Ok")
    else:
        print("No has saludado")

# Ejercicio 3:

"""
El código postal de una región determinada se forma a partir de dos caracteres alfanuméricos y cuatro numéricos a continuación (ejemplo: XX1234). Crea una función, llamada verificar_cp para comprobar si el código postal pasado como argumento sigue este patrón. Si el patrón es correcto, mostrar al usuario el mensaje "Ok", de lo contrario: "El código postal ingresado no es correcto".
"""

import re

def verificar_cp(cp):
    patron = r"\w{2}\d{4}"
    verificar = re.search(patron, cp)
    if verificar != None:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")

