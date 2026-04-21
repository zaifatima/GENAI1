import streamlit as st
from lyrics_generator import generate_lyrics

st.set_page_config(page_title="Lyrics Generator")

st.title("🎤 AI Lyrics Generator")

mood = st.selectbox(
    "Select Mood",
    [
        "self growth",
        "self doubt",
        "heartbroken",
        "in love",
        "in pain",
        "go with the flow",
        "romantic",
        "failed",
        "success",
        "calm"
    ]
)

language = st.selectbox("Language", ["English", "Hindi"])

theme = st.text_input("Theme (e.g. love, success, memories)")

if st.button("Generate Lyrics"):
    if not theme:
        st.warning("Enter a theme")
    else:
        with st.spinner("Writing lyrics..."):
            lyrics = generate_lyrics(mood, theme, language)

        st.text_area("Your Lyrics", lyrics, height=300)