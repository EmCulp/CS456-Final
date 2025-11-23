import speech_recognition as sr
import pyttsx3
from gtts import gTTS         
from pydub import AudioSegment 
from pydub.playback import play 
import os                     
import threading 
import time

TEMP_AUDIO_FILE = "response.mp3"

def speak_audio_and_cleanup(text_to_speak, visuals):
    try:
        tts = gTTS(text=text_to_speak, lang='en', slow=False)
        tts.save(TEMP_AUDIO_FILE)

        audio_segment = AudioSegment.from_file(TEMP_AUDIO_FILE, format="mp3")

        if visuals:
            visuals.start_speaking_waveform()
            
        print(f"J.A.R.V.I.S. says: {text_to_speak}")

        play(audio_segment)
        time.sleep(0.5)
    except FileNotFoundError:
        print("FATAL ERROR: FFmpeg (ffplay.exe) is not found. Ensure the FFmpeg 'bin' directory is added to your system PATH.")
    except Exception as e:
        print(f"FATAL TTS/PLAYBACK ERROR (pydub): {e}")

    finally:
        if visuals:
            visuals.stop_speaking_waveform()
        
        if os.path.exists(TEMP_AUDIO_FILE):
            os.remove(TEMP_AUDIO_FILE)

def speak(text: str, visuals=None):
    speech_thread = threading.Thread(target=speak_audio_and_cleanup, args=(text, visuals))
    speech_thread.start()

def listen_for_command(visuals=None) -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if visuals:
            visuals.set_listening_mode(False)

        r.adjust_for_ambient_noise(source)
        print("Listening...")

        try:
            if visuals:
                visuals.set_listening_mode(True)

            audio = r.listen(source, timeout=5, phrase_time_limit=8)
        
        except sr.WaitTimeoutError:
            print("No speech detected within the timeout.")
            return ""
        finally:
            if visuals:
                visuals.set_listening_mode(False)

    try:
        command = r.recognize_google(audio)
        print(f"User said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""