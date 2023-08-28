# Ya conocemos Format e Index. Veamos 6 más:
# upper, lower, split, join, find y replace

texto = "Este es el resultado"
upper_text = texto.upper()
print(upper_text)
lower_text = upper_text.lower()
print(lower_text)
print(lower_text.capitalize())

split_text_to_list = texto.split() # Separa en listas / Si necesito separar por algo distinto a espacios vacios debo pasarlo como primer parametro. Ej "-" o "_" o "/" o "e"
print(split_text_to_list)

a = "Aprender"
b = "Python"
c = "es"
d = "genial."
e = " ".join([a,b,c,d]) # Para unir elementos en un join deben estar dentro de una lista. 
print(e)

# find es exactamente igual que el método index. Busca un caracter en mi string. Con la diferencia de que si no lo encuentra no devuelve error. 
resultado = texto.find("g") # Si no lo encuentra devuelve "-1"
print(resultado)

# replace
texto = "Este es el texto de Mariano"
print(texto)
resultado = texto.replace("Mariano", "Gobea")
print(resultado)