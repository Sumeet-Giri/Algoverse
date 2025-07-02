import webbrowser
import datetime
import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def process_command(command):
    command = command.lower()
    if "help" in command:
        return "You can ask me to tell the time, open YouTube, open Notepad, or run any command. Say exit or quit to stop."
    elif "time" in command:
        time_str = datetime.datetime.now().strftime("%I:%M %p")
        return f"The time is {time_str}"
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"
    elif "open notepad" in command:
        os.system("notepad")
        return "Opening Notepad"
    elif "exit" in command or "quit" in command:
        return "Goodbye!"
    else:
        # For demo, just echo the command
        return f"You said: {command}"

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    command = data.get('command', '')
    response = process_command(command)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)