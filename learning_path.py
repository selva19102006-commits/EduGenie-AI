import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def get_learning_recommendations(topic: str) -> str:
    try:
        model = genai.GenerativeModel("gemini-3.8-flash")
        prompt = f"Provide a structured learning path with key topics and resources for: {topic}"
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error occurred: {e}"