from PyPDF2 import PdfReader

# skill list
skills_list = [
    "python",
    "java",
    "c++",
    "html",
    "css",
    "javascript",
    "sql",
    "machine learning",
    "data analysis",
    "flask"
]

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text.lower()


def analyze_resume(file_path):
    text = extract_text_from_pdf(file_path)

    detected_skills = []
    missing_skills = []

    for skill in skills_list:
        if skill in text:
            detected_skills.append(skill)
        else:
            missing_skills.append(skill)

    return detected_skills, missing_skills