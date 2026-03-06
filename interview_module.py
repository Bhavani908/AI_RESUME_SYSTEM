def get_mock_questions(role):
    role = role.lower()
    if "data" in role:
        return [
            "Explain what is data cleaning.",
            "What is the difference between INNER JOIN and LEFT JOIN?",
            "Describe a data analysis project."
        ]
    return ["Tell me about yourself", "Explain your project"]

def evaluate_answer(question, answer):
    keywords_map = {
        "data cleaning": ["missing", "duplicates", "null", "inconsistent", "errors"],
        "join": ["table", "match", "common", "rows"],
        "project": ["analysis", "tools", "result", "dataset"]
    }

    score = 0
    feedback = "Good answer."

    for key, words in keywords_map.items():
        if key in question.lower():
            matches = sum(1 for w in words if w in answer)
            score = matches * 6
            if score < 12:
                feedback = "Try mentioning key technical steps and examples."
            elif score < 24:
                feedback = "Good, but add more technical depth."
            else:
                feedback = "Excellent detailed answer!"
            break

    return score, feedback
