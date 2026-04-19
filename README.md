# 💼 Intelligent Job Recommendation System

## 📌 Overview

An end-to-end Machine Learning + NLP based system that recommends suitable job roles based on user resumes. The system extracts skills from resumes, matches them with job descriptions, and provides personalized job recommendations along with skill gap analysis.

---

## 🚀 Features

* Upload resume (PDF) or paste resume text
* Extract key technical skills from unstructured data
* Match resume with job roles using TF-IDF and cosine similarity
* Display job recommendations with match scores
* 🔥 Skill Gap Analysis to identify missing skills
* Interactive and user-friendly UI using Streamlit

---

## 🧠 Tech Stack

* Python
* Scikit-learn
* NumPy
* Streamlit
* PyPDF2
* Natural Language Processing (TF-IDF)

---

## ⚙️ How It Works

1. **Resume Input**

   * User uploads a PDF or enters resume text

2. **Text Processing**

   * Resume text is cleaned and preprocessed

3. **Skill Extraction**

   * Extracts relevant technical skills using a predefined skill database

4. **Job Matching**

   * TF-IDF vectorization converts text into numerical form
   * Cosine similarity compares resume with job roles

5. **Recommendations**

   * Top matching job roles are displayed with scores

6. **Skill Gap Analysis 🔥**

   * Identifies missing skills required for each job role

---

## 📊 Example Output

**Extracted Skills:**

```
['python', 'machine learning', 'nlp', 'sql']
```

**Job Recommendations:**

```
1. Data Scientist → 51%
   Missing Skills: ['statistics']

2. Machine Learning Engineer → 32%
   Missing Skills: ['tensorflow', 'pytorch']
```

---

## 📁 Project Structure

```
intelligent-job-recommendation-system/
│
├── app.py
├── notebook.ipynb
├── .gitignore
└── README.md
```

---

## ⚠️ Note

Large datasets are not included in this repository. The project uses a predefined job-skill dataset for demonstration purposes.

---

## 🔥 Future Improvements

* LLM-based skill extraction (GPT / embeddings)
* Real-time job API integration
* Advanced resume parsing
* Deployment on Streamlit Cloud
* Authentication system for users

---

## 👩‍💻 Author

**Pavitra Bhat**
