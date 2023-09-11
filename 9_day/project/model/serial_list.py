from .numeros_de_series import SerialNumber
import datetime

class SerialList:
    def __init__(self, serial_list: list[SerialNumber]) -> None:
        self.serial_list = serial_list

    def __str__(self) -> str:
        time = 0
        data : str =f"""
----------------------------------------------------
Fecha de búsqueda: [{datetime.date.today()}]

ARCHIVO		NRO. SERIE
-------		----------
"""

        for serial in self.serial_list:
            data += serial.__str__()
            time += serial.search_time
        
        data += f"""
Duración de la búsqueda: {time}
----------------------------------------------------
"""
        return data
    