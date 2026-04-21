def mood_from_questions(energy, valence):
    if valence > 0.7:
        return "happy"
    elif valence < 0.3:
        return "sad"
    elif energy > 0.7:
        return "energetic"
    else:
        return "chill"
