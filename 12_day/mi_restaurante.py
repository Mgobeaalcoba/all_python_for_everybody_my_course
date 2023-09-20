from tkinter import * # Importante importar tkinter así y no con un "import tkinter" porque te ahorra mucho código al llamar las clases, constantes, etc.

# Iniciar a tkinter
aplicacion = Tk()

# Tamaño de la ventana y ubicación de la ventana
aplicacion.geometry('1250x630+0+0') # Va antes del loop dado que sino se mostrará pequeña como viene por default

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
                        font=('Dosis', 48), bg="burlywood", width=27)

## Seteo donde va ubicada mi etiqueta en el panel. Que en este caso es todo lo que va a haber en mi panel superior
etiqueta_titulo.grid(row=0, column=0) 

# Configuramos nuestro panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Configuramos el panel de costos que va dentro del panel izquierdo
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg="azure4", padx=110)
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

# Nueva sección: Cechkbuttons!!! y Cuadros de entrada!!!

# Empezemos ahora a poner dentro de nuestra estructura elementos que podamos ver como lista de comidas, bebidas, etc.
lista_comidas = ["pollo", "cordero", "salmon", "merluza", "kebab", "pizza", "empanadas", "sushi"]
lista_bebidas = ["agua", "soda", "jugo", "cola", "vino", "cerveza", "coctails", "lima-limon"]
lista_postres = ["helado", "flan", "brownies", "fruta", "mousse", "pastel", "panqueques", "bombon"]

## Generar items de comidas
variables_comida = []
cuadros_comida = []
texto_comida = []

contador = 0

for comida in lista_comidas:

    ## Crear checkbuttons
    variables_comida.append('')
    variables_comida[contador] = IntVar() # Creo la variable que va a contener la selección o selecciones de nuestro check button
    comida = Checkbutton(panel_comidas, 
                         text=comida.title(), 
                         font=("Dosis", 19, "bold"),
                         onvalue=1, 
                         offvalue=0, 
                         variable=variables_comida[contador]) # Onvalue y Offvalue significa el valor que va a tener la casilla cuando esté activada y offvalue lo contrario
    comida.grid(row=contador, 
                column=0, 
                sticky=W) # sticky=W significa que quiero un encolumnado del lado izquierdo de la pantalla

    ## Crear los cuadros de entrada
    cuadros_comida.append("")
    texto_comida.append("")
    # Valores por defecto para los textos de nuestros checkbox
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas, 
                                     font=("Dosis", 18, "bold"),
                                     bd=1, 
                                     width=6, 
                                     state=DISABLED, 
                                     textvariable=texto_comida[contador]) # state=DISABLED significa que no estará activo el cuadro de entrada sino hasta que se haya presionado en el checkbox!
    cuadros_comida[contador].grid(row=contador, 
                                  column=1)
    ### Incremento el valor de contador cada ciclo
    contador += 1

## Generar items de bebidas
variables_bebida = []
cuadros_bebida = []
texto_bebida = []

contador = 0

for bebida in lista_bebidas:

    ## Crear checkbuttons
    variables_bebida.append('')
    variables_bebida[contador] = IntVar() # Creo la variable que va a contener la selección o selecciones de nuestro check button
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=("Dosis", 19, "bold"),
                         onvalue=1, offvalue=0, variable=variables_bebida[contador]) # Onvalue y Offvalue significa el valor que va a tener la casilla cuando esté activada y offvalue lo contrario
    bebida.grid(row=contador, column=0, sticky=W) # sticky=W significa que quiero un encolumnado del lado izquierdo de la pantalla

    ## Crear los cuadros de entrada:
    cuadros_bebida.append("")
    texto_bebida.append("")
    # Valores por defecto para los textos de nuestros checkbox
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas, 
                                     font=("Dosis", 18, "bold"),
                                     bd=1, 
                                     width=6, 
                                     state=DISABLED, 
                                     textvariable=texto_bebida[contador]) # state=DISABLED significa que no estará activo el cuadro de entrada sino hasta que se haya presionado en el checkbox!
    cuadros_bebida[contador].grid(row=contador, 
                                  column=1)
    ### Incremento el valor de contador cada ciclo
    contador += 1

## Generar items de postres
variables_postre = []
cuadros_postre = []
texto_postre = []

contador = 0

for postre in lista_postres:

    ## Crear checkbuttons
    variables_postre.append('')
    variables_postre[contador] = IntVar() # Creo la variable que va a contener la selección o selecciones de nuestro check button
    postre = Checkbutton(panel_postres, text=postre.title(), font=("Dosis", 19, "bold"),
                         onvalue=1, offvalue=0, variable=variables_postre[contador]) # Onvalue y Offvalue significa el valor que va a tener la casilla cuando esté activada y offvalue lo contrario
    postre.grid(row=contador, column=0, sticky=W) # sticky=W significa que quiero un encolumnado del lado izquierdo de la pantalla

    ## Crear los cuadros de entrada:
    cuadros_postre.append("")
    texto_postre.append("")
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres, 
                                     font=("Dosis", 18, "bold"),
                                     bd=1, 
                                     width=6, 
                                     state=DISABLED, 
                                     textvariable=texto_postre[contador]) # state=DISABLED significa que no estará activo el cuadro de entrada sino hasta que se haya presionado en el checkbox!
    cuadros_postre[contador].grid(row=contador, 
                                  column=1)
    ### Incremento el valor de contador cada ciclo
    contador += 1

# Panel de Costos
## variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

## Etiquetas de costo y campos de entrada
### Comida
etiqueta_costo_comida = Label(panel_costos,
                              text="Costo Comida",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos, 
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

### Bebida
etiqueta_costo_bebida = Label(panel_costos,
                              text="Costo Bebida",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos, 
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

### Postre
etiqueta_costo_postre = Label(panel_costos,
                              text="Costo Postre",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos, 
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

### Subtotal
etiqueta_subtotal = Label(panel_costos,
                              text="Subtotal",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos, 
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

### Impuesto
etiqueta_impuesto = Label(panel_costos,
                              text="Impuestos",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_costos, 
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3, padx=41)

### Total
etiqueta_total = Label(panel_costos,
                              text="Total",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos, 
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41) # padx = Agraga un padding entre el texto y el borde del objeto

# Botones a construir a traves de un loop y una lista

## Defino mi lista de botones:
botones = ["Total", "Recibo", "Guardar", "Resetear"]
columna = 0

## Loop para crear todos mis botones y ubicarlos en el panel
for boton in botones:
    ### Creacion de los botones
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=("Dosis", 14, "bold"),
                   fg="white",
                   bg="azure4",
                   bd=1,
                   width=9)
    ### Ubicacion de los mismos en el panel:
    boton.grid(row=0, column=columna)
    columna += 1

# Armo el contenido de mi panel de Recibo

## Creo mi texto de recibo
texto_recibo = Text(panel_recibo,
                    font=("Dosis", 12, "bold"),
                    bd=1,
                    width=42,
                    height=10)

## Ubico a mi texto de recibo
texto_recibo.grid(row=0,column=0) # Es 0 y 0 dado que no hay otros elementos dentro de este panel



# Necesito que mi ventana Tkinter no se cierre nunca
aplicacion.mainloop() # Hace que nuestra ventana no se cierre. 


