import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("User said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

def process_command(command):
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I don't know that command.")

# Main loop
speak("Hi, I am your assistant. How can I help you?")
while True:
    user_command = listen()
    if user_command:
        process_command(user_command)
