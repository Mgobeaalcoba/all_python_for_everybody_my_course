# Envío de multiples e indefinidos argumentos a una función a traves de un diccionario: 

def suma(**kwargs):
    print(type(kwargs))
    print(kwargs)
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print(suma(x=3, y=5, z=2)) # Lo que enviamos no es un diccionario. Sino pares clave valor que se transforman en diccioanarios al pasar como **kwargs


def prueba(num1, num2, *args, **kwargs):
    print(f"el primer valor es {num1}")
    print(f"el primer valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

# prueba(15,50,100,200,300,400,x="uno",y="dos",z="tres")

# Desempacado de valores para enviar como args o kwargs

args = [100,200,300,400]
kwargs = {
    "x":"uno",
    "y":"dos",
    "z":"tres"
}

prueba(15,50,*args,**kwargs)


# Ejercicios

def cantidad_atributos(**kwargs):
    parametros = 0
    for clave in kwargs.keys():
        parametros += 1
    return parametros


def lista_atributos(**kwargs):
    my_list = []
    for valor in kwargs.values():
        my_list.append(valor)
    return my_list


def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for nombre_argumento, valor_argumento in kwargs.items():
        print(f"{nombre_argumento}: {valor_argumento}")
        
describir_persona("María", color_ojos="azules", color_pelo="rubio")