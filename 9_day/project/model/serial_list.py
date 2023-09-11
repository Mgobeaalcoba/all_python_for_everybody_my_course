from .numeros_de_series import SerialNumber
import datetime
import math

class SerialList:
    def __init__(self, serial_list: list[SerialNumber]) -> None:
        self.serial_list = serial_list

    def __str__(self) -> str:
        today = datetime.date.today()
        time = 0
        data : str =f"""
----------------------------------------------------
Fecha de búsqueda: [{today.day}/{today.month}/{today.year}]

ARCHIVO		NRO. SERIE	TIEMPO BUSQUEDA
-------		----------	---------------
"""

        for serial in self.serial_list:
            data += serial.__str__()
            time += serial.search_time
        
        data += f"""
Duración de la búsqueda: {math.ceil(time)} Segundo.
----------------------------------------------------
"""
        return data
    