# Accessible Voice Assistant

This is a simple AI-based voice assistant built to help visually impaired users interact with their computer using voice commands.

## Features
- Voice recognition using Google API
- Text-to-speech responses
- Commands like:
  - "What is the time?"
  - "Open YouTube"
  - "Open Notepad"

## Requirements

Install required packages using pip:

```
pip install SpeechRecognition pyttsx3 pyaudio
```

If `pyaudio` fails, run:

```
pip install pipwin
pipwin install pyaudio
```

## Running the App

Run the assistant using:

```
python voice_assistant.py
```

## Future Scope
- Integrate OCR for reading text from images
- Add chatbot integration (like GPT)
- GUI support

y