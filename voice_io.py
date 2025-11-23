import speech_recognition as sr
import threading 
import time
import pyttsx3
from queue import Queue

input_queue = Queue()

try:
    tts_engine = pyttsx3.init('sapi5')
    rate = tts_engine.getProperty('rate')
    tts_engine.setProperty('rate', rate+20)
except Exception as e:
    print(f"FATAL ERROR: Could not initialize SAPI5 TTS engine: {e}")
    tts_engine = None

TEMP_AUDIO_FILE = "response.mp3"

def speak_audio_and_cleanup(text_to_speak, visuals):
    if not tts_engine:
        print("Speech engine not available")
        return
    
    try:
        print(f"ATLAS says: {text_to_speak}")

        tts_engine.say(text_to_speak)
        tts_engine.runAndWait()
    except Exception as e:
        print(f"RATAL SAPI5 PLAYBACK ERROR: {e}")

def speak(text: str, visuals=None):
    pass

def listen_for_input_blocking():
    """Function to run on a dedicated thread to wait for input."""
    try:
        # This is the line that blocks, now safely on its own thread
        command = input("\nATLAS is listening: ")
        input_queue.put(command.strip())
    except EOFError:
        input_queue.put("exit")
    except KeyboardInterrupt:
        input_queue.put("exit")

def listen_for_command(visuals=None) -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if input_queue.empty():
            # Start a new thread just for the input() call
            input_thread = threading.Thread(target=listen_for_input_blocking)
            input_thread.daemon = True
            input_thread.start()

        try:
            command = input("\nATLAS is listening: ")
            return command.lower().strip()
        except:
            return ""

    try:
        return command.lower().strip()
        
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""