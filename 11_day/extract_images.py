import os
import bs4
import requests


result = requests.get("https://www.escueladirecta.com/courses")

soup = bs4.BeautifulSoup(result.text, 'lxml')

all_images = soup.select('.course-box-image')
print(all_images)

# Nombre de la carpeta donde guardarás las imágenes.
save_folder = 'images'

# Crea la carpeta si no existe.
os.makedirs(save_folder, exist_ok=True)

# Itero all_images para quedarme solo con el link de la imagen y luego descargarla
for img in all_images:

    image_url = img.get('src')

    image_response = requests.get(image_url)

    ## El contenido está en el "content" de los descargado:
    content_image = image_response.content

    ## Extraigo el nombre para la imagen del link donde la descargué usando OS y le sumo antes el path de mi carpeta images:
    file_name = os.path.join(save_folder, os.path.basename(image_url))

    ## Imprimo el content que por el momento es un binario:
    print(content_image)

    # Guardo la imagen en la carpeta local con el nombre ya construido:
    with open(file_name+".jpg", 'wb') as f:
        f.write(content_image)
        print(f"The image {file_name} has been save in {save_folder}!")

"""
The image images/UTNSPDfDQgurVa1kLkcC has been save in images!
The image images/bcae2c4d38ac4953bd27a3d3be140893 has been save in images!
The image images/MGAWdJKaQqmQ2aMIRUbv has been save in images!
The image images/xvEiapGLTlK2SkgfzV2F has been save in images!
The image images/teachable-logomark-white-31d2296978598bacace50e6d48a2e1223c20a9b074af424acdd465676f81560f.svg has been save in images! 
"""

