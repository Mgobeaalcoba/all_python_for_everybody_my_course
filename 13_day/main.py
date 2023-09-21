import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

def run():
    desgrabar()

# Escucha nuestro microfono y devuelve el audio como texto - desgrabar:
def desgrabar():
    # almacenar el recognizer en variable
    r = sr.Recognizer()

    # configuramos el microfono
    with sr.Microphone() as origen:
        # Tiempo de espera desde que se active el microfono
        r.pause_threshold = 0.8 # menos de 1 segundo

        # Informar que comenzó la grabación para saber que ya comenzó
        print("Ya puedes hablar!")

        # Guardo en una variable lo que escucha como audio:
        audio = r.listen(origen)

        try:
            # Buscar en google lo que haya escuchado
            pedido = r.recognize_google(audio, lenguaje= "es-ar")

            # Prueba de que pudo ingresar y transformar nuestra vos:
            print("Dijiste: " + pedido)

            # Devolver pedido
            return pedido
        
        # En caso de que no pueda hacer la función dado que no comprende el audio
        except sr.UnknownValueError:
            # Prueba de que no comprendió el audio
            print("Upss, no entendí su mensaje")

            # Devolver error
            return "sigo esperando"
        
        # En caso de no resolver el pedido
        except sr.RequestError:
            # Prueba de que no comprendió el audio
            print("Upss, no hay servicio")

            # Devolver error
            return "sigo esperando"
        
        except:
            # Prueba de que no comprendió el audio
            print("Upss, algo ha salido mal")

            # Devolver error
            return "sigo esperando"
        
if __name__ == '__main__':
    run()