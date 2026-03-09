import streamlit as st
from PIL import Image
import base64

st.set_page_config(page_title="Gokul Portfolio", page_icon="💻", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
.title {
    font-size:40px;
    font-weight:bold;
}

.subtitle {
    font-size:25px;
    color: #4CAF50;
}

.section {
    margin-top:40px;
}

.social-btn a{
text-decoration:none;
padding:10px 20px;
background:#4CAF50;
color:white;
border-radius:8px;
margin-right:10px;
}

</style>
""", unsafe_allow_html=True)


# ---------- PROFILE ----------
col1, col2 = st.columns([1,2])

with col1:
    image = Image.open("C:\Users\Admin\Desktop\portfolio\portfolionew\pic.jpeg")   # add your profile image
    st.image(image, width=220)

with col2:
    st.markdown('<div class="title">Gokul M</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="subtitle">
    Aspiring Data Analyst | Python Developer | Software Developer
    </div>
    """, unsafe_allow_html=True)

    st.write("""
Data-driven professional with strong analytical thinking and experience in  
Python, SQL, Tableau and Business Analytics. Passionate about building
data-driven solutions and developing applications.
""")


# ---------- RESUME DOWNLOAD ----------
def get_resume():
    with open("Gokul_Resume.pdf", "rb") as file:
        btn = st.download_button(
            label="📄 Download Resume",
            data=file,
            file_name="Gokul_Resume.pdf",
            mime="application/pdf"
        )
    return btn

get_resume()


# ---------- SOCIAL LINKS ----------
st.markdown("""
<div class="social-btn">

<a href="https://github.com/yourgithub" target="_blank">GitHub</a>

<a href="https://linkedin.com/in/yourlinkedin" target="_blank">LinkedIn</a>

</div>
""", unsafe_allow_html=True)


# ---------- SKILLS ----------
st.markdown("## 🧠 Skills")

skills = [
"Python",
"MySQL",
"Flask",
"SQL",
"Tableau",
"Excel",
"Data Analysis",
"C / C++"
]

st.write(", ".join(skills))


# ---------- PROJECTS ----------
st.markdown("## 🚀 Projects")

# Project 1
st.subheader("Client Portal Dashboard")

st.write("""
Developed a **Client Portal Web Application** during my internship at 
Expert Medical Billing as a **Software Developer Intern**.

Goal of the project:
To consolidate all operational and client related information into a 
single **GUI dashboard** that is regularly updated.

Key Features:
- Centralized client data management
- Real-time dashboard updates
- User-friendly interface
- Improved data accessibility for internal teams

Technologies Used:
Python, MySQL, Flask
""")


# Project 2
st.subheader("Lung Cancer Severity Prediction (Capstone Project)")

st.write("""
Developed a **Machine Learning model** to predict the severity level 
of lung cancer based on patient clinical and behavioral data.

This project was completed as part of the **PGP in Data Science and Business Analytics**.

Key Highlights:
- Data preprocessing and feature engineering
- Exploratory Data Analysis (EDA)
- Machine learning model building
- Model evaluation and prediction

Tools & Technologies:
Python, Pandas, Scikit-learn, SQL
""")


# ---------- COURSE ----------
st.markdown("## 📚 Current Learning")

st.write("""
Currently pursuing **Python Developer Course** covering:

- Python Programming
- MySQL Database
- Flask Web Development
""")


# ---------- CONTACT ----------
st.markdown("## 📞 Contact")

st.write("📧 gokulms2309@gmail.com")

st.write("📍 Chennai, India")
