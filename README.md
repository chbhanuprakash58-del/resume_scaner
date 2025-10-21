# 🧠 AI Resume–Job Description Analyzer

This project is a **Resume Screening System** that takes a **Job Description (JD)** and a **Resume** as input, analyzes them using AI, and gives a detailed match report including skills matched, missing skills, and overall match score.

---

## Features

- Upload **Resume** (PDF/DOCX) and **Job Description** (PDF/DOCX)
- **AI-powered analysis** for matching resumes with JDs
- Provides:
  - **Match Score** (0-100%)
  - **Matched Skills**
  - **Missing/Weak Skills**
  - **Summary/Explanation**
- Highlights resumes with **strong matches** (≥ 80%)

---

## How It Works

1. **FastAPI Backend** (`read_doc.py`):
   - Extracts text from uploaded PDF or DOCX files
   - Sends text to **Groq AI** for analysis
   - Returns structured JSON with match score, skills, and summary

2. **Streamlit Frontend** (`web_app.py`):
   - Simple web interface for users to upload files
   - Calls FastAPI backend and displays results in a user-friendly format

3. **Environment Variables**:
   - API keys are stored in a `.env` file for security:
     ```text
     GROQ_API_KEY="your_groq_api_key_here"
     ```

---

## Installation & Usage

1. **Clone the repo**:
   ```bash
   git clone https://github.com/chbhanuprakash58-del/resume_scaner.git
   cd resume_scaner
Create a virtual environment & install dependencies:

bash
Copy code
python -m venv venv
source venv/Scripts/activate   # Windows
pip install -r requirements.txt
Create a .env file in project root with your API key:

text
Copy code
GROQ_API_KEY="your_groq_api_key_here"
Run FastAPI backend:

bash
Copy code
uvicorn read_doc:app --reload
Run Streamlit frontend:

bash
Copy code
streamlit run web_app.py
Open the web app in your browser, upload Resume & JD, and get the analysis!

Project Structure
bash
Copy code
Resume_Scanner_Bot/
│
├── read_doc.py       # FastAPI backend
├── web_app.py        # Streamlit frontend
├── requirements.txt  # Python packages
├── .env              # Environment variables (API keys)
└── data/             # (Optional) folder for test files
Notes
Only Resume (PDF/DOCX) and JD (PDF/DOCX) are supported.

API keys must never be pushed to GitHub. Always use .env for security.

Match score ≥ 80% is considered a strong match.

Demo Screenshot
(Optional: Add screenshot of your Streamlit app here)

Author: chbhanuprakash58-del

yaml
Copy code

---

If you want, I can also make a **more visually appealing README** with **badges, GIF preview, and headings** so it looks very professional on GitHub.  

Do you want me to do that?