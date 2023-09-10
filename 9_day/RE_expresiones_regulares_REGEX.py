# re = regular expresions o REGEX --> Modulo Python para trabajar con ellas es RE
## Ejemplo de patron REGEX para fecha:

patron_fecha = r'\d\d-\d\d-d\d\d\d' # Dos digitos para el día, dos para el mes y 4 digitos para el año. 
patron_telefono = r'\d\d\d-\d\d\d-d\d\d\d' # Patron de un numero de telefono valido.  
patron_fecha = r'\d{2}-\d{2}-\d{4}' # Idem a patron_fecha en su version original.
patron_telefono = r'\d{3}-\d{3}-\d{4}' # Idem a patron_telefono en su version original

"""
Caracteres especiales:

Caracter    Descripción         Ejemplo
\d          Digito numérico     v\d.\d\d
\w          Car alfanumerico    \w\w\w-\w\w
\s          Espacio en blanco   número\s\d\d
\D          NO numerico         \D\D\D\D --> Solo letras. 
\W          NO alfanumerico     \W --> Solo admite signos.
\D          NO esp blanco       \S --> Tiene contenido visible. 

Caracteres cuantificadores

Caracter    Descripción         Ejemplo
+           1 o más veces       código_\d-\d+ ---> Admite código_5-5 ó tmb código _3-3345
{n}         Se repite n veces   Ver ejemplo arriba en patron_fecha o patron_telefono
{n, m}      Se repite entre n y m veces
{n,}        Se repite entre n e infinito
*           Se repite cero o más veces. Puede no aparecer. 
?           El caracter aparece una vez o ninguna. Caso más frecuente: palabra que puede estar en plurarl o en singular

Otras expresiones regex:
[ ] Un set de caracteres. Por ejmplo: [a-z] cualquier letra / [0-9] cualquier numero del 0 al 9
.   Un caracter cualquiera
^   Inicia con
$   Finaliza con
|   operador lógico "O" 

Funciones del modulo RE más importantes:
search(): devuelve un objeto "match" que contiene información acerca del hallazgo si se encuentra en algún punto del string
findall(): devuelve una lista que contiene todos los hallazgos del patrón.
"""

import re

patron = r'\w{4}\d{4}' # Cuatro alfanumericos seguidos de 4 numeros

# Uso de search():
verificar = re.search(patron, "cont1234")

# Uso de findall():
hallazgos = re.findall(patron, "cont1234 - mariano4699 - hola123 - hola1234")
print(f'Verificar tiene {verificar}') # Verificar tiene <re.Match object; span=(0, 8), match='cont1234'>
print(f'hallazgos tiene {hallazgos}') # hallazgos tiene ['cont1234', 'iano4699', 'hola1234']
verificar2 = re.search(patron, "con123")
print(f'Verificar2 tiene {verificar2}') # Verificar2 tiene None

# Reminder: Puedo verificar si un string está dentro de otro sin usar RE de la siguiente forma: 
texto = "Hola, necesitamos ayuda!!!"
palabra = "ayuda"

print(palabra in texto) # True

# Usar findall() para saber cuantas veces se repite y donde se ubica la repetición con finditer():

print(f"El patron {patron} se repite en nuestro texto: {len(hallazgos)} veces!") # El patron \w{4}\d{4} se repite en nuestro texto: 3 veces!

texto = "cont1234 - mariano4699 - hola123 - hola1234"

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())

"""
Posicion de inicio y posición de fin de cada repetición: 
(0, 8)
(14, 22)
(35, 43)
"""

texto = "Hola, necesitamos ayuda!!!"

# Buscar y separar en lista todo lo que no empieze con un espacio vacio o lo que es lo mismo separar una oración por palabras:

buscar = re.findall(r'[^\s]+', texto)
print(buscar) # ['Hola,', 'necesitamos', 'ayuda!!!']
print(" ".join(buscar)) # Hola, necesitamos ayuda!!!  --> Reconstruyo la oración usando el join de la clase String
