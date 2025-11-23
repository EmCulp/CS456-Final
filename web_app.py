# app.py

import sys
from flask import Flask, render_template, request, jsonify
from ai_core import get_ai_response
# Import a basic placeholder function for the "speak" step
from voice_io import speak 

# --- FLASK SETUP ---
app = Flask(__name__)

# This list will hold the conversation history to display in the UI
conversation_history = [
    {"speaker": "ATLAS", "text": "System online. Hello. How may I assist you?"}
]

@app.route("/", methods=["GET"])
def index():
    """Renders the main chat interface, passing the history."""
    return render_template("index.html", history=conversation_history)

@app.route("/chat", methods=["POST"])
def chat():
    """Handles the user's command, gets the AI response, and updates history."""
    global conversation_history
    
    # 1. Get user input from the HTML form
    user_query = request.form.get("user_input")
    
    if not user_query:
        return jsonify({"success": False, "message": "No input provided."})

    user_query = user_query.strip()
    
    # 2. Check for exit command
    if "exit" in user_query.lower() or "shutdown" in user_query.lower():
        conversation_history.append({"speaker": "User", "text": user_query})
        ai_answer = "Goodbye. Shutting down system."
        conversation_history.append({"speaker": "ATLAS", "text": ai_answer})
        
        # Note: We can't immediately exit a Flask app elegantly like this, 
        # but the conversation logic is complete.
        return jsonify({"success": True, "answer": ai_answer, "history": conversation_history})
    
    # 3. Process the query
    conversation_history.append({"speaker": "User", "text": user_query})
    
    # Call the AI core (which is now completely decoupled from I/O)
    ai_answer = get_ai_response(user_query)
    
    conversation_history.append({"speaker": "ATLAS", "text": ai_answer})

    # The 'speak' function from voice_io now only prints to the console (backend)
    speak(ai_answer)
    
    # 4. Return the response to update the frontend
    return jsonify({"success": True, "answer": ai_answer, "history": conversation_history})

if __name__ == '__main__':
    # You will run the app using 'flask run' in the terminal
    print("\n------------------------------------------------------------------")
    print("ATLAS is ready! Open your browser to http://127.0.0.1:5000")
    print("Use the terminal command: flask run")
    print("------------------------------------------------------------------\n")
    # app.run(debug=True) # Comment out, we use 'flask run'