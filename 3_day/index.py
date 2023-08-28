def run():
    mi_texto = "Esta es una prueba"
    resultado = mi_texto[0]
    resultado_inverso = mi_texto[-1] # E
    print(resultado + " / " + resultado_inverso) # a
    mi_indice = mi_texto.index("n") # ¿En que indice está la letra n? # indice 9
    # mi_indice_no_existente = mi_texto.index("z") #  ValueError: substring not found
    # print(mi_indice, " / ", mi_indice_no_existente) 
    # Index busca de izquierda a derecha y una vez que encuentra se detiene. 
    print(mi_indice, " / ", ) 
    index_2 = mi_texto.index("a",5)
    print(index_2) # 10
    # Puedo poner también un parametro de finalización el cual no se incluye en la busqueda. El inicio sí. Pero el final no
    rindex = mi_texto.rindex("a") # Busca de derecha a izquierda. 
    print(rindex)


if __name__ == '__main__':
    run()