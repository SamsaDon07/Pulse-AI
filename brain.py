import pyttsx3
import psutil

# Initialize the Voice Engine
engine = pyttsx3.init()

# Adjust the voice (Optional: make it faster/slower)
engine.setProperty('rate', 180) 

def jarvis_report():
    # Get current stats
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    
    report = f"System check complete. CPU load is at {cpu} percent. Memory usage is at {ram} percent."
    
    print(f"🤖 Jarvis: {report}")
    engine.say(report)
    engine.runAndWait()

if __name__ == "__main__":
    print("Initializing Voice Assistant...")
    jarvis_report()