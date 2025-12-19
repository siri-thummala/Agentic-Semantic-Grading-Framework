import os
from dotenv import load_dotenv
import google.generativeai as genai

#load_dotenv()

# def call_llm(prompt):
#     api_key = os.getenv("GOOGLE_API_KEY")

#     if not api_key:
#         raise RuntimeError("GOOGLE_API_KEY not set")

#     genai.configure(api_key=api_key)

#     model = genai.GenerativeModel("models/gemini-1.5-flash")

#     response = model.generate_content(prompt)

#     return response.text.strip()"""
def call_llm(prompt):
    """
    Placeholder LLM client.
    Can be replaced with real LLM when API access is available.Replace placeholder with real LLM client once API access is enabled
    """
    return "This reference answer was generated using an LLM placeholder."
