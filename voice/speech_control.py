import speech_recognition as sr
import pyttsx3

# Voice Engine
engine = pyttsx3.init()

# AI Speak Function
def speak(text):

    engine.say(text)
    engine.runAndWait()

# Listen Function
def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        command = recognizer.recognize_google(audio)

        command = command.lower()

        print("You Said:", command)

        return command

    except:

        return ""