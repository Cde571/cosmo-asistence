import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyaudio
import random  # Import the random module for generating opinions
import urllib.request
import json
import wikipedia




name = ''

# Crear un objeto de reconocimiento de voz
listener = sr.Recognizer()

# Inicializar el motor de texto a voz
engine = pyttsx3.init()

# Función para obtener el nombre del usuario
def get_name():
    try:
        with sr.Microphone() as source:
            # Indicar al usuario que diga su nombre
            engine.say("Hola, me alegra saludarte. ¿Cómo te llamas?")
            engine.runAndWait()

            # Escuchar la respuesta del usuario
            audio = listener.listen(source)

            # Reconocer el nombre del usuario
            name = listener.recognize_google(audio, language='es')

            # Mostrar el nombre reconocido
            print("Tu nombre es" + name)
            engine.runAndWait()

    except sr.UnknownValueError:
        print("No pude entenderte. Por favor, repite tu nombre.")
        get_name()  # Recursividad si no se reconoce el nombre

    except sr.RequestError:
        print("Error al obtener el nombre. Inténtalo de nuevo más tarde.")

# obtener el nombre del usuario
get_name()

# saludar al usuario por su nombre
engine.say("Hola"+name+", ¿cómo estás?")
engine.runAndWait()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Speak now:")
            audio = listener.listen(source)
            text = listener.recognize_google(audio)
            print("You said:", text)
            engine.say("Acabas de decir"+text)
            return text
    except:
        engine.say("No te entiendo, puedes repetir por favor")
        return ""

    return None

def run():
    while True:
        text = listen()
        if text and 'reproduce ' in text:
            music = text.replace('reproduce','')

            # express opinions about the song
            opinions = [
                "Esta canción es un clásico, siempre me pone de buen humor.",
                "Me encanta el ritmo de esta canción, ¡es perfecta para bailar!",
                "La melodía de esta canción es muy relajante, me ayuda a concentrarme.",
                "La letra de esta canción es muy profunda, me hace reflexionar.",
                "La voz del cantante es increíble, ¡me transmite muchas emociones!",
                "¡Esta canción es super pegadiza, no puedo dejar de cantarla!",
                "Este género musical no es mi favorito, pero admito que esta canción tiene algo especial."
            ]
            opinion = random.choice(opinions)  # choose a random opinion

            speak(opinion)  # express the opinion
            speak(f"Reproduciendo {music}")  # then announce the playback
            pywhatkit.playonyt(music)
        elif 'busca' in text:
            order = text.replace('busca','')
            info = wikipedia.summary(order,1)
            engine.say(order)


run()
