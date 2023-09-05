import os
from pathlib import Path


def run():
    init_program : bool = True
    
    while init_program:
        os.system("cls")
        welcome()
        recipes_path : Path = directory_route()
        show_directory(recipes_path)
        total_recipes : int = count_recipes(recipes_path)
        show_count_recepes(total_recipes)
        chosen_option : int = select_option()
        if chosen_option == 6:
            init_program = False
        else:
            if chosen_option == 1:
                return_to_home()
                chosen_category : str = select_category()
                change_directory(chosen_category)
                chosen_recete : str = select_recete(chosen_category)
                print_recete(chosen_recete)
            elif chosen_option == 2:
                return_to_home()
                chosen_category : str = select_category()
                change_directory(chosen_category)
                create_recete(chosen_category)
            elif chosen_option == 3:
                return_to_home()
                create_category()
            elif chosen_option == 4:
                return_to_home()
                chosen_category : str = select_category()
                change_directory(chosen_category)
                chosen_recete : str = select_recete(chosen_category)
                delete_recete(chosen_recete)
            else:
                return_to_home()
                delete_category()


def welcome() -> None:
    print("*******************************")
    print("*    Bienvenido al Programa   *")
    print("*******************************")
    print()


def select_option() -> int():
    print("\nSelecciona una opción:")
    print("[1] - Leer receta ")
    print("[2] - Crear receta ")
    print("[3] - Crear categoría ")
    print("[4] - Eliminar receta ")
    print("[5] - Eliminar categoría ")
    print("[6] - Finalizar programa ")
    option : int = int(input("Ingrese la opción elegida: "))
    while option not in range(1,7):
        print("Seleccionó una opción NO valida... Vuelva a intentarlo. ")
        option : int = int(input("Ingrese la opción elegida: "))
    print()
    return option


def directory_route() -> Path:
    home = Path.home()
    recetas = Path(home, "Documents", "develop","python_total", "6_day", "Recetas")
    return recetas


def return_to_home() -> None:
    home = Path.home()
    recetas = Path(home, "Documents", "develop","python_total", "6_day", "Recetas")
    os.chdir(recetas)


def show_directory(directory) -> None:
    print(f"La ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas es: {directory}. ")
    print()


def count_recipes(directory) -> int:
    count = 0
    for txt in directory.glob("**/*.txt"):
        count += 1 
    return count


def show_count_recepes(count) -> None:
    print(f"En la actualidad contamos con {count} recetas disponibles. ")
    print()


def create_category() -> None:
    current_directory = os.getcwd()
    new_category : str = input("Ingrese el nombre de la nueva categoría que desea crear: ")
    new_path = Path(current_directory, new_category)
    os.makedirs(new_path)

def delete_category() -> None:
    current_directory = Path(os.getcwd())
    categories = os.listdir(current_directory)

    option = select_options("categoria de recetas", categories)

    category_to_delete : Path = Path(current_directory, categories[option - 1])
    os.rmdir(category_to_delete)
    if category_to_delete.exists():
        print("Falló la eliminación del directorio de recetas! Vuelva a intentarlo.")
    else:
        print("Eliminación realizada con exito. ")


def select_category() -> str:
    current_directory = Path(os.getcwd())
    categories = os.listdir(current_directory)

    option = select_options("categoria de recetas", categories)

    return categories[option - 1]


def change_directory(category) -> None:
    current_directory = Path(os.getcwd())
    guia = Path(current_directory, category)
    os.chdir(guia)


def select_recete(category) -> str:
    current_directory = Path(os.getcwd())
    recetes = os.listdir(current_directory)

    option = select_options("receta", recetes)

    return recetes[option - 1]


def print_recete(recete) -> None:
    current_directory = os.getcwd()
    my_file = Path(current_directory, recete)
    content = my_file.read_text()
    print(content)
    input("Presione enter para finalizar el programa. ")


def delete_recete(recete) -> None:
    current_directory = os.getcwd()
    my_file = Path(current_directory, recete)

    if my_file.exists():
        os.remove(my_file)
        print(f"El archivo '{my_file}' ha sido eliminado con éxito.")
    else:
        print(f"El archivo '{my_file}' no existe.")


def create_recete(category) -> None:
    name_recete : str = input("Ingrese el nombre de su nueva receta: ")
    my_file = open(f"{name_recete}.txt", "w")

    lineas_de_texto = []
    print("Ingrese el contenido de su receta. Presione Enter en una línea vacía para finalizar.")

    while True:
        linea = input()
        if not linea:
            break
        lineas_de_texto.append(linea)
    texto_completo = '\n'.join(lineas_de_texto)

    my_file.write(texto_completo)
    my_file.close()


def select_options(option_category, list_options) -> int:

    print(f"Que {option_category} desea seleccionar: ")
    for indice, elemento in enumerate(list_options):
        print(f"[{indice + 1}] - {elemento}")
    option = int(input("Opcion seleccionada: "))
    while option not in range(1,len(list_options)+1):
        print("Seleccionó una opción NO valida... Vuelva a intentarlo. ")
        option = int(input("Opcion seleccionada: "))
    print()

    return option


if __name__ == '__main__':
    run()