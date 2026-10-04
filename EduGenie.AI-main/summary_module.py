import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def summarize_text(text: str) -> str:
    try:
        model = genai.GenerativeModel("gemini-3.8-flash")
        prompt = f"Summarize the following content in 3 key bullet points:\n\n{text}"
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error in Summary: {e}"