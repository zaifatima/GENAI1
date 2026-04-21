from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

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
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional songwriter."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9
    )

    return response.choices[0].message.content
