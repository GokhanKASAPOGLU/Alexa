import speech_recognition as sr
import pyttsx3
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id) # 0 for female 1 for male voice

def talk(talking_text):
    engine.say(talking_text)
    engine.runAndWait()

def take_command():
    command = ("")
    try:
        with sr.Microphone() as source:
            talk("Listening...")
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if command.lower().startswith("alexa"):
                command = command.replace("Alexa ", "")
                print(command)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError:
        print(f"Could not request results; {sr.RequestError}")
    except Exception:
        print(f"An error occurred: {Exception}")
    return command

def run_alexa():
    command = take_command()
    if ("play") in command:
        song = command.replace("play ", "")
        talk("Playing " + song)
        print("Playing " + song)
        pywhatkit.playonyt(song)
    elif ("exit Alexa") in command:
        talk("Have a nice day!")
        print("Have a nice day!")
        print(command)
        exit()
    else:
        talk("Please say the command again.")
        print("Please say the command again.")
        print(command)

while True:
    run_alexa()
