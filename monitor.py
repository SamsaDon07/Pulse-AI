import psutil
import os
import time
import pyttsx3

# --- FORCED DRIVER INITIALIZATION ---
try:
    # 'sapi5' is the official Windows 10/11 speech driver
    engine = pyttsx3.init('sapi5') 
except:
    engine = pyttsx3.init() # Fallback if sapi5 is weird

engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0) # 100% volume

def speak(text):
    print(f"\n🤖 JARVIS: {text}")
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Voice Error: {e}")

def get_bar(percent):
    filled = int(percent / 5)
    bar = "█" * filled + "-" * (20 - filled)
    return f"[{bar}] {percent}%"

def start_monitor():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🛡️  PULSE-AI SYSTEM ONLINE")
    speak("Guardian is online and monitoring.")

    while True:
        cpu = psutil.cpu_percent(interval=0.8)
        ram = psutil.virtual_memory().percent

        os.system('cls' if os.name == 'nt' else 'clear')
        print("🚀 --- PULSE-AI LIVE DASHBOARD --- 🚀")
        print(f"CPU LOAD:  {get_bar(cpu)}")
        print(f"RAM USAGE: {get_bar(ram)}")
        print("-" * 40)
        
        # Trigger at 20% for testing
        if cpu > 20:
            speak(f"Alert. CPU usage is rising. Currently at {int(cpu)} percent.")
            time.sleep(2) # Prevent JARVIS from stuttering
        
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        start_monitor()
    except KeyboardInterrupt:
        print("\n[!] Dashboard Stopped.")