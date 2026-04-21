# GENAI1
# AI Mood Music & Lyrics Generator

An AI-powered web app that recommends music based on your mood and generates original song lyrics using **Google Gemini AI**.

Built with **Streamlit**, this app combines mood detection, music discovery, and creative AI into one smooth experience.

---

## Features

### Mood-Based Music Recommendation

* Detects your mood using:

  * Multiple-choice inputs (energy, vibe, emotion)
  * Optional text sentiment analysis
* Recommends songs using YouTube search
* Filters out:

  * Playlists
  * Long videos
  * Irrelevant results
* Smart ranking for better suggestions

---

### AI Lyrics Generator

* Generates original lyrics based on:

  * Mood
  * Theme
  * Language
* Uses **Google Gemini (gemini-flash-latest)** model
* Structured output:

  * Verse 1
  * Chorus
  * Verse 2

---

### Multi-language Support

* English
* Hindi
* Korean
* Arabic
* Spanish

---

## Tech Stack

* **Frontend & App Framework:** Streamlit
* **AI Model:** Google Gemini API (`google-genai`)
* **NLP:** TextBlob (sentiment analysis)
* **YouTube Data:** YouTube Data API v3
* **Python Libraries:**

  * streamlit
  * google-genai
  * textblob
  * google-api-python-client

---

## Project Structure

```
genai1/
│
├── app.py                 # Main app (music recommendation)
├── youtube_utils.py       # YouTube API + helper functions
├── lyrics_generator.py    # Gemini AI lyrics generation
│
├── pages/
│   └── lyrics.py          # Lyrics UI page
│
├── requirements.txt
└── README.md
```

---

## API Setup

### 1. Gemini API Key

* Go to Google AI Studio
* Create an API key
* Add to Streamlit secrets:

```toml
GEMINI_API_KEY = "your_key_here"
```

---

### 2. YouTube API Key

* Enable YouTube Data API v3 in Google Cloud Console
* Add to secrets:

```toml
YOUTUBE_API_KEY = "your_key_here"
```

---

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Deployment (Streamlit Cloud)

1. Push project to GitHub
2. Go to Streamlit Cloud
3. Deploy repo
4. Add secrets:

   * `GEMINI_API_KEY`
   * `YOUTUBE_API_KEY`
5. Click **Deploy**

---

## Notes

* Use:

  ```
  model="gemini-flash-latest"
  ```

  to avoid deprecated model errors
* Do NOT expose API keys publicly

---

## Future Improvements

* Playlist creation (Spotify integration)
* Voice mood detection
* Lyrics-to-audio generation
* Save favorite songs

---

## Author

**Zainab Fatima**

---

## 🌟 If you like this project

Give it a ⭐ on GitHub!
