import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

def run():
    # desgrabar()
    # hablar("Hello World!!! This is my first message. I'm your own voice assistant programmed with Python. Congratulations!")
    # distintas_voces()
    # pedir_dia()
    saludo_inicial()
    pedir_hora()

# Escucha nuestro micrófono y devuelve el audio como texto - desgrabar:
def desgrabar():
    # almacenar el recognizer en variable
    r = sr.Recognizer()

    # configuramos el micrófono
    with sr.Microphone() as origen:
        # Tiempo de espera desde que se active el micrófono
        r.pause_threshold = 0.8 # menos de 1 segundo

        # Informar que comenzó la grabación para saber que ya comenzó
        print("Ya puedes hablar!")

        # Guardo en una variable lo que escucha como audio:
        audio = r.listen(origen)

        try:
            # Buscar en google lo que haya escuchado
            pedido = r.recognize_google(audio, language="es-ar")

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

# Transformar la respuesta de nuestro asistente (por ahora en texto) a una voz humana
def hablar(mensaje):
    # Encender el motor de pyttsx3
    engine = pyttsx3.init() # Inicio el motor

    # Seteo el idioma que deseo usar para mi asistente de voz:
    engine.setProperty('voice', distintas_voces())

    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

# Identificar las distintas voces que tengo en mi os y devolver alguna de ellas.
def distintas_voces() -> str:
    engine = pyttsx3.init()

    # Devuelve las voces disponibles en mi sistema operativo:
    for voice in engine.getProperty('voices'):
        print(voice)

    # Guardo los id's en variables para luego poder usarlos si fuese necesario:
    id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

    return id1

# Informar el día de la semana
def pedir_dia():
    # Crear la variable con datos de hoy:
    dia = datetime.date.today()
    print(dia)

    # Diccionario para poder obtener el nombre del día
    dias = {
        "0": "Monday",
        "1": "Tuesday",
        "2": "Wednesday",
        "3": "Thursday",
        "4": "Friday",
        "5": "Saturday",
        "6": "Sunday",
    }

    # Crear una variable para el día de la semana
    dia_semana = str(dia.weekday())
    print(dias[dia_semana])

    # Le pido a mi asistente que me diga el día y la fecha
    hablar(f"Today is {dias[dia_semana]} and the date is {dia}. Good day Marian!")

# Informar que hora es
def pedir_hora():
    # Crea una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f"In this moment is the hour {hora.hour} with {hora.minute} minutes and {hora.second} seconds. There is still one day ahead"
    print(hora)

    # Decir la hora
    hablar(hora)

# Saludo inicial
def saludo_inicial():
    # Desear buenos días, buenas tardes o buenas noches en función del horario
    hora = datetime.datetime.now().hour

    # Armó el saludo deseado en función del horario
    if hora < 5:
        greetings = "Good evening"
    elif hora < 13:
        greetings = "Good morning"
    else:
        greetings = "Good afternoon"

    # Decir el saludo!
    hablar(f"Hello, {greetings}, I'm Ada, your personal assistant. Tell me where I can help you")

if __name__ == '__main__':
    run()
