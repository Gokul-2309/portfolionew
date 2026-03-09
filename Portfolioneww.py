import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="Gokul Portfolio", page_icon="💻", layout="wide")

# ----------- CUSTOM CSS -----------
st.markdown("""
<style>

/* Main background */
.stApp {
background-color:#F5F7FB;
}

/* Name */
.title{
font-size:45px;
font-weight:bold;
color:#1F2937;
}

/*image */
img {
border-radius:50%;
box-shadow:0px 6px 20px rgba(0,0,0,0.15);
}

/* Animated role text */
.role{
font-size:28px;
color:#2563EB;
font-weight:600;
}

/* Project cards */
.card{
background-color:#FFFFFF;
padding:25px;
border-radius:12px;
box-shadow:0px 4px 12px rgba(0,0,0,0.08);
border-left:5px solid #4F8BF9;
}

/* Skill tags */
.skill{
background-color:#E8F0FE;
color:#1F2937;
padding:8px 14px;
border-radius:20px;
margin:6px;
display:inline-block;
font-weight:500;
}

/* Buttons */
.stDownloadButton button{
background-color:#4F8BF9;
color:white;
border-radius:8px;
border:none;
padding:10px 18px;
font-weight:600;
}

.stLinkButton a{
background-color:#4F8BF9 !important;
color:white !important;
border-radius:8px !important;
padding:10px 18px !important;
text-decoration:none !important;
font-weight:600 !important;
}

</style>
""", unsafe_allow_html=True)

# -------- PROFILE SECTION --------

col1, col2 = st.columns([1,2])

with col1:
    image = Image.open("pic.jpeg")
    st.image(image,width=250,output_format="auto")

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