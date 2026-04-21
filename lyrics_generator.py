import google.generativeai as genai
import streamlit as st

# Configure API
genai.configure(api_key=st.secrets.get("GEMINI_API_KEY"))

def generate_lyrics(mood, theme, language):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash")  # ✅ FIXED MODEL NAME

        prompt = f"""
        Write powerful original song lyrics.

        Mood: {mood}
        Theme: {theme}
        Language: {language}

        Structure:
        Verse 1
        Chorus
        Verse 2

        Make it emotional, catchy, and meaningful.
        """

        response = model.generate_content(prompt)

        return response.text if response.text else "No lyrics generated."

    except Exception as e:
        return "⚠️ Error: Check Gemini API key or model access."
