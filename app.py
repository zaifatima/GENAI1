import streamlit as st
from youtube_utils import get_youtube_client, search_music, explain
from textblob import TextBlob
from lyrics_generator import generate_lyrics

st.set_page_config(page_title="AI Mood Music", layout="wide")

# -----------------------------
# UI STYLE
# -----------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom, #121212, #000000);
    color: white;
}
.main-title {
    text-align: center;
    font-size: 36px;
    font-weight: 700;
}
.sub-title {
    text-align: center;
    color: #b3b3b3;
}
.section {
    background: #111;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 20px;
}
.stButton button {
    background-color: #1DB954;
    color: white;
    border-radius: 25px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("<div class='main-title'>🎧 Mood Music</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>AI-powered songs based on your mood</div>", unsafe_allow_html=True)

youtube = get_youtube_client()

# -----------------------------
# LANGUAGE
# -----------------------------
language = st.selectbox("🌍 Select Language", ["English", "Hindi", "Korean", "Arabic", "Spanish"])

language_map = {
    "English": {"region": "US", "base": "english song official video"},
    "Hindi": {"region": "IN", "base": "hindi song official video"},
    "Korean": {"region": "KR", "base": "kpop song official video"},
    "Arabic": {"region": "AE", "base": "arabic song official video"},
    "Spanish": {"region": "ES", "base": "spanish song official video"},
}

# -----------------------------
# MOOD INPUT
# -----------------------------
energy = st.radio("⚡ Energy", ["Low", "Medium", "High"], horizontal=True)
emotion = st.radio("💭 Mood", ["Sad", "Neutral", "Happy"], horizontal=True)
vibe = st.radio("🎧 Vibe", ["Relax", "Love", "Party", "Stress"], horizontal=True)

# -----------------------------
# MOOD LOGIC
# -----------------------------
def detect_mood():
    if vibe == "Love":
        return "romantic"
    if vibe == "Stress":
        return "anxious"
    if emotion == "Sad":
        return "heartbroken"
    if energy == "High":
        return "energetic"
    if energy == "Low":
        return "chill"
    return "happy"

mood = detect_mood()

st.markdown(f"### 🎯 Detected Mood: **{mood.upper()}**")

# -----------------------------
# SONG RECOMMENDATION
# -----------------------------
if st.button("🎶 Recommend Songs"):
    query = f"{mood} {language_map[language]['base']}"
    region = language_map[language]["region"]

    results = search_music(youtube, query, region)

    st.markdown("## 🎧 Your Playlist")

    for video in results[:6]:
        st.video(video["url"])
        st.caption(video["title"])
        st.write(explain(video, mood, language))

# -----------------------------
# 🎤 LYRICS SECTION
# -----------------------------
st.markdown("## 🎤 Generate Lyrics")

theme = st.text_input("Enter theme (e.g. self growth, heartbreak, love)")

if st.button("Generate Lyrics"):
    lyrics = generate_lyrics(mood, theme, language)
    st.text_area("Your Lyrics", lyrics, height=300)
