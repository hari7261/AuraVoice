import speech_recognition as sr
import pyttsx3
import customtkinter as ctk
import datetime
import webbrowser
import subprocess
import threading
import os
import requests
from bs4 import BeautifulSoup
import psutil
import time
import plyer

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()
        self.notification_check_interval = 10
        self.notification_thread = threading.Thread(target=self.check_notifications, daemon=True)
        self.notification_thread.start()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio)
                return text.lower()
            except sr.UnknownValueError:
                return ""
            except sr.RequestError:
                return ""

    def get_date(self):
        return datetime.datetime.now().strftime("%B %d, %Y")

    def get_time(self):
        return datetime.datetime.now().strftime("%I:%M %p")

    def open_application(self, app_name):
        app_name = app_name.lower()
        if app_name == "youtube":
            webbrowser.open("https://www.youtube.com")
            return "Opening YouTube"
        elif app_name == "chrome":
            if os.name == 'nt':
                os.startfile("chrome")
            elif os.name == 'posix':
                subprocess.Popen(["google-chrome"])
            return "Opening Chrome"
        else:
            try:
                subprocess.Popen(app_name)
                return f"Opening {app_name}"
            except:
                return f"Unable to open {app_name}"

    def search_google(self, query):
        try:
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)
            return f"Searching Google for '{query}'"
        except Exception as e:
            return f"An error occurred while searching: {str(e)}"

    def read_google_search_results(self, query):
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
            }
            response = requests.get(f"https://www.google.com/search?q={query}", headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            weather_info = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
            if weather_info:
                weather_text = weather_info.get_text()
                return f"The weather is: {weather_text}"
            else:
                return "I find weather on Google."
        except Exception as e:
            return f"An error occurred while reading search results: {str(e)}"

    def check_notifications(self):
        while True:
            notifications = plyer.notification.get_notifications()
            if notifications:
                for notification in notifications:
                    self.speak(f"You have a notification from {notification['app_name']}. {notification['message']}")
            time.sleep(self.notification_check_interval)

    def get_system_info(self):
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        return f"CPU usage is {cpu_usage}% and memory usage is {memory_usage}%."

    def open_file(self, file_path):
        try:
            os.startfile(file_path)
            return f"Opening {file_path}"
        except Exception as e:
            return f"Unable to open {file_path}. Error: {str(e)}"

    def open_folder(self, folder_path):
        try:
            os.startfile(folder_path)
            return f"Opening {folder_path}"
        except Exception as e:
            return f"Unable to open {folder_path}. Error: {str(e)}"

class AssistantGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Enhanced Voice Assistant")
        self.master.geometry("500x400")
        self.assistant = VoiceAssistant()
        self.label = ctk.CTkLabel(master, text="Enhanced Voice Assistant", font=("Arial", 24))
        self.label.pack(pady=20)
        self.text_area = ctk.CTkTextbox(master, width=450, height=250)
        self.text_area.pack(pady=10)
        self.listen_button = ctk.CTkButton(master, text="Listen", command=self.start_listening)
        self.listen_button.pack(pady=10)
        self.assistant.speak("Welcome to the Enhanced Voice Assistant sir. How can I assist you sir?")

    def start_listening(self):
        self.listen_button.configure(state="disabled")
        threading.Thread(target=self.process_command).start()

    def process_command(self):
        command = self.assistant.listen()
        response = self.execute_command(command)
        self.text_area.insert("end", f"You: {command}\nAssistant: {response}\n\n")
        self.assistant.speak(response)
        self.listen_button.configure(state="normal")

    def execute_command(self, command):
        if "date" in command:
            return self.assistant.get_date()
        elif "time" in command:
            return self.assistant.get_time()
        elif "weather" in command or "whether" in command:
            if "weather in" in command:
                location = command.split("weather in ")[-1]
            elif "whether in" in command:
                location = command.split("whether in ")[-1]
            else:
                location = command.split("weather of ")[-1] if "weather of" in command else command.split("whether of ")[-1]
            query = f"What is the weather in {location}"
            self.assistant.search_google(query)
            return self.assistant.read_google_search_results(query)
        elif "open" in command:
            app = command.split("open ")[-1]
            return self.assistant.open_application(app)
        elif "system info" in command:
            return self.assistant.get_system_info()
        elif "open file" in command:
            file_path = command.split("open file ")[-1]
            return self.assistant.open_file(file_path)
        elif "open folder" in command:
            folder_path = command.split("open folder ")[-1]
            return self.assistant.open_folder(folder_path)
        elif any(keyword in command for keyword in ["search", "find", "look up", "what is", "who is", "how to"]):
            return self.assistant.search_google(command)
        else:
            return self.assistant.search_google(command)

    def on_closing(self):
        self.assistant.speak("Thank you, Sir. Have a nice day.")
        self.master.destroy()

if __name__ == "__main__":
    root = ctk.CTk()
    app = AssistantGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
