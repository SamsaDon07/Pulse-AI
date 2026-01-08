import speech_recognition as sr
import pyttsx3
import psutil
import os
import time

# --- SETUP VOICE ---
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)

def speak(text):
    print(f"🤖 JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

# --- SETUP EARS ---
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Listening for 'Jarvis'...")
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("🧠 Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"👤 You: {query}")
        return query.lower()
    except Exception:
        return "none"

# --- SYSTEM CHECK ---
def get_stats():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    speak(f"Sir, the CPU is at {cpu} percent and memory usage is at {ram} percent.")

# --- MAIN LOOP ---
if __name__ == "__main__":
    os.system('cls')
    speak("Systems initialized. I am online and ready, sir.")

    while True:
        query = take_command()

        if "jarvis" in query:
            if "status" in query or "report" in query:
                get_stats()
            
            elif "open vault" in query:
                speak("Accessing the secure vault now.")
                # Make sure your vault.py is in this same folder!
                os.system('python vault.py') 

            elif "goodbye" in query or "sleep" in query:
                speak("Powering down. Have a good day, sir.")
                break
            
            else:
                speak("I am listening. What are your orders?")