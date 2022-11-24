import speech_recognition as sr
import pyttsx3



escucha = sr.Recognizer()

inicio = pyttsx3.init()
voices= inicio.getProperty('voices')
inicio.setProperty('voice','spanish')
inicio.say("Buenos  dias mis perros")
inicio .runAndWait()

'''
Haciendo la funcion para que escuche
 y me lo capture  
'''
try:
    with sr.Microphone() as micro:
        print("Escuchando ..... ")
        voz = escucha.listen(micro)
        rec = escucha.recognizer_google(voz)
        print(rec)
except:
    pass

