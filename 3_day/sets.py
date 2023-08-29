# Dos maneras de declararlos en Python
my_set = set((1,2,3,4,4,4,5,6)) # Debe encerrarse en una lista o tupla el contenido del metodo set()
my_set2 = {1,2,3,3,3,3,4,4,4,5,5,6,1}
print(my_set)
print(my_set2)
print(type(my_set))
print(type(my_set2))
print(len(my_set2)) # Len o largo
print(2 in my_set2) # Query

# Union de sets
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

# Método Add
s1.add(4)
print(s1)

# Metodo Remove
s1.remove(3) # Si el elemento a eliminar no está en el Set me va a dar un error. Pero podría evitar este error si usara discard en lugar de remove
print(s1) 

# Método Discard
s1.discard(8)
print(s1)

# Método Pop. En una lista elimina el último elemento. Pero como en Sets no hay orden "pop" va a eliminar un elemento aleatorio. Es peligroso. Pero puede servir para un sorteo por ejemplo
sorteo = s1.pop()
print(s1)
print(sorteo)

# Método Clear: limpia nuestro set vaciandolo

# Son inmutables, no tienen orden ni indice
# print(my_set2[1]) no funciona
# Los sets no admiten elementos de tipo lista a su interior. 
# Si va a admitir tuplas a su interior. Dado que un objeto inmutable como un set no puede admitir un objeto mutable a su interior. 

# Ejercicios con Sets: 

"""
Une los siguientes sets en uno solo, llamado mi_set_3:

{1, 2, "tres", "cuatro"}

{"tres", 4, 5}
"""

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5} 
mi_set_3 = mi_set_1.union(mi_set_2)

"""
Elimina un elemento al azar del siguiente set, utilizando métodos de sets.

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
"""

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()

"""
Agrega el nombre Damián al siguiente set, utilizando métodos de sets:

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
"""

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")