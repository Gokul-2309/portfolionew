import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="Gokul Portfolio", page_icon="💻", layout="wide")

# ----------- CUSTOM CSS -----------
st.markdown("""
<style>

.main {
background-color:#0E1117;
}

.title{
font-size:45px;
font-weight:bold;
}

.role{
font-size:28px;
color:#00F5A0;
}

.card{
background-color:#1E1E1E;
padding:20px;
border-radius:12px;
box-shadow:0px 0px 10px rgba(0,0,0,0.5);
}

.skill{
background-color:#2E2E2E;
padding:8px;
border-radius:10px;
margin:5px;
display:inline-block;
}

.button{
background:#00F5A0;
color:black;
padding:10px 20px;
border-radius:8px;
text-decoration:none;
font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# -------- PROFILE SECTION --------

col1, col2 = st.columns([1,2])

with col1:
    image = Image.open("pic.jpeg")
    st.image(image,width=250)

with col2:

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