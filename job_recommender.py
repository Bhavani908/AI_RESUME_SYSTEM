from job_database import job_roles

def recommend_jobs(resume_text):
    scores = []

    for role, skills in job_roles.items():
        match_count = sum(1 for skill in skills if skill in resume_text)
        similarity = (match_count / len(skills)) * 100
        scores.append((role, round(similarity, 2)))

    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:5]

