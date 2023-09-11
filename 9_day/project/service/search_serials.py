from model.numeros_de_series import SerialNumber
from model.serial_list import SerialList
from pathlib import Path
import os
import re
import time


def inicio() -> None:
    # En este caso es un directorio de WSL por lo que va con slash común y no back slash
    my_directory = Path("/home/mgobea/develop/python/python_total/9_day/consigna_proyecto_dia_9/Mi_Gran_Directorio")
    os.chdir(my_directory)
    patron = r'[N]\w{3}[-]\d{5}'
    my_serials_list = regex_identifier(my_directory, patron)
    final_list = construct_serial_list(my_serials_list)
    print(final_list)


def print_hits(hits_list: list[SerialNumber]) -> None:
    for serial in hits_list:
        print(serial)


def regex_identifier(route: Path, patron: str) -> list:
    my_walk = os.walk(route)
    regex_ok_list = []
    
    for carpeta, _, archivo in my_walk:
        for arch in archivo:
            file_route = Path(carpeta) / arch
            content = file_route.read_text()
            init = time.time()
            validation = re.search(patron, content)
            end = time.time()
            processing_time = end - init
            # print(validation.string)
            if validation != None:
                serial = content[validation.start():validation.end()]
                my_serial_object = construct_serials(arch, serial, processing_time)
                regex_ok_list.append(my_serial_object)
    
    return regex_ok_list


def construct_serials(file_found: str, serial_content: str, found_time: float) -> SerialNumber:
    return SerialNumber(file_found, serial_content, found_time)


def construct_serial_list(pre_list: list[SerialNumber]):
    return SerialList(pre_list)


def file_identifier(route: Path) -> list:
    my_walk = os.walk(route)
    file_list = []
    for carpeta, subcarpeta, archivo in my_walk:
        print(f"En la carpeta: {carpeta}")
        print(f"Las subcarpetas son:")
        for sub in subcarpeta:
            print(f"\t{sub}")
        print("Los archivos son:")
        for arch in archivo:
            file_list.append(arch)
            print(f"\t{arch}")
        print("\n")
    return file_list

