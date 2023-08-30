print(list(enumerate("Hola")))

# [(0, 'H'), (1, 'o'), (2, 'l'), (3, 'a')]

for indice, numero in enumerate([5.55, 6, 7.50]):
    print(indice, numero)

lista = ['a','b','c']

print(enumerate(lista)) # Si no lo convierto a lista no lo puedo usar. 

mis_tuples = list(enumerate(lista))
print(mis_tuples)

"""
Imprime en pantalla frases como la siguiente:

'{nombre} se encuentra en el índice {indice}'

Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el índice, obtenido mediante enumerate().

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

Puedes modificar la línea print() otorgada como ejemplo, pero las frases entregadas deberán ser iguales.

Tip: utiliza loops!
"""

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

"""
Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() los índices de cada caracter del string "Python".

Llama a la lista obtenida con el nombre de variable lista_indices .
"""

my_string = "Python"
lista_indices = list(enumerate(my_string))

"""
Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

Puedes resolverlo de diferentes maneras, pero servirá que tengas presente todos o algunos de los siguientes elementos:

Loops

Condicionales if

El método enumerate()

Métodos de strings o indexado
"""

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(indice)

