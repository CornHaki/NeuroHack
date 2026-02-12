import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_llm(model_type="groq"):
    """
    Factory to get the LLM.
    Using Groq's Llama 3.3 for high speed and free tier limits.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY missing in .env")

    return ChatGroq(
        temperature=0,
        model_name="llama-3.3-70b-versatile", 
        groq_api_key=api_key
    )