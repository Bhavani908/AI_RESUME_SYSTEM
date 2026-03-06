from flask import Flask, render_template, request, redirect, url_for, session
from database import get_db, init_db
from resume_parser import extract_text_from_pdf, extract_text_from_docx
from job_recommender import recommend_jobs
from skill_gap_ai import detect_skill_gap, recommend_resources
from interview_module import get_mock_questions, evaluate_answer
from job_links import generate_job_links
import speech_recognition as sr
import os

app = Flask(__name__)
app.secret_key = "career_ai_secret"

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

init_db()

# ================= HOME =================
@app.route("/")
def home():
    return redirect(url_for("login"))

# ================= REGISTER =================
@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        db = get_db()

        db.execute(
            "INSERT INTO users(username,password) VALUES (?,?)",
            (username,password)
        )

        db.commit()

        return redirect(url_for("login"))

    return render_template("register.html")


# ================= LOGIN =================
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db()

        user = db.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        ).fetchone()

        if user:
            session["user_id"] = user["id"]
            return redirect("/dashboard")

    return render_template("login.html")


# ================= LOGOUT =================
@app.route("/logout")
def logout():

    session.clear()
    return redirect(url_for("login"))


# ================= DASHBOARD =================
@app.route("/dashboard", methods=["GET","POST"])
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        file = request.files["resume"]

        filepath = os.path.join(UPLOAD_FOLDER,file.filename)
        file.save(filepath)

        if file.filename.endswith(".pdf"):
            resume_text = extract_text_from_pdf(filepath)
        else:
            resume_text = extract_text_from_docx(filepath)

        jobs = recommend_jobs(resume_text)

        role_actions = []

        db = get_db()

        for role, match in jobs:

            job_links = generate_job_links(role)

            if match >= 80:

                db.execute("""
                INSERT INTO resume_history(user_id,filename,role,match_score,gaps,resources)
                VALUES (?,?,?,?,?,?)
                """,(
                    session["user_id"],
                    file.filename,
                    role,
                    match,
                    "",
                    ""
                ))

                db.commit()

                role_actions.append({
                    "role": role,
                    "match": match,
                    "type": "interview",
                    "job_links": job_links
                })

            else:

                gaps = detect_skill_gap(role,resume_text)
                resources = recommend_resources(gaps)

                db.execute("""
                INSERT INTO resume_history(user_id,filename,role,match_score,gaps,resources)
                VALUES (?,?,?,?,?,?)
                """,(
                    session["user_id"],
                    file.filename,
                    role,
                    match,
                    str(gaps),
                    str(resources)
                ))

                db.commit()

                role_actions.append({
                    "role": role,
                    "match": match,
                    "type": "learning",
                    "gaps": gaps,
                    "resources": resources,
                    "job_links": job_links
                })

        return render_template("result.html", role_actions=role_actions)

    return render_template("index.html")


# ================= INTERVIEW =================
@app.route("/start_interview/<role>")
def start_interview(role):

    session["role"] = role
    session["questions"] = get_mock_questions(role)
    session["current_q"] = 0
    session["score"] = 0

    return redirect(url_for("interview_question"))


@app.route("/interview_question")
def interview_question():

    questions = session.get("questions")
    current_q = session.get("current_q",0)

    if current_q >= len(questions):

        final_score = session["score"]
        feedback = session.get("feedback","Good attempt!")

        return render_template(
            "interview_result.html",
            score=final_score,
            feedback=feedback
        )

    return render_template(
        "interview.html",
        question=questions[current_q]
    )


# ================= VOICE ANSWER =================
@app.route("/submit_voice", methods=["POST"])
def submit_voice():

    try:

        file = request.files["audio_data"]
        wav_path = os.path.join(UPLOAD_FOLDER,"answer.wav")
        file.save(wav_path)

        recognizer = sr.Recognizer()

        with sr.AudioFile(wav_path) as source:
            audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio).lower()
        except:
            text = ""

        question = session["questions"][session["current_q"]]

        score, feedback = evaluate_answer(question,text)

        session["score"] += score
        session["feedback"] = feedback
        session["current_q"] += 1

        return {
            "score":score,
            "feedback":feedback,
            "next":url_for("interview_question")
        }

    except:

        return {
            "score":0,
            "feedback":"Audio processing failed",
            "next":url_for("interview_question")
        }


# ================= HISTORY =================
@app.route("/history")
def history():

    if "user_id" not in session:
        return redirect(url_for("login"))

    db = get_db()

    records = db.execute(
        "SELECT * FROM resume_history WHERE user_id=?",
        (session["user_id"],)
    ).fetchall()

    return render_template("history.html", records=records)


# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)