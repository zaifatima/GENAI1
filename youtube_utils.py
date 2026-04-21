import os
from googleapiclient.discovery import build
from dotenv import load_dotenv
import isodate

# -----------------------------
# LOAD API KEY
# -----------------------------
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

# -----------------------------
# CREATE CLIENT
# -----------------------------
def get_youtube_client():
    return build("youtube", "v3", developerKey=API_KEY)

# -----------------------------
# SEARCH MUSIC
# -----------------------------
def search_music(youtube, query, region, max_results=50):

    search_response = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=max_results,
        regionCode=region,
        videoDuration="medium"
    ).execute()

    video_ids = [item["id"]["videoId"] for item in search_response["items"]]

    video_details = youtube.videos().list(
        part="contentDetails,snippet",
        id=",".join(video_ids)
    ).execute()

    def parse_duration(duration):
        try:
            return isodate.parse_duration(duration).total_seconds()
        except:
            return 0

    videos = []

    for item in video_details["items"]:
        try:
            videos.append({
                "title": item["snippet"]["title"],
                "url": f"https://www.youtube.com/watch?v={item['id']}",
                "duration": parse_duration(item["contentDetails"]["duration"]),
                "channel": item["snippet"]["channelTitle"]
            })
        except:
            continue

    return videos

# -----------------------------
# EXPLANATION FUNCTION
# -----------------------------
def explain(video, mood, language):
    title = video["title"].lower()
    channel = video.get("channel", "").lower()

    reasons = []

    if mood in title:
        reasons.append(f"matches your {mood} mood")

    if language.lower() in title:
        reasons.append(f"in {language} language")

    if "official" in title:
        reasons.append("official music video")

    if "vevo" in channel:
        reasons.append("verified artist channel")

    if any(x in channel for x in ["t-series", "sony", "zee", "yrf", "saregama"]):
        reasons.append("major music label")

    if not reasons:
        reasons.append("relevant to your preferences")

    return "🎯 Recommended because it " + ", ".join(reasons) + "."