# GRANDMA.md

## How My Project Works (Simple Explanation)

Hi Grandma,

Let me explain how my project works in very simple words.


## What happens when someone uses my app?

1. The user opens the app
2. They answer a few questions like:

   * How they feel (happy, sad, stressed)
   * What kind of vibe they want
3. They can also type about their day (optional)

The app uses this to understand their mood.

## How it suggests songs

* The app takes the mood (like "happy" or "heartbroken")
* It searches YouTube for songs matching that mood
* It filters out bad results (like long playlists or random videos)
* Then it shows the best songs

So it’s like a smart music search.


## How it generates lyrics
Else there is a generate lyrics as you scroll down just by asking you a theme.
If you want in a specific language or mood than :
click << button on the left side of the screen click lyrics(if you want it in other languages(english/hindi)
* The app sends a message to an AI (Gemini) (using Gemini API)
* It tells the AI:
  * mood
  * theme
  * language
* The AI writes a brand new song
So the app doesn’t write lyrics itself — it asks a smart AI to do it (Gemini in this case).
## What are API keys?
API keys are like secret passwords that let my app talk to other services.
Without them, the app cannot work.
## APIs I used
### 1. Gemini API (for lyrics)
* This is the AI that writes songs
* I got it from Google AI Studio
* I created a key and added it to my app
Used for:
* generating lyrics
2. YouTube API (for songs)
* This helps my app search YouTube
* I got it from Google Cloud Console
Used for:
* finding music videos
## Where I stored the keys
I did NOT put them directly in my code (for safety)
Instead, I used:
(GEMINI_API_KEY = "...")
(YOUTUBE_API_KEY = "...")
These are stored securely in Streamlit secrets.
## How everything connects (coding part)
* User gives mood → app understands feeling
* App → searches YouTube → shows songs
* App → asks AI → generates lyrics
So everything works together like a team.
## In one line
My app understands feelings, finds music, and writes songs using AI.
# Important Code Explained (Simple)
Let me explain the main parts of my code and how they work together.
Note:Everything in () is a line from the code
The repository looks like this:
## Starting the App (app.py)
This is the main file.
It:
* shows the app on screen
* takes user input
* connects everything together
Think of this as the brain of the app.
## Mood Detection
In the code, we decide the mood using simple rules:
(if vibe == "Love": return "romantic")
This means:
* If user selects “Love” → mood becomes “romantic”
Other checks:
* Sad → heartbroken
* High energy → energetic
* Low energy → chill
So the app converts answers into one clear mood.
## YouTube Music Search (youtube_utils.py)
This file talks to YouTube.
### Important function:
(search_music(youtube, query, region))
What it does:
* Takes a search like “happy English songs”
* Sends it to YouTube
* Gets video results back
### Cleaning results:
(if video["duration"] > 900: return False)
Removes:
* very long videos
* playlists
* unwanted content
### Ranking system:
(if "official" in title: s += 5)
Gives higher score to:
* official songs
* trusted channels
So users see better quality songs first.
## Gemini Lyrics Generator (lyrics_generator.py)
This is where AI is used.
### Key line:
(response = client.models.generate_content(model="gemini-flash-latest", contents=prompt))
What happens here:
* We send a message (prompt) to Gemini AI
* The AI writes lyrics
* We get the result back
### Prompt example:
("Write powerful original song lyrics. Mood: happy Theme: love")
This tells the AI:
* what kind of song to write
* what feeling to include
## Connecting Everything Together

### Step 1:

User selects mood + language

### Step 2:

App detects mood

### Step 3 (Music):

App → YouTube API → gets songs → filters → shows videos

### Step 4 (Lyrics):

App → Gemini API → generates lyrics → shows them


## Simple flow

User → App → Mood → YouTube (songs) → Gemini (lyrics) → Results

## Simple working idea

Think of the app like a team:

* app.py → manager
* YouTube API → music finder
* Gemini → songwriter

They all work together to help the user.

## Final understanding

My code:

* understands feelings
* finds music
* creates lyrics
* shows everything in one app

That’s it.


All images are available in images.docs folder


