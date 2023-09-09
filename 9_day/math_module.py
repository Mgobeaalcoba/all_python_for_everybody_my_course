# Math es un modulo integrado en Python con todo lo necesario para hacer matematicas

import math

# Redondear hacia abajo

resultado = math.floor(89.665) # 89
print(resultado)

# Redondear hacia arriba

resultado = math.ceil(89.665) # 90
print(resultado)

# Obtener el valor de "Pi" 

pi = math.pi # 3.141592653589793
print(pi)

# Calcular el logaritmo de un numero y una base

resultado = math.log(100, 5) # El resultado es la respuesta a preguntarse a que numero debería exponer yo el numero 5 (la base) para que el resultado me de 100: 
print(resultado) # 2.8613531161467867

# Tangente, seno, coseno y demás valores trigonometricos:

tangente = math.tan(2565)
seno = math.sin(2565)
coseno = math.cos(2565)

print(tangente) # 9.02100465179493
print(seno) # 0.9939119246611438
print(coseno) # 0.11017752046756596

# También tiene muchisimas cosas más. Todas relacionadas a las matematicas. Numpy puede ser un excelente complemento para trabajar si sos un experto en numeros. 
