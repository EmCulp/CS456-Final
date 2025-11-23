from voice_io import speak, listen_for_command
from ai_core import get_ai_response
from visuals import JarvisVisuals
import sys, threading
import time

GUI_UPDATE_INTERVAL_MS = 100

def run_jarvis(visuals):
    time.sleep(1.5)
    speak("System online. Hello. How may I assist you?", visuals=visuals)

    while True:
        user_query = listen_for_command(visuals=visuals)

        if not user_query:
            continue

        if "exit" in user_query or "goodbye" in user_query or "shutdown" in user_query:
            speak("Goodbye. Shutting down system.", visuals=visuals)
            visuals.root.quit()
            sys.exit()

        if user_query:
            ai_answer = get_ai_response(user_query)
            speak(ai_answer, visuals=visuals)

def start_logic_and_gui(visuals):
    """Initializes the GUI, sets up the update loop, and starts the logic."""
    
    visuals.root.after(GUI_UPDATE_INTERVAL_MS, lambda: visuals.root.after(GUI_UPDATE_INTERVAL_MS, run_jarvis, visuals))
    
    # Start the Tkinter main loop, which blocks and handles all events
    try:
        visuals.start_gui_loop()
    except Exception as e:
        print(f"An unexpected GUI error occurred: {e}")

if __name__ == '__main__':
    jarvis_visuals = JarvisVisuals()

    # logic_thread = threading.Thread(target=run_jarvis, args=(jarvis_visuals,))
    # logic_thread.daemon = True
    # logic_thread.start()

    try:
        run_jarvis(jarvis_visuals)
    except Exception as e:
        print(f"An unexpected GUI error occurred: {e}")
    finally:
        print("J.A.R.V.I.S. system fully terminated.")
        sys.exit(0)