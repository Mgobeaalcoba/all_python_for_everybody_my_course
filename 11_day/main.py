import bs4
import requests

# Extraer el Titulo de la Página (Es el que está arriba en la pestaña)
## Le digo a Python que le haga get a la página que me interesa consultar: 
resultado = requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")

# print(type(resultado))
# print()
# print(resultado) # <Response [200]>
# print(resultado.encoding) # UTF-8
# print(resultado.reason) # OK
# # print(resultado.content) # Me trae todo el HTML o código fuente de la página. 
# print(resultado.cookies) # <RequestsCookieJar[]>
# print(resultado.headers) # {'Content-Type': 'text/html; charset=UTF-8', 'Expires': 'Fri, 15 Sep 2023 20:04:16 GMT', 'Date': 'Fri, 15 Sep 2023 20:04:16 GMT', 'Cache-Control': 'private, max-age=0', 'Last-Modified': 'Fri, 28 Jul 2023 09:29:57 GMT', 'ETag': 'W/"89566f8480986bae307dbf99360f5a1a561ae19b5b235ebfad9a498542ab2081"', 'Content-Encoding': 'gzip', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '1; mode=block', 'Server': 'GSE', 'Alt-Svc': 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000', 'Transfer-Encoding': 'chunked'}
# print(resultado.history) # []
# # print(resultado.text) # El código fuente pero estructurado para una lectura más agil

# # Hastá acá lo que obtenemos como resultado de la request es un texto en formato string. Debe ser parseado a un HTML y para eso debo usar Beautiful Soup 4 o bs4

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

print(type(sopa)) # <class 'bs4.BeautifulSoup'>
# print(sopa) # Ya no es un string. Ahora es un BeautifulSoup Object

## La diferencia principal radica en que este elemento de tipo BeautifulSoup nos permite navegar entre sus elementos:

# for element in sopa.find_all():
#     if 'link' in element.get_text():
#         print("hola")
#         print(element) # Imprime de a uno cada uno de los elementos y esto lo puedo usar para filtrar


# Utilizando el método find_all con una expresión lambda
elementos_con_link = sopa.find_all(lambda tag: tag.name and 'link' in tag.get_text())

# Utilizando el método select con un selector CSS
elementos_con_link2 = sopa.select(':-soup-contains("link")')

# Imprime los elementos que cumplen con el criterio
# for elemento in elementos_con_link2:
#     print(elemento)

# Imprime los elementos que cumplen con el criterio
# for elemento in elementos_con_link:
#     print(elemento)

## Las treas formas dan los mismos resultados

# Tmb puedo buscar exactamente por el nombre de la etiqueta: 

# print(sopa.select('title')) # [<title>Encapsulamiento - Pilares de la Programaci�n Orientada a Objetos en Python</title>]

# print(sopa.select('link')) # [<link href="https://escueladirecta-blog.blogspot.com/favicon.ico" rel="icon" type="image/x-icon"/>, <link href="https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html" rel="canonical"/>, <link href="https://escueladirecta-blog.blogspot.com/feeds/posts/default" rel="alternate" title="Escuela Directa | Blog - Atom" type="application/atom+xml"/>, <link href="https://escueladirecta-blog.blogspot.com/feeds/posts/default?alt=rss" rel="alternate" title="Escuela Directa | Blog - RSS" type="application/rss+xml"/>, <link href="https://www.blogger.com/feeds/9051560144631131122/posts/default" rel="service.post" title="Escuela Directa | Blog - Atom" type="application/atom+xml"/>, <link href="https://escueladirecta-blog.blogspot.com/feeds/9007029838311903839/comments/default" rel="alternate" title="Escuela Directa | Blog - Atom" type="application/atom+xml"/>, <link href="https://www.blogger.com/dyn-css/authorization.css?targetBlogID=9051560144631131122&amp;zx=c69528fb-44d4-474e-8953-7e9b18ce55b0" media="none" onload="if(media!='all')media='all'" rel="stylesheet"/>, <link href="https://www.blogger.com/dyn-css/authorization.css?targetBlogID=9051560144631131122&amp;zx=c69528fb-44d4-474e-8953-7e9b18ce55b0" rel="stylesheet"/>, <link href="https://fonts.googleapis.com/css2?display=swap&amp;family=Manrope&amp;family=Roboto&amp;family=Montserrat&amp;family=Lato&amp;family=Poppins" rel="stylesheet"/>]

# Quiero saber cuantos elementos parrafos tiene la pagina lo puedo hacer de la siguiente forma: 

print(len(sopa.select('p'))) # 4

# Si no quiero traer todo: elmento + texto en una lista entonces tengo que pedir el .get_text() del elemento al que deseo acceder así: 

print(sopa.select('title')[0].get_text()) # Encapsulamiento - Pilares de la Programaci�n Orientada a Objetos en Python

## Y ahí finalmente ya tengo entonces el titulo de mi pagina puro!!!

# Me quiero traer solo el contenido del 4° parrafo de la lista:

print(sopa.select('p')[3].get_text()) # instancia + _ + NombreClase + m�todo/atributo oculto
