from voice_io import speak, listen_for_command
from ai_core import get_ai_response
from visuals import JarvisVisuals
import sys, threading
import time

def run_jarvis(visuals):
    time.sleep(1.5)
    speak("System online. Hello. How may I assist you?", visuals=visuals)

    while True:
        user_query = listen_for_command(visuals=visuals)

        if not user_query:
            continue

        if "exit" in user_query or "goodbye" in user_query:
            speak("Goodbye. Shutting down system.", visuals=visuals)
            visuals.root.quit()
            break

        if user_query:
            ai_answer = get_ai_response(user_query)
            speak(ai_answer, visuals=visuals)

if __name__ == '__main__':
    jarvis_visuals = JarvisVisuals()

    logic_thread = threading.Thread(target=run_jarvis, args=(jarvis_visuals,))
    logic_thread.daemon = True
    logic_thread.start()

    try:
        jarvis_visuals.start_gui_loop()
    except Exception as e:
        print(f"An unexpected GUI error occurred: {e}")
    finally:
        print("J.A.R.V.I.S. system fully terminated.")
        sys.exit(0)