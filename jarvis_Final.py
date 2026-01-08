import speech_recognition as sr
import pyttsx3
import psutil
import os
import webbrowser
from datetime import datetime

# --- VOICE SETUP ---
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 185)
engine.setProperty('volume', 1.0)

def speak(text):
    print(f"🤖 JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

# --- EARS SETUP ---
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"👤 You: {query}")
        return query.lower()
    except:
        return "none"

# --- THE LOGIC CENTER ---
if __name__ == "__main__":
    os.system('cls')
    speak("Final systems check complete. I am fully operational, sir.")

    while True:
        query = take_command()

        if "jarvis" in query:
            # 1. BRAIN: Web Research
            if "open youtube" in query:
                speak("Opening YouTube.")
                webbrowser.open("https://youtube.com")

            elif "google" in query:
                search = query.replace("jarvis", "").replace("google", "").strip()
                speak(f"Searching Google for {search}")
                webbrowser.open(f"https://www.google.com/search?q={search}")

            # 2. SENSORS: System Status
            elif "status" in query:
                cpu = psutil.cpu_percent()
                speak(f"CPU is at {cpu} percent. All systems stable.")

            # 3. UTILITY: Time
            elif "time" in query:
                now = datetime.now().strftime("%I:%M %p")
                speak(f"The current time is {now}")

            # 4. SECURITY: Open your Vault
            elif "vault" in query:
                speak("Decrypting access to the vault.")
                os.system('python vault.py')

            # 5. SHUTDOWN
            elif "terminate" in query or "goodbye" in query:
                speak("Going offline. Sleep mode activated.")
                break