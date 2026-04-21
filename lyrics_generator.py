import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-pro")


def generate_lyrics(mood, theme, language):

    prompt = f"""
    Write powerful original song lyrics.

    Mood: {mood}
    Theme: {theme}
    Language: {language}

    Structure:
    - Verse 1
    - Chorus
    - Verse 2

    Make it emotional, catchy, and meaningful.
    Use rhyming and vivid imagery.
    """

    response = model.generate_content(prompt)

    return response.text
