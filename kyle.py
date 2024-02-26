import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()

engine.say("Hola Cristian, como estas?")
engine.runAndWait()

def speak(text):
    engine.say(text)
    engine.runAndWait()

try:
    with sr.Microphone() as source:
        print("Speak now:")
        audio = listener.listen(source)
        text = listener.recognize_google(audio)
        print("You said:", text)
        speak(text)
except:
    pass

