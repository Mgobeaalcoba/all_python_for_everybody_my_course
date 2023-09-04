# Ejercicio 1

from pathlib import Path 

ruta_base = Path.home()
print(ruta_base)

# Ejercicio 2

from pathlib import Path 

ruta = Path("Curso Python",
"Día 6",
"practicas_path.py")

print(ruta)

# Ejercicio 3

from pathlib import Path 

home = Path.home()
guia = Path(
"Curso Python",
"Día 6",
"practicas_path.py"
)
ruta = Path(home, guia)

print(ruta)