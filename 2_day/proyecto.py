def calculate_comision(total, share):
    return total * share


def run():
    name = input("¿Cual es su nombre? ")
    sales = float(input("¿Cuanto has vendido en este mes (expresado en dinero)? "))
    comision_rate = 0.13
    comision = calculate_comision(sales, comision_rate)
    print(f'Hola {name}. Bienvenido! Sus comisiones por el momento son de ${comision}. Que sigas bien!')


if __name__ == '__main__':
    run()