import streamlit as st
from youtube_utils import get_youtube_client, search_music, explain
from textblob import TextBlob

st.set_page_config(page_title="AI Mood Music", layout="wide")

# -----------------------------
# PREMIUM UI STYLE
# -----------------------------
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(to bottom, #121212, #000000);
    color: white;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 36px;
    font-weight: 700;
    margin-bottom: 5px;
}

.sub-title {
    text-align: center;
    color: #b3b3b3;
    margin-bottom: 30px;
}

/* Card */
.music-card {
    background: #181818;
    border-radius: 16px;
    padding: 15px;
    margin-bottom: 25px;
    transition: 0.3s;
}

.music-card:hover {
    background: #242424;
    transform: translateY(-5px);
}

/* Title */
.music-title {
    font-size: 15px;
    font-weight: 600;
    margin-top: 10px;
}

/* Channel */
.music-channel {
    font-size: 12px;
    color: #aaa;
}

/* Explanation */
.music-reason {
    font-size: 12px;
    color: #1db954;
    margin-top: 8px;
}

/* Section box */
.section {
    background: #111;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 20px;
}

/* Button */
.stButton button {
    background-color: #1DB954;
    color: white;
    border-radius: 25px;
    padding: 10px 25px;
    border: none;
    font-weight: 600;
}

.stButton button:hover {
    background-color: #1ed760;
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
st.markdown("<div class='section'>", unsafe_allow_html=True)

language = st.selectbox(
    "🌍 Select Language",
    ["English", "Hindi", "Korean", "Arabic", "Spanish"]
)

language_map = {
    "English": {"region": "US", "base": "english song official video"},
    "Hindi": {"region": "IN", "base": "hindi song official video"},
    "Korean": {"region": "KR", "base": "kpop song official video"},
    "Arabic": {"region": "AE", "base": "arabic song official video"},
    "Spanish": {"region": "ES", "base": "spanish song official video"},
}

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# MOOD (MCQ)
# -----------------------------
st.markdown("<div class='section'>", unsafe_allow_html=True)

st.markdown("### 🧠 Answer a few quick questions")

col1, col2 = st.columns(2)

with col1:
    energy = st.radio(
        "⚡ Energy Level",
        ["Low", "Medium", "High"],
        horizontal=True
    )

    vibe = st.radio(
        "🎧 What vibe are you looking for?",
        ["Relax", "Love", "Party", "Stress"],
        horizontal=True
    )

with col2:
    emotion = st.radio(
        "💭 Current Mood",
        ["Sad", "Neutral", "Happy"],
        horizontal=True
    )

st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# MOOD DETECTION LOGIC
# -----------------------------
def detect_mood_mcq():
    # Priority-based logic (strong signals first)

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

# -----------------------------
# TEXT INPUT
# -----------------------------
st.markdown("<div class='section'>", unsafe_allow_html=True)

user_text = st.text_area("✍️ Describe your day (optional)")

st.markdown("</div>", unsafe_allow_html=True)

def detect_mood_text(text):
    if not text:
        return None

    polarity = TextBlob(text).sentiment.polarity
    text = text.lower()

    if "love" in text:
        return "romantic"
    if "break" in text:
        return "heartbroken"
    if "stress" in text:
        return "anxious"

    if polarity > 0.4:
        return "happy"
    elif polarity < -0.4:
        return "sad"

    return None

# -----------------------------
# FINAL MOOD
# -----------------------------
mood = detect_mood_text(user_text) or detect_mood_mcq()

st.markdown(f"""
<div style='text-align:center; margin:20px 0; font-size:18px;'>
🎯 Detected Mood: <b>{mood.upper()}</b>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# BUILD QUERY
# -----------------------------
def build_query():
    base = language_map[language]["base"]
    return f"{mood} {base}"

# -----------------------------
# FILTER
# -----------------------------
def is_good(video):
    title = video["title"].lower()

    bad = ["playlist", "mix", "mashup", "hour", "jukebox"]
    if any(x in title for x in bad):
        return False

    if video["duration"] > 900:
        return False

    return True

def is_correct_language(video):
    title = video["title"].lower()

    if language == "English":
        bad = ["hindi", "bollywood", "punjabi"]
        return not any(x in title for x in bad)

    if language == "Hindi":
        return "hindi" in title or "song" in title

    return True

# -----------------------------
# RANKING
# -----------------------------
def score(video):
    title = video["title"].lower()
    channel = video.get("channel", "").lower()

    s = 0

    if "official" in title:
        s += 5

    if "vevo" in channel:
        s += 4

    if any(x in channel for x in ["t-series", "sony", "zee"]):
        s += 4

    if mood in title:
        s += 2

    return s

# -----------------------------
# BUTTON
# -----------------------------
if st.button("🎶 Recommend Songs"):

    query = build_query()
    region = language_map[language]["region"]

    with st.spinner("🎧 Finding your perfect playlist..."):
        results = search_music(youtube, query, region)

    filtered = [
        v for v in results
        if is_good(v) and is_correct_language(v)
    ]

    ranked = sorted(filtered, key=lambda x: score(x), reverse=True)
    final = ranked[:10]

    st.markdown("## 🎧 Your Playlist")

    cols = st.columns(2)

    for i, video in enumerate(final):
        with cols[i % 2]:

            st.markdown('<div class="music-card">', unsafe_allow_html=True)

            st.video(video["url"])

            st.markdown(f"""
            <div class="music-title">{video['title']}</div>
            <div class="music-channel">{video.get('channel','')}</div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="music-reason">
            {explain(video, mood, language)}
            </div>
            """, unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)