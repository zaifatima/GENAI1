from google import genai
import streamlit as st

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def generate_lyrics(mood, theme, language):
    try:
        prompt = f"""
        Write powerful original song lyrics.

        Mood: {mood}
        Theme: {theme}
        Language: {language}

        Structure:
        Verse 1
        Chorus
        Verse 2

        Make it emotional and meaningful.
        """

        response = client.models.generate_content(
            model="gemini-1.5-flash",   # ✅ NO "models/"
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"⚠️ Error: {str(e)}"
