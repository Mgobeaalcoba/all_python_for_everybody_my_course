"""
Objetivo: scrapear la web de "toscrape.com" para obtener de ella todos los titulos
de los libros que estén calificados con 4 o más
estrellas.
Consideraciones:
1. Cada pagina nos muestra solo 20 libros. Pero tenemos 1000 almacenados por lo que tendremos que ir navegando la web para poder obtener todos
Dirección pagina 1: http://books.toscrape.com/catalogue/category/books_1/page-1.html
Dirección pagina 2: http://books.toscrape.com/catalogue/category/books_1/page-2.html
"""

import bs4
import requests

# counter1 = 1

# counter2 = 51

# result1 = requests.get(f"http://books.toscrape.com/catalogue/category/books_1/page-{counter1}.html")

# result2 = requests.get(f"http://books.toscrape.com/catalogue/category/books_1/page-{counter2}.html")

# print(result1.reason) # OK
# print(result1) # <Response [200]>
# print(result2.reason) # Not Found
# print(result2) # <Response [404]>

# soup = bs4.BeautifulSoup(result1.text, 'lxml')
# # elements = soup.select("article .Five") # Trae solo los "p" class"Five" pero no todo el article.

# # Utiliza el método find_all para buscar todos los elementos "article" que contienen un "p" con la clase "Five"
# all_articles = soup.find_all('article', recursive=True)  # Busca todos los elementos "article" en el documento

# # Filtra los elementos que contienen un "p" con la clase "Five"
# filtered_articles = [article for article in all_articles if article.find('p', class_='Five')]

# # filter_elements = elements.select()
# print(all_articles)
# print()
# print(len(all_articles))

# print()

# print(filtered_articles)
# print()
# print(len(filtered_articles))


my_titles = []

counter = 1

print("Hola estoy por entrar al ciclo while!!! Suerte!")

dinamic_web = f"http://books.toscrape.com/catalogue/category/books_1/page-{counter}.html"

result = requests.get(dinamic_web)

print(f"Web a hacerle Get es: {dinamic_web}")
print()

while result.reason != "Not Found":
    result = requests.get(f"http://books.toscrape.com/catalogue/category/books_1/page-{counter}.html")
    print(result.reason)
    print(result)
    soup = bs4.BeautifulSoup(result.text, 'lxml')

    # Utiliza el método find_all para buscar todos los elementos "article" que contienen un "p" con la clase "Five"
    all_articles = soup.find_all('article', recursive=True)  # Busca todos los elementos "article" en el documento

    # Filtra los elementos que contienen un "p" con la clase "Five"
    filtered_articles = [article for article in all_articles if article.find('p', class_='Five')]
    
    # Recorre los elementos "article" filtrados
    for article in filtered_articles:
        # Busca el primer "h3" dentro del elemento "article"
        h3 = article.find('h3')
        
        # Comprueba si se encontró un "h3"
        if h3:
            # Busca el primer elemento "a" dentro del "h3" y obtén su texto
            a = h3.find('a')
            if a:
                my_titles.append(a.text)

    # Filtra los elementos que contienen un "p" con la clase "Five"
    filtered_articles = [article for article in all_articles if article.find('p', class_='Four')]

    # Recorre los elementos "article" filtrados
    for article in filtered_articles:
        # Busca el primer "h3" dentro del elemento "article"
        h3 = article.find('h3')
        
        # Comprueba si se encontró un "h3"
        if h3:
            # Busca el primer elemento "a" dentro del "h3" y obtén su texto
            a = h3.find('a')
            if a:
                my_titles.append(a.text)

    counter += 1

    dinamic_web = f"http://books.toscrape.com/catalogue/category/books_1/page-{counter}.html"

    result = requests.get(dinamic_web)

    print(f"Web a hacerle Get es: {dinamic_web}")
    print()

print(len(my_titles))
print()

for title in my_titles:
    print(title)

# Guardo los nombres en un archivo en la raiz del proyecto con el nombre ya construido:
with open("project/best_books.txt", 'a') as f:
    for title in my_titles:
        f.write(title+"\n")

# Challenge resuelto


