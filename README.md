
# AI Powered Resume Analysis and Career Recommendation System

## 📌 Project Overview
The AI Powered Resume Analysis and Career Recommendation System is an intelligent web-based application developed to automate the resume screening process and provide personalized career guidance. The system uses Natural Language Processing (NLP) and semantic similarity techniques to analyze resumes, compare them with job descriptions, and recommend suitable job roles.

Unlike traditional keyword-based Applicant Tracking Systems (ATS), this system understands the contextual meaning of skills and experience using Sentence Embeddings and Cosine Similarity. It also provides skill gap analysis, learning resource suggestions, and mock interview support for candidates.

---

## 🚀 Features
- User Registration and Login Authentication
- Resume Upload (PDF/DOCX)
- Resume Text Extraction and Preprocessing
- NLP-Based Semantic Resume Analysis
- Job Recommendation with Match Percentage
- Cosine Similarity-Based Matching
- Skill Gap Analysis
- Learning Resource Suggestions
- Mock Interview Questions for High Match Scores
- Resume History Tracking
- Responsive Web Interface

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Framework
- Flask / Streamlit

### Libraries
- NLTK
- NumPy
- Pandas
- Scikit-learn
- Sentence Transformers
- PyPDF2
- python-docx

### Database
- SQLite

---

## ⚙️ Methodology
1. User uploads resume through the web interface  
2. Resume text is extracted from PDF/DOCX files  
3. NLP preprocessing is applied  
4. Sentence embeddings are generated  
5. Cosine similarity compares resume with job descriptions  
6. Top matching jobs are recommended  
7. If score ≥ 80% → Mock interview support  
8. If score < 80% → Skill gap analysis and learning resources  

---

## 📊 System Workflow

```text
Resume Upload
      ↓
Text Extraction
      ↓
Preprocessing
      ↓
Sentence Embedding
      ↓
Cosine Similarity
      ↓
Job Recommendation
      ↓
Skill Gap / Mock Interview
```

---

## 🎯 Advantages
- Reduces manual screening effort
- Improves recruitment efficiency
- Provides semantic understanding of resumes
- Reduces human bias in hiring
- Helps candidates improve missing skills
- Provides personalized career guidance

---

## 🔮 Future Scope
- GPT-based interview chatbot
- ATS integration
- Multilingual resume support
- Mobile application development
- Voice-based interview system
- Live job portal integration

---

## 📌 Conclusion
This project demonstrates how AI and NLP can improve traditional recruitment systems by providing intelligent resume analysis, accurate job recommendations, and personalized career support for candidates.
