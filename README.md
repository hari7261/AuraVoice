# Voice Assistant 

## Overview
This project is a **Voice Assistant** built using Python. It integrates speech recognition, text-to-speech, and various system-level functionalities to provide a seamless user experience. The assistant can perform tasks like fetching weather information, opening applications, reading notifications, and answering general questions using Google Search.

## Features
1. **Speech Recognition**: Uses the `speech_recognition` library to convert spoken commands into text.
2. **Text-to-Speech**: Utilizes the `pyttsx3` library to convert text responses into speech.
3. **Google Search Integration**: Redirects user queries to Google Search and reads the results aloud.
4. **System Integration**: Can open files, folders, and applications, and provide system information (e.g., CPU and memory usage).
5. **Notification Detection**: Detects and reads notifications from apps like WhatsApp and Chrome.
6. **Welcome and Goodbye Messages**: Greets the user when the application starts and says goodbye when it closes.
7. **Dynamic Weather Updates**: Fetches weather information using Google Search.
8. **Multi-threading**: Uses threading to handle tasks like notification detection without blocking the main application.
9. **Customizable GUI**: Built using the `customtkinter` library for a modern and user-friendly interface.
10. **Error Handling**: Provides meaningful error messages for invalid commands or system issues.

## Technologies Used
- **Python**: The core programming language used for development.
- **SpeechRecognition**: For converting speech to text.
- **pyttsx3**: For converting text to speech.
- **customtkinter**: For creating a modern and customizable GUI.
- **requests**: For making HTTP requests to fetch Google Search results.
- **BeautifulSoup**: For parsing HTML content from Google Search results.
- **psutil**: For fetching system information like CPU and memory usage.
- **plyer**: For detecting and reading notifications.
- **threading**: For handling background tasks like notification detection.

## Logic and Workflow
1. **Speech Recognition**:
   - The assistant listens to the user's voice command using the microphone.
   - The `speech_recognition` library converts the audio into text.

2. **Command Execution**:
   - The assistant processes the text command and executes the corresponding function.
   - For example, if the user says, "What is the weather in Kolkata?", the assistant redirects to Google Search and reads the weather information.

3. **Text-to-Speech**:
   - The assistant uses the `pyttsx3` library to convert the response into speech and reads it aloud.

4. **System Integration**:
   - The assistant can open files, folders, and applications using the `os` and `subprocess` libraries.
   - It can also fetch system information like CPU and memory usage using the `psutil` library.

5. **Notification Detection**:
   - The assistant uses the `plyer` library to detect notifications from apps like WhatsApp and Chrome.
   - It reads the notification content aloud using the `pyttsx3` library.

6. **Multi-threading**:
   - Background tasks like notification detection are handled using the `threading` library to ensure the main application remains responsive.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/voice-assistant.git
