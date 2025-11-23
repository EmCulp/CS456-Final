from google import genai
import os

# print(f"DEBUG: GEMINI_API_KEY is present: {'GEMINI_API_KEY' in os.environ}")

try:
    client = genai.Client()
    GEMINI_MODEL = 'gemini-2.5-flash'
except Exception as e:
    print(f"Error initializing Gemini Client: {e}")
    print("ACTION REQUIRED: Ensure GEMINI_API_KEY environment variable is set.")
    client = None

def get_ai_response(prompt: str) -> str:
    if not client:
        return "I'm sorry, my core intelligence module is offline. Please check my API key."
    
    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
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