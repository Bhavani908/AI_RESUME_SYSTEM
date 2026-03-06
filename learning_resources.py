# Calculates resume strength score
def calculate_resume_score(resume_text):
    important_keywords = [
        "project", "internship", "experience", "skills",
        "team", "leadership", "development", "analysis"
    ]

    score = 0
    for word in important_keywords:
        if word in resume_text:
            score += 12.5   # 8 keywords × 12.5 = 100

    return min(int(score), 100)
