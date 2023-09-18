from tkinter import * # Importante importar tkinter así y no con un "import tkinter" porque te ahorra mucho código al llamar las clases, constantes, etc.

# Iniciar a tkinter
aplicacion = Tk()

# Tamaño de la ventana y ubicación de la ventana
aplicacion.geometry('1680x1050+0+0') # Va antes del loop dado que sino se mostrará pequeña como viene por default

# Evitar maximizar la pantalla con la app abierta
aplicacion.resizable(0,0)

# Titulo de la ventana:
aplicacion.title("Mi Restaurante - Sistema de Facturación")

# Cambiar el color de fondo de mi aplicación:
aplicacion.config(bg="burlywood")

# Configuramos nuestro panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT) # Opciones de relive: FLAT, RAISED, SUNKEN, GROOVE, RIDGE
panel_superior.pack(side=TOP)

## Etiqueta titulo para el panel superior:
etiqueta_titulo = Label(panel_superior, text="Sistema de Facturación", fg="azure4",
                        font=('Dosis', 58), bg="burlywood", width=27)

## Seteo donde va ubicada mi etiqueta en el panel. Que en este caso es todo lo que va a haber en mi panel superior
etiqueta_titulo.grid(row=0, column=0) 

# Configuramos nuestro panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Configuramos el panel de costos que va dentro del panel izquierdo
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

# Configuramos el panel de comidas"
panel_comidas = LabelFrame(panel_izquierdo, text="Comida", font=("Dosis", 19, 'bold'),
                           bd=1, relief=FLAT, fg="azure4")
panel_comidas.pack(side=LEFT)

# Configuramos el panel de bebidas:
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", font=("Dosis", 19, 'bold'),
                           bd=1, relief=FLAT, fg="azure4")
panel_bebidas.pack(side=LEFT) # Se ubica también a la izquierda pero como ya el anterior estaba a la izquierda entonces este va a ubicarse a un lado

# Configuramos el panel de postres:
panel_postres = LabelFrame(panel_izquierdo, text="Postres", font=("Dosis", 19, 'bold'),
                           bd=1, relief=FLAT, fg="azure4")
panel_postres.pack(side=LEFT) # Se ubica también a la izquierda pero como ya el anterior estaba a la izquierda entonces este va a ubicarse a un lado

# Ahora armamos el panel de la derecha: 
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Configuramos nuestro panel calculadora:
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_calculadora.pack() # Si no colocamos nada por defecto lo ubica en la parte de arriba. 

# Configuramos nuestro panel calculadora:
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_recibo.pack() # Si no colocamos nada por defecto lo ubica en la parte de arriba. En este caso, debajo de la calculadora dado que entró antes al panel 

# Configuramos nuestro panel calculadora:
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_botones.pack() # Si no colocamos nada por defecto lo ubica en la parte de arriba. En este caso, debajo de la calculadora dado que entró antes al panel 




# Necesito que mi ventana Tkinter no se cierre nunca
aplicacion.mainloop() # Hace que nuestra ventana no se cierre. 


