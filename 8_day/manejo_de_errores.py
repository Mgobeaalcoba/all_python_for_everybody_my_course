# try, except, else y finally
"""
Es buena práctica capturar y manejar las excepciones posibles
individualmente y brindar información acerca del error y su posible
solución.

except ValueError:

except TypeError:

except FileNotFoundError:
"""

def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    print(n1 + n2)
    print("Gracias por sumar")

# suma() # Si ingreso una palabra arrojará un error

# Para impedirlo debo capturar las excepciones

try:
    # Codigo que queremos probar
    suma()
except:
    # Codigo a ejecutar si hay un error
    print("Algo no ha salido bien")
    suma()
else:
    # Codigo a ejecutar si NO hay un error
    print("Hiciste todo bien")
finally:
    # Codigo que se va ejecutar de todos modos. 
    print("Eso fue todo")


# Tambien podemos capturar las excepciones de forma individual. Buena práctica

try:
    suma()
except TypeError:
    print("Estás intentando concatenar tipos distintos. ")
except ValueError:
    print("Ese no es un numero! ")
else:
    print("Hiciste todo bien")
finally:
    print("Eso fue todo!")

# 1° forma de manejar el ingreso equivocado de un tipo de dato usando try/except:

def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un numero: "))
        except ValueError:
            print("Ese no es es un numero! ")
        else:
            print(f"Ingresaste el numero {numero} ")
            break
    return numero

