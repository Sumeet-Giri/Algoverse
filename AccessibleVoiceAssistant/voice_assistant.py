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

def get_confirmation():
    for _ in range(2):
        response = listen()
        if any(word in response for word in ["yes", "sure", "go ahead", "okay"]):
            return True
        elif any(word in response for word in ["no", "cancel", "stop"]):
            return False
        else:
            speak("Sorry, I didn't understand. Please say yes or no.")
    speak("No response detected. Cancelling the command.")
    return False

def process_command(command):
    if "help" in command:
        speak("You can ask me to tell the time, open YouTube, open Notepad, or run any command. Say exit or quit to stop.")
    elif "time" in command:
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
        speak(f"You said: {command}. Do you want to run this command? Please say yes or no.")
        if get_confirmation():
            speak(f"Running command: {command}")
            try:
                os.system(command)
            except Exception as e:
                speak(f"Failed to run the command: {e}")
        else:
            speak("Okay, command not executed.")

# Main loop
speak("Hi, I am your assistant. Say 'help' to know what I can do. How can I help you?")
while True:
    speak("I'm listening for your command.")
    user_command = listen()
    if user_command:
        process_command(user_command)
