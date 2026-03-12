from flask import Flask, render_template, request
import os
from PyPDF2 import PdfReader

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]
    job_desc = request.form.get("jobdesc", "")

    if file.filename == "":
        return "No file selected"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    reader = PdfReader(filepath)
    resume_text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            resume_text += content

    skills = [
    "python", "html", "css", "machine learning",
    "data analysis", "problem solving",
    "communication", "teamwork", "web development",
    "artificial intelligence", "deep learning"
    ]

    found_skills = []
    missing_skills = []

    for skill in skills:
        if skill.lower() in resume_text.lower():
            found_skills.append(skill)
        else:
            missing_skills.append(skill)

    score = len(found_skills) * 10
    if score > 100:
        score = 100

    # ATS match
    resume_words = set(resume_text.lower().split())
    job_words = set(job_desc.lower().split())
    matched = resume_words.intersection(job_words)
    ats_score = int((len(matched) / len(job_words)) * 100) if len(job_words) > 0 else 0
    if ats_score > 100:
        ats_score = 100

    return render_template(
        "result.html",
        skills=found_skills,
        missing=missing_skills,
        score=score,
        ats=ats_score
    )


if __name__ == "__main__":
    app.run(debug=True)