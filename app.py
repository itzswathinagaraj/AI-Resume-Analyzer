from flask import Flask, render_template, request
import os
from PyPDF2 import PdfReader

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Skills for each job role
JOB_ROLES = {
    "Python Developer": [
        "python", "flask", "django", "sql", "html", "css",
        "javascript", "git", "api", "machine learning"
    ],
    "Data Analyst": [
        "python", "sql", "excel", "pandas", "numpy",
        "matplotlib", "power bi", "tableau", "statistics", "data analysis"
    ],
    "Full Stack Developer": [
        "html", "css", "javascript", "react", "nodejs",
        "python", "sql", "git", "api", "mongodb"
    ],
    "Machine Learning Engineer": [
        "python", "machine learning", "deep learning", "tensorflow",
        "keras", "scikit-learn", "numpy", "pandas", "nlp", "data analysis"
    ],
    "Web Developer": [
        "html", "css", "javascript", "react", "bootstrap",
        "git", "api", "nodejs", "sql", "figma"
    ]
}

# Tips based on resume content
def get_tips(text, found_skills):
    tips = []
    if "github" not in text.lower():
        tips.append("Add your GitHub profile link")
    if "linkedin" not in text.lower():
        tips.append("Add your LinkedIn profile link")
    if "project" not in text.lower():
        tips.append("Add a Projects section")
    if "experience" not in text.lower():
        tips.append("Add internship or work experience")
    if "certif" not in text.lower():
        tips.append("Add certifications if you have any")
    if len(found_skills) < 4:
        tips.append("Add more technical skills to your resume")
    return tips

# Course recommendations for missing skills
COURSES = {
    "python": "Python - https://www.learnpython.org",
    "sql": "SQL - https://www.w3schools.com/sql",
    "machine learning": "ML - https://www.coursera.org/learn/machine-learning",
    "html": "HTML - https://www.w3schools.com/html",
    "css": "CSS - https://www.w3schools.com/css",
    "javascript": "JavaScript - https://javascript.info",
    "react": "React - https://react.dev/learn",
    "pandas": "Pandas - https://pandas.pydata.org/docs",
    "numpy": "NumPy - https://numpy.org/learn",
    "deep learning": "Deep Learning - https://www.coursera.org/specializations/deep-learning",
    "tensorflow": "TensorFlow - https://www.tensorflow.org/tutorials",
    "git": "Git - https://learngitbranching.js.org",
    "flask": "Flask - https://flask.palletsprojects.com",
    "django": "Django - https://www.djangoproject.com/start",
    "mongodb": "MongoDB - https://learn.mongodb.com",
    "tableau": "Tableau - https://www.tableau.com/learn/training",
    "power bi": "Power BI - https://learn.microsoft.com/en-us/power-bi",
}

# Strength meter
def get_strength(score):
    if score >= 80:
        return "Excellent", "#7cfa9d"
    elif score >= 60:
        return "Strong", "#7c6dfa"
    elif score >= 40:
        return "Average", "#fad06d"
    else:
        return "Weak", "#fa6d8f"


@app.route("/")
def home():
    roles = list(JOB_ROLES.keys())
    return render_template("index.html", roles=roles)


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["resume"]
    job_desc = request.form.get("jobdesc", "")
    selected_role = request.form.get("role", "Python Developer")

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

    # Role based skill matching
    skills = JOB_ROLES.get(selected_role, JOB_ROLES["Python Developer"])
    found_skills = []
    missing_skills = []

    for skill in skills:
        if skill.lower() in resume_text.lower():
            found_skills.append(skill)
        else:
            missing_skills.append(skill)

    score = int((len(found_skills) / len(skills)) * 100)

    # ATS match
    resume_words = set(resume_text.lower().split())
    job_words = set(job_desc.lower().split())
    matched = resume_words.intersection(job_words)
    ats_score = int((len(matched) / len(job_words)) * 100) if job_words else 0
    if ats_score > 100:
        ats_score = 100

    # Extras
    tips = get_tips(resume_text, found_skills)
    strength, strength_color = get_strength(score)
    course_recs = [COURSES[s] for s in missing_skills if s in COURSES]

    return render_template(
        "result.html",
        skills=found_skills,
        missing=missing_skills,
        score=score,
        ats=ats_score,
        role=selected_role,
        tips=tips,
        strength=strength,
        strength_color=strength_color,
        courses=course_recs
    )


if __name__ == "__main__":
    app.run(debug=True)