import datetime 

mi_hora = datetime.time(12,18,23,1455)

print(mi_hora) # 12:18:23
print(type(mi_hora)) # <class 'datetime.time'>
print(mi_hora.minute)
print(mi_hora.hour)
print(mi_hora.second)
print(mi_hora.microsecond)

mi_dia = datetime.date(2023,9,9)
print(mi_dia) # 2023-09-09
print(mi_dia.year)
print(mi_dia.month)
print(mi_dia.day)
print(mi_dia.ctime()) # Solo la hora pero en este aso no tiene

mi_fecha_y_hora = datetime.datetime(2023,9,9,12,23,14,2500)
print(mi_fecha_y_hora) # 2023-09-09 12:23:14.002500

# Cambiar una parte de mi_fecha_y_hora

mi_fecha_y_hora = mi_fecha_y_hora.replace(month=10)
print(mi_fecha_y_hora) # 2023-10-09 12:23:14.002500

# Calculos de tiempo entre dos fechas

nacimiento = datetime.datetime(1930,6,20)
fallecimiento = datetime.datetime(2016,5,15)

tiempo_de_vida = fallecimiento - nacimiento

print(tiempo_de_vida) # 31376 days, 0:00:00
años_de_vida = tiempo_de_vida.days / 365.25
print(años_de_vida) # 85.90280629705681
print(str(int(años_de_vida)) + " years") # 85 years
