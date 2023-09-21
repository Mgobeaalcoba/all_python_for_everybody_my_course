from tkinter import * # Importante importar tkinter así y no con un "import tkinter" porque te ahorra mucho código al llamar las clases, constantes, etc.
from model.calculadora import Calculadora
from typing import Tuple, Union
from random import randint
import datetime


def pintar_frontend():
    # Iniciar a tkinter
    aplicacion = Tk()

    # Tamaño de la ventana y ubicación de la ventana
    aplicacion.geometry('1248x630+0+0') # Va antes del loop dado que sino se mostrará pequeña como viene por default 1250x630

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

    # Defino los precios de mis productos ofrecidos en el restaurante: 
    precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
    precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
    precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

    # Función para revisar si los checkbuttons se activaron o no y habilitar los Entry frente a su activación
    def revisar_check():
        for x in range(len(cuadros_comida)):
            if variables_comida[x].get() == 1:
                cuadros_comida[x].config(state=NORMAL)
                if cuadros_comida[x].get() == "0":
                    cuadros_comida[x].delete(0, END)
                cuadros_comida[x].focus()
            else:
                if cuadros_comida[x].get() == "":
                    cuadros_comida[x].insert(END, "0")
                cuadros_comida[x].config(state=DISABLED)

        for x in range(len(cuadros_bebida)):
            if variables_bebida[x].get() == 1:
                cuadros_bebida[x].config(state=NORMAL)
                if cuadros_bebida[x].get() == "0":
                    cuadros_bebida[x].delete(0, END)
                cuadros_bebida[x].focus()
            else:
                if cuadros_bebida[x].get() == "":
                    cuadros_bebida[x].insert(END, "0")
                cuadros_bebida[x].config(state=DISABLED)

        for x in range(len(cuadros_postre)):
            if variables_postre[x].get() == 1:
                cuadros_postre[x].config(state=NORMAL)
                if cuadros_postre[x].get() == "0":
                    cuadros_postre[x].delete(0, END)
                cuadros_postre[x].focus()
            else:
                if cuadros_postre[x].get() == "":
                    cuadros_postre[x].insert(END, "0")
                cuadros_postre[x].config(state=DISABLED)

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
                            font=("Dosis", 19),
                            onvalue=1, 
                            offvalue=0, 
                            variable=variables_comida[contador],
                            command=revisar_check) # Onvalue y Offvalue significa el valor que va a tener la casilla cuando esté activada y offvalue lo contrario
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
        bebida = Checkbutton(panel_bebidas, 
                            text=bebida.title(), 
                            font=("Dosis", 19),
                            onvalue=1, 
                            offvalue=0, 
                            variable=variables_bebida[contador],
                            command=revisar_check) # Onvalue y Offvalue significa el valor que va a tener la casilla cuando esté activada y offvalue lo contrario
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
        postre = Checkbutton(panel_postres, 
                            text=postre.title(), 
                            font=("Dosis", 19),
                            onvalue=1, 
                            offvalue=0, 
                            variable=variables_postre[contador],
                            command=revisar_check) # Onvalue y Offvalue significa el valor que va a tener la casilla cuando esté activada y offvalue lo contrario
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

    ## Defino mi lista de nombres de botones:
    botones = ["Total", "Recibo", "Guardar", "Resetear"]

    # Defino otra lista para guardar mis objetos Button creados
    botones_creados = []

    columna = 0

    # Defino las funciones que van a realizar mis botones (Esto podría pasarse a lógica de negocio con una clase Botonera)

    ## Imprimir recibo para el segundo botón:
    def imprimir_recibo() -> None:
        sub_total_comida, sub_total_bebida,  sub_total_postre = calcular_subtotales()
        total_sin_impuestos = sub_total_comida + sub_total_bebida + sub_total_postre
        impuestos = calcular_impuestos(total_sin_impuestos)
        total = total_sin_impuestos + impuestos

        # Edito el texto recibo
        texto_recibo.delete(1.0, END)
        texto_recibo.insert(END, "************************************\n")
        texto_recibo.insert(END, f"Factura N° {randint(1000,9999)}-{randint(1000000,9999999)}\n")
        texto_recibo.insert(END, f"Fecha de emisión {datetime.date.today()}\n")
        texto_recibo.insert(END, "\n")
        texto_recibo.insert(END, "************************************\n")
        texto_recibo.insert(END, "Detalle\n")
        texto_recibo.insert(END, "\n")
        texto_recibo.insert(END, f"[1] Comida: $ {round(sub_total_comida, 2)}\n")
        texto_recibo.insert(END, f"[2] Bebida: $ {round(sub_total_bebida, 2)}\n")
        texto_recibo.insert(END, f"[3] Postre: $ {round(sub_total_postre, 2)}\n")
        texto_recibo.insert(END, f"[4] Subtotal: $ {round(total_sin_impuestos, 2)}\n")
        texto_recibo.insert(END, f"[5] Impuestos: $ {round(impuestos, 2)}\n")
        texto_recibo.insert(END, "\n")
        texto_recibo.insert(END, "************************************\n")
        texto_recibo.insert(END, "\n")
        texto_recibo.insert(END, f"[6] Total: $ {round(total, 2)}\n")

    ## Calcular Total para el primer boton
    def calcular_total() -> None:
        sub_total_comida, sub_total_bebida,  sub_total_postre = calcular_subtotales()
        total_sin_impuestos = sub_total_comida + sub_total_bebida + sub_total_postre
        impuestos = calcular_impuestos(total_sin_impuestos)
        total = total_sin_impuestos + impuestos

        # Edito el panel de costos
        texto_costo_comida.config(state=NORMAL)
        texto_costo_comida.delete(0, END)
        texto_costo_comida.insert(END, f"$ {round(sub_total_comida, 2)}")
        texto_costo_comida.config(state="readonly")

        texto_costo_bebida.config(state=NORMAL)
        texto_costo_bebida.delete(0, END)
        texto_costo_bebida.insert(END, f"$ {round(sub_total_bebida, 2)}")
        texto_costo_bebida.config(state="readonly")

        texto_costo_postre.config(state=NORMAL)
        texto_costo_postre.delete(0, END)
        texto_costo_postre.insert(END, f"$ {round(sub_total_postre, 2)}")
        texto_costo_postre.config(state="readonly")

        texto_subtotal.config(state=NORMAL)
        texto_subtotal.delete(0, END)
        texto_subtotal.insert(END, f"$ {round(total_sin_impuestos, 2)}")
        texto_subtotal.config(state="readonly")

        texto_impuesto.config(state=NORMAL)
        texto_impuesto.delete(0, END)
        texto_impuesto.insert(END, f"$ {round(impuestos, 2)}")
        texto_impuesto.config(state="readonly")

        texto_total.config(state=NORMAL)
        texto_total.delete(0, END)
        texto_total.insert(END, f"$ {round(total, 2)}")
        texto_total.config(state="readonly")

    ## Auxiliares
    def calcular_impuestos(importe: int | float) -> int | float:
        return importe * 0.21


    def calcular_subtotales() -> Tuple[Union[int, float], Union[int, float], Union[int, float]]:
        sub_total_comida = 0
        for x in range(len(cuadros_comida)):
            sub_total_comida += int(cuadros_comida[x].get()) * precios_comida[x]

        sub_total_bebida = 0
        for x in range(len(cuadros_bebida)):
            sub_total_bebida += int(cuadros_bebida[x].get()) * precios_bebida[x]
        
        sub_total_postre = 0
        for x in range(len(cuadros_postre)):
            sub_total_postre += int(cuadros_postre[x].get()) * precios_postres[x]

        return sub_total_comida, sub_total_bebida,  sub_total_postre

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
        ### Agrego los botones creados a mi lista de objetos
        botones_creados.append(boton)

    ## Con todos mis botones creados ahora voy a asignarle a cada uno de ellos su función
    botones_creados[0].config(command=calcular_total)
    botones_creados[1].config(command=imprimir_recibo)

    # Armo el contenido de mi panel de Recibo

    ## Creo mi texto de recibo
    texto_recibo = Text(panel_recibo,
                        font=("Dosis", 12, "bold"),
                        bd=1,
                        width=51,
                        height=10)

    ## Ubico a mi texto de recibo
    texto_recibo.grid(row=0,column=0) # Es 0 y 0 dado que no hay otros elementos dentro de este panel

    # Armo la calculadora de mi sistema y con esto terminamos la parte VISUAL. Falta la lógica de negocio. 

    ## Creamos el visor de la calculadora
    visor_calculadora = Entry(panel_calculadora, 
                            font=("Dosis", 16, "bold"),
                            width=39,
                            bd=1)

    ## Establecemos la ubicación del visor en el panel:
    visor_calculadora.grid(row=0, column=0, columnspan=4) # Aparece arriba de todo. Columnspan=4 es para que ocupe todo el ancho de mi columna

    ## Creo los 16 botones de mi calculadora. Como son un montón voy a hacerlo mediante un loop. 
    botones_calculadora = ["7","8","9","+",
                        "4","5","6","-",
                        "1","2","3","X",
                        "R","B","0","/"]

    ## Creo una lista para guardar todos los botones creados y luego hacer que cada botón use la función "click_boton" frente al evento de click:
    botones_guardados = []

    ## Creo las variables que van ordenar la inserción de mis botones. Sabiendo que la fila 0 ya está ocupada con el visor de mi calculadora:
    fila = 1
    columna = 0

    for boton in botones_calculadora:
        ### Creo a mis botones de calculador
        boton = Button(panel_calculadora,
                    text=boton.title(),
                    font=("Dosis", 14, "bold"),
                    fg="white",
                    bg="azure4",
                    bd=1,
                    width=9)
        
        botones_guardados.append(boton)
        
        ### Ubico a mis botones de calculadora 
        boton.grid(row=fila, column=columna)
        
        if columna == 3:
            columna = 0
            fila += 1
        else:
            columna += 1

    ## Creo un objeto Calculadora para asignar sus métodos al frontend
    calculadora = Calculadora(visor_calculadora)

    ## Agregamos funcionalidad a todos los botones: 

    botones_guardados[0].config(command=lambda : calculadora.click_boton("7"))
    botones_guardados[1].config(command=lambda : calculadora.click_boton("8"))
    botones_guardados[2].config(command=lambda : calculadora.click_boton("9"))
    botones_guardados[3].config(command=lambda : calculadora.click_boton("+"))
    botones_guardados[4].config(command=lambda : calculadora.click_boton("4"))
    botones_guardados[5].config(command=lambda : calculadora.click_boton("5"))
    botones_guardados[6].config(command=lambda : calculadora.click_boton("6"))
    botones_guardados[7].config(command=lambda : calculadora.click_boton("-"))
    botones_guardados[8].config(command=lambda : calculadora.click_boton("1"))
    botones_guardados[9].config(command=lambda : calculadora.click_boton("2"))
    botones_guardados[10].config(command=lambda : calculadora.click_boton("3"))
    botones_guardados[11].config(command=lambda : calculadora.click_boton("*"))
    botones_guardados[12].config(command=calculadora.obtener_resultado)
    botones_guardados[13].config(command=calculadora.borrar)
    botones_guardados[14].config(command=lambda : calculadora.click_boton("0"))
    botones_guardados[15].config(command=lambda : calculadora.click_boton("/"))

    # Necesito que mi ventana Tkinter no se cierre nunca
    aplicacion.mainloop() # Hace que nuestra ventana no se cierre. 


