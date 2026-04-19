import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import PyPDF2
import re

# -------------------------------
# CLEAN TEXT
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

# -------------------------------
# PDF TEXT EXTRACTION
# -------------------------------
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

# -------------------------------
# SKILL DATABASE
# -------------------------------
skills_list = [
    "python", "machine learning", "deep learning", "data analysis",
    "nlp", "sql", "tensorflow", "pytorch", "pandas", "numpy",
    "statistics", "data science", "ai", "excel", "power bi",
    "java", "c++", "html", "css", "javascript", "react"
]

# -------------------------------
# JOB DATA (UPDATED 🔥)
# -------------------------------
job_data = [
    {
        "title": "Data Scientist",
        "skills": ["python", "pandas", "numpy", "machine learning", "statistics", "nlp"],
        "desc": "Analyze data, build ML models, and generate insights."
    },
    {
        "title": "Machine Learning Engineer",
        "skills": ["python", "deep learning", "tensorflow", "pytorch", "ai"],
        "desc": "Build and deploy ML models in production systems."
    },
    {
        "title": "Backend Developer",
        "skills": ["java", "sql", "api", "backend"],
        "desc": "Develop server-side applications and APIs."
    },
    {
        "title": "Web Developer",
        "skills": ["html", "css", "javascript", "react"],
        "desc": "Build responsive web applications."
    }
]

# -------------------------------
# UI
# -------------------------------
st.title("💼 Intelligent Job Recommendation System")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
resume_text = st.text_area("Or paste your resume text:")

# -------------------------------
# PROCESS
# -------------------------------
if st.button("Get Recommendations"):

    # INPUT
    if uploaded_file:
        resume = extract_text_from_pdf(uploaded_file)
    elif resume_text.strip():
        resume = resume_text
    else:
        st.warning("Please upload or enter resume")
        st.stop()

    # CLEAN
    resume = clean_text(resume)

    # -------------------------------
    # SKILL EXTRACTION
    # -------------------------------
    found_skills = []
    for skill in skills_list:
        if skill in resume:
            found_skills.append(skill)

    st.subheader("🔍 Extracted Skills")
    st.write(found_skills)

    resume_skills_text = " ".join(found_skills)

    # -------------------------------
    # MATCHING
    # -------------------------------
    job_titles = [job["title"] for job in job_data]
    job_skills_text = [" ".join(job["skills"]) for job in job_data]

    documents = [resume_skills_text] + job_skills_text

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(X[0:1], X[1:])
    scores = similarity[0]

    sorted_indices = np.argsort(scores)[::-1]

    # -------------------------------
    # OUTPUT
    # -------------------------------
    st.success("✅ Recommendations generated!")
    st.subheader("🎯 Top Job Matches")

    for rank, i in enumerate(sorted_indices):

        percentage = scores[i] * 100
        job = job_data[i]

        st.markdown(f"### {rank+1}. {job['title']}")
        st.progress(float(scores[i]))
        st.write(f"Match Score: {percentage:.1f}%")

        # Description
        st.write(f"📝 {job['desc']}")

        # -------------------------------
        # SKILL GAP ANALYSIS 🔥
        # -------------------------------
        missing_skills = []

        for skill in job["skills"]:
            if skill not in found_skills:
                missing_skills.append(skill)

        if missing_skills:
            st.write("⚠️ Missing Skills:")
            st.write(missing_skills)
        else:
            st.write("✅ You have all required skills!")

        st.markdown("---")