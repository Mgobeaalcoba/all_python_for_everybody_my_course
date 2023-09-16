import bs4
import requests

""" 
Caracter    Sintaxis                        Resultados
" o '       soup.select('div')              Todos los elementos con la etiqueta 'div'
#           soup.select('#estilo_4')        Elementos que contengan id='estilo_4'
.           soup.select('.columna_der')     Elementos que contengan class='columna_der'
(ESPACIO)   soup.select('div span')         Cualquier elemento llamado 'span' dentro de un elemento 'div'
>           soup.select('div>span')         Cualquier elemento llamado 'span' directamente dentro de un elemento 'div', sin nada en el medio.
"""

resultado = requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")

sopa = bs4.BeautifulSoup(resultado.text, "lxml")

columna_lateral = sopa.select('.sidebar-container')
# columna_lateral = sopa.select('.content')
print(columna_lateral) # Trae el contenido completo de mi sidebar

## Quiero solo los links o "a" de mi sidebar

links_sidebar = sopa.select('.sidebar-container a')
print()
# print(links_sidebar)

## Imprimo de a uno todos los links en lugar de imprimir todo en una lista:
for a in links_sidebar:
    print(a) # Me imprime cada elemento completo.

## Si quiero solo el texto del elemento entonces puedo hacer
print(links_sidebar[0].get_text()) # Cohesión - Pilares de la Programación Orientada a Objetos en Python

## Si quiero solo el link debería hacer: 
print(links_sidebar[0].get('href')) # https://escueladirecta-blog.blogspot.com/2021/09/cohesion-pilares-de-la-programacion.html

## Entonces podría iterar e imprimir todos los links que encuentro en el sidebar de la pagina así: 
for a in links_sidebar:
    print(a.get('href'))

