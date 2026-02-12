import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("--- Checking Available Models ---")
try:
    count = 0
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"AVAILABLE: {m.name}")
            count += 1
    
    if count == 0:
        print("CRITICAL ERROR: Your API Key is valid, but has NO access to any text generation models.")
        print("Fix: Go to Google AI Studio -> Create New API Key.")
        
except Exception as e:
    print(f"CONNECTION ERROR: {e}")