import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="Gokul Portfolio", page_icon="💻", layout="wide")

# ----------- CUSTOM CSS -----------
st.markdown("""
<style>

/* Background */

.stApp {
background: linear-gradient(135deg,#0F172A,#1E293B);
color:#F1F5F9;
}

/* Name */

.title{
font-size:48px;
font-weight:700;
text-align:center;
}

/* Role animation */

.role{
font-size:26px;
color:#38BDF8;
text-align:center;
font-weight:500;
}

/* Profile image */

img {
border-radius:50%;
box-shadow:0px 10px 30px rgba(0,0,0,0.6);
display:block;
margin-left:auto;
margin-right:auto;
}

/* Buttons */

.stDownloadButton button{
background:#38BDF8;
color:black;
border-radius:10px;
padding:10px 20px;
border:none;
font-weight:600;
transition:0.3s;
}

.stDownloadButton button:hover{
transform:translateY(-3px);
box-shadow:0px 8px 20px rgba(56,189,248,0.5);
}

/* Link Buttons */

.stLinkButton a{
background:#38BDF8 !important;
color:black !important;
border-radius:10px !important;
padding:10px 20px !important;
font-weight:600 !important;
transition:0.3s !important;
}

.stLinkButton a:hover{
transform:translateY(-4px);
box-shadow:0px 8px 20px rgba(56,189,248,0.6);
}

/* Skills */

.skill{
background:#1E293B;
padding:10px 16px;
border-radius:20px;
margin:6px;
display:inline-block;
border:1px solid #38BDF8;
transition:0.3s;
}

.skill:hover{
transform:translateY(-3px);
box-shadow:0px 6px 18px rgba(56,189,248,0.5);
}

/* Project cards */

.card{
background:#1E293B;
padding:25px;
border-radius:15px;
box-shadow:0px 6px 20px rgba(0,0,0,0.5);
transition:0.3s;
}

.card:hover{
transform:translateY(-6px);
box-shadow:0px 10px 30px rgba(56,189,248,0.4);
}

</style>
""", unsafe_allow_html=True)

# -------- PROFILE SECTION --------

st.image("pic.jpeg", width=220)

st.markdown('<div class="title">Gokul M</div>',unsafe_allow_html=True)

roles = [
        "Aspiring Data Analyst",
        "Python Developer",
        "Software Developer"
    ]

role_placeholder = st.empty()

for i in range(3):
        for role in roles:
            role_placeholder.markdown(f'<div class="role">{role}</div>',unsafe_allow_html=True)
            time.sleep(1)

st.write("""
Data-driven professional passionate about building analytical solutions and
software applications using **Python, SQL, MySQL, Flask and Data Analytics tools**.
""")

# -------- BUTTONS --------

col1,col2,col3 = st.columns(3)

with col1:
    with open("Gokul_Resume.pdf","rb") as file:
        st.download_button("📄 Download Resume",file,"Gokul_Resume.pdf")

with col2:
    st.link_button("💻 GitHub","https://github.com/Gokul-2309")

with col3:
    st.link_button("🔗 LinkedIn","https://www.linkedin.com/in/gokul-m-892903216")

# -------- SKILLS --------

st.markdown("## 🧠 Skills")

skills = [
"Python","MySQL","Flask","SQL","Tableau",
"Excel","Data Analysis","Machine Learning","C","C++"
]

for skill in skills:
    st.markdown(f'<span class="skill">{skill}</span>',unsafe_allow_html=True)

# -------- PROJECTS --------

st.markdown("## 🚀 Projects")

col1,col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="card">

    ### Client Portal Dashboard

    Developed during **Software Developer Internship**
    at Expert Medical Billing.

    **Goal**
    - Consolidate all operational data into one GUI dashboard

    **Features**
    - Centralized client information
    - Real-time updates
    - User friendly dashboard

    **Tech Stack**
    Python | MySQL | Flask

    </div>
    """,unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="card">

    ### Lung Cancer Severity Prediction

    Capstone project from **PGP Data Science & Business Analytics**

    **Work Done**
    - Data preprocessing
    - Exploratory Data Analysis
    - Machine Learning Model
    - Prediction system

    **Tools**
    Python | Pandas | Scikit-Learn | SQL

    </div>
    """,unsafe_allow_html=True)

# -------- CURRENT LEARNING --------

st.markdown("## 📚 Current Learning")

st.write("""
Currently pursuing **Python Developer Course**

Technologies learning:

• Python Programming  
• MySQL Database  
• Flask Web Development  
""")

# -------- CONTACT --------

st.markdown("## 📞 Contact")

st.write("📧 Email: gokulms2309@gmail.com")
st.write("📍 Location: Chennai, India")