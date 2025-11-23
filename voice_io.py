import speech_recognition as sr
# from gtts import gTTS         
# from pydub import AudioSegment 
# from pydub.playback import play 
import os                     
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
        if visuals:
            visuals.start_speaking_waveform()

        print(f"J.A.R.V.I.S. says: {text_to_speak}")

        tts_engine.say(text_to_speak)
        tts_engine.runAndWait()
    except Exception as e:
        print(f"RATAL SAPI5 PLAYBACK ERROR: {e}")
    finally:
        if visuals:
            visuals.stop_speaking_waveform()

def speak(text: str, visuals=None):
    """
    Simulates speech by printing the response. 
    This is the guaranteed final working output method.
    """
    if visuals:
        # Still show the waveform animation if visuals are available
        visuals.start_speaking_waveform()
        
    print(f"J.A.R.V.I.S. says: {text}")
    
    # Simulate the time it would take to speak for a smooth transition
    time.sleep(len(text) / 25) 
    
    if visuals:
        visuals.stop_speaking_waveform()

def listen_for_input_blocking():
    """Function to run on a dedicated thread to wait for input."""
    try:
        # This is the line that blocks, now safely on its own thread
        command = input("\nJ.A.R.V.I.S. is listening: ")
        input_queue.put(command.strip())
    except EOFError:
        input_queue.put("exit")
    except KeyboardInterrupt:
        input_queue.put("exit")

def listen_for_command(visuals=None) -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if visuals:
            visuals.set_listening_mode(False)

        if input_queue.empty():
            # Start a new thread just for the input() call
            input_thread = threading.Thread(target=listen_for_input_blocking)
            input_thread.daemon = True
            input_thread.start()

        try:
            command = input("\nJ.A.R.V.I.S. is listening: ")
            if visuals:
                visuals.set_listening_mode(False)
            return command.lower().strip()
        except:
            return ""

    try:
        return command.lower().strip()
        
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""