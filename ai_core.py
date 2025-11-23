from google import genai
import os

API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    # If the key isn't set, print a reminder and use a placeholder
    print("FATAL ERROR: GEMINI_API_KEY environment variable is NOT set.")

try:
    client = genai.Client(api_key=API_KEY)
    GEMINI_MODEL = 'gemini-2.5-flash'
except Exception as e:
    print(f"Error initializing Gemini Client: {e}")
    print("ACTION REQUIRED: Ensure GEMINI_API_KEY environment variable is set.")
    client = None

def get_ai_response(prompt: str) -> str:
    if not client:
        return "I'm sorry, my core intelligence module is offline. Please check my API key."
    
    try:
        if not API_KEY:
            return "Error: API Key is missing. Check terminal for instructions"
        
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config={"tools": [{"google_search": {}}]}
        )
        return response.text
    except Exception as e:
        print(f"AI Core Error: {e}")
        return "I encountered a processing error while fetching the information."
    
if __name__ == '__main__':
    # This block allows you to test the AI Core independently
    test_prompt = "What are the three most important things I need for a basic Python voice assistant?"
    print(f"Testing AI with: '{test_prompt}'")
    ai_answer = get_ai_response(test_prompt)
    print(f"\nAI Response:\n{ai_answer}")