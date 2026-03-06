import speech_recognition as sr

def speech_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio).lower()
    except:
        return ""

def evaluate_answer(answer_text, expected_keywords):
    score = 0
    for word in expected_keywords:
        if word in answer_text:
            score += 20
    return min(score, 100)

def get_feedback(score):
    if score > 80:
        return "Excellent answer with good technical explanation."
    elif score > 50:
        return "Good answer but needs more technical depth."
    else:
        return "Answer lacks key concepts. Revise fundamentals."
