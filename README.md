🌐 Live Demo: https://ai-resume-analyzer-t9uc.onrender.com
# 🤖 ResumeAI — AI Resume Analyzer

> An intelligent web application that analyzes resumes, detects skills, calculates ATS match scores, and provides recommendations — built with Python, Flask, and NLP.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=flat-square&logo=flask&logoColor=white)
![PyPDF2](https://img.shields.io/badge/PyPDF2-3.0-red?style=flat-square)
![Chart.js](https://img.shields.io/badge/Chart.js-4.x-FF6384?style=flat-square&logo=chart.js&logoColor=white)

---

## ✨ Features

- 📄 **PDF Resume Upload** — Upload any resume in PDF format
- 🔍 **Skill Detection** — Automatically identifies technical skills in the resume
- ⚠️ **Missing Skill Recommendations** — Highlights skills to add for better job fit
- 📊 **Resume Score** — Calculates a score based on detected skills
- 🎯 **ATS Match Score** — Compares resume against a job description for job matching
- 📈 **Visual Dashboard** — Doughnut chart, progress bars, and skill breakdown

---

## 🖥️ Demo

| Upload Page | Results Dashboard |
|---|---|
| Upload PDF + paste job description | Skill analysis, ATS score, charts |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| PDF Parsing | PyPDF2 |
| Frontend | HTML, CSS, JavaScript |
| Charts | Chart.js |
| NLP | Keyword-based skill matching |

---

## 📁 Project Structure
```
resume-analyzer/
│
├── app.py                  # Flask backend + analysis logic
├── model.py                # Skill extraction module
├── requirements.txt        # Project dependencies
│
├── templates/
│   ├── index.html          # Upload page
│   └── result.html         # Results dashboard
│
├── static/
│   └── style.css           # Styles
│
└── uploads/                # Uploaded resumes (auto-created)
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/itzswathinagaraj/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
python app.py
```

### 4. Open in browser
```
http://127.0.0.1:5000
```

---

## 📦 Requirements
```
flask
PyPDF2
gunicorn
```

---

## 💡 How It Works

1. User uploads a **PDF resume**
2. User pastes a **job description**
3. The app **extracts text** from the PDF using PyPDF2
4. Skills are **matched** against a predefined skill list
5. **ATS score** is calculated by comparing resume words vs job description words
6. Results are displayed with **charts and skill tags**

---

## 📌 Skills Currently Detected

`Python` `Java` `HTML` `CSS` `JavaScript` `React` `Flask` `SQL` `Machine Learning`

> You can easily extend this list in `app.py` to include more skills.

---

## 🌐 Deployment

This project can be deployed on [Render](https://render.com) for free.

Start command:
```bash
gunicorn app:app
```

---

## 👩‍💻 Author

**Swathi N**
- LinkedIn: [linkedin.com/in/itsswathinagaraj](https://linkedin.com/in/itsswathinagaraj)
- GitHub: [itzswathinagaraj](https://github.com/itzswathinagaraj)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built as a portfolio project to demonstrate Flask, NLP, and full-stack web development skills.*

