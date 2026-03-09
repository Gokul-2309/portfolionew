import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="Gokul Portfolio", page_icon="💻", layout="wide")

# ----------- CUSTOM CSS -----------
st.markdown("""
<style>

/* MAIN BACKGROUND */

.stApp{
background: radial-gradient(circle at top,#050505,#000000);
color:white;
text-align:center;
}

/* HERO CONTAINER */

.hero{
margin-top:80px;
}

/* PROFILE IMAGE */

.profile-img{
width:180px;
height:180px;
border-radius:50%;
object-fit:cover;
border:4px solid #00E5FF;
box-shadow:0 0 25px #00E5FF;
}

/* NAME GRADIENT */

.hero-title{
font-size:60px;
font-weight:700;
background:linear-gradient(90deg,#00E5FF,#6A5CFF);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
margin-top:25px;
}

/* ROLE TEXT */

.hero-role{
font-size:20px;
color:#cbd5e1;
margin-top:10px;
}

/* BUTTON */

.hero-btn{
display:inline-block;
margin-top:25px;
padding:12px 28px;
border-radius:25px;
background:linear-gradient(90deg,#00E5FF,#6A5CFF);
color:white;
text-decoration:none;
font-weight:500;
transition:0.3s;
}

.hero-btn:hover{
transform:translateY(-4px);
box-shadow:0 10px 30px rgba(0,229,255,0.4);
}

/* BACKGROUND CODE */

.code-bg{
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
z-index:-1;
opacity:0.05;
font-size:120px;
display:flex;
align-items:center;
justify-content:center;
color:white;
}

</style>
""", unsafe_allow_html=True)

#-----------Background Coding theme---------

st.markdown("""
<div class="code-bg">
&lt;python&gt; &lt;sql&gt; &lt;flask&gt; &lt;pandas&gt; &lt;data&gt;
</div>
""", unsafe_allow_html=True)

# -------- PROFILE SECTION --------

st.markdown("""
<div class="hero">

<img src="pic.jpeg" class="profile-img">

<h1 class="hero-title">Hi, I'm Gokul Mohan</h1>
""", unsafe_allow_html=True)

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

st.markdown("##  Skills")

skills = [
"Python","MySQL","Flask","SQL","Tableau",
"Excel","Data Analysis","Machine Learning","C","C++"
]

st.markdown('<div class="skills-container">', unsafe_allow_html=True)

for skill in skills:
    st.markdown(f'<div class="skill">{skill}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# -------- PROJECTS --------

st.markdown("##  Projects")

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

st.markdown("##  Current Learning")

st.write("""
Currently pursuing **Python Developer Course**

Technologies learning:

• Python Programming  
• MySQL Database  
• Flask Web Development  
""")

# -------- CONTACT --------

st.markdown("##  Contact")

st.write(" Email: gokulms2309@gmail.com")
st.write(" Location: Chennai, India")