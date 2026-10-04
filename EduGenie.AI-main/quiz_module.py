import os
import re
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def clean_json_block(text: str) -> str:
    return re.sub(r"```(?:json)?\n(.*?)```", r"\1", text, flags=re.DOTALL).strip()

def generate_quiz(text: str) -> list:
    try:
        model = genai.GenerativeModel("gemini-3.8-flash")
        prompt = f"""You are a quiz generator.
From the following topic/text, create 3 multiple-choice questions in raw JSON format with keys: "question", "options" (list of 4 strings), and "answer".

Topic: {text}"""
        response = model.generate_content(prompt)
        cleaned_text = clean_json_block(response.text)
        return json.loads(cleaned_text)
    except Exception as e:
        return []