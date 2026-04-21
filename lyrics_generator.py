from google import genai
import streamlit as st

# Initialize Gemini client
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def generate_lyrics(mood, theme, language):
    try:
        prompt = f"""
        Write powerful and original song lyrics.

        Mood: {mood}
        Theme: {theme}
        Language: {language}

        Style:
        - Emotional
        - Catchy
        - Rhyming

        Structure:
        Verse 1
        Chorus
        Verse 2

        Make it feel real and expressive.
        """

        response = client.models.generate_content(
            model="gemini-1.5-flash-latest",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"⚠️ Error: {str(e)}"
