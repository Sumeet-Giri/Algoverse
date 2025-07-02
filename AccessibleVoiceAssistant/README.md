# Accessible Voice Assistant (Web + Voice)

A simple voice assistant with a web interface, supporting both text and speech input, powered by Flask and the Web Speech API.

## Features

- Type or speak commands in your browser
- Handles commands like "time", "open youtube", "open notepad", etc.
- User-friendly, responsive web UI

## Requirements

- Python 3.x
- Flask (`pip install flask`)
- Google Chrome (for best speech recognition support)

## Setup

1. **Clone or download this repository.**

2. **Install dependencies:**
   ```
   pip install flask
   ```

3. **Project structure:**
   ```
   AccessibleVoiceAssistant/
   ├── voice_assistant_server.py
   ├── static/
   │   ├── style.css
   │   └── script.js
   └── templates/
       └── index.html
   ```

4. **Run the Flask server:**
   ```
   python voice_assistant_server.py
   ```

5. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000/
   ```

6. **Usage:**
   - Type a command or click the 🎤 Speak button and say a command.
   - Example commands:  
     - `What time is it?`  
     - `Open YouTube`  
     - `Open Notepad`  
     - `Help`  
     - `Exit`

## Notes

- For speech recognition, use Google Chrome and allow microphone access.
- Some commands (like opening Notepad) will only work on Windows.
- The backend runs commands on the server machine, not the client.

---
```# Accessible Voice Assistant (Web + Voice)

A simple voice assistant with a web interface, supporting both text and speech input, powered by Flask and the Web Speech API.

## Features

- Type or speak commands in your browser
- Handles commands like "time", "open youtube", "open notepad", etc.
- User-friendly, responsive web UI

## Requirements

- Python 3.x
- Flask (`pip install flask`)
- Google Chrome (for best speech recognition support)

## Setup

1. **Clone or download this repository.**

2. **Install dependencies:**
   ```
   pip install flask
   ```

3. **Project structure:**
   ```
   AccessibleVoiceAssistant/
   ├── voice_assistant_server.py
   ├── static/
   │   ├── style.css
   │   └── script.js
   └── templates/
       └── index.html
   ```

4. **Run the Flask server:**
   ```
   python voice_assistant_server.py
   ```

5. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000/
   ```

6. **Usage:**
   - Type a command or click the 🎤 Speak button and say a command.
   - Example commands:  
     - `What time is it?`  
     - `Open YouTube`  
     - `Open Notepad`  
     - `Help`  
     - `Exit`

## Notes

- For speech recognition, use Google Chrome and allow microphone access.
- Some commands (like opening Notepad) will only work on Windows.
- The backend runs commands on the server machine, not the client.