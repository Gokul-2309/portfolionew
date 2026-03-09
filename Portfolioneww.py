import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="Gokul Portfolio", page_icon="💻", layout="wide")

# ----------- CUSTOM CSS -----------
st.markdown("""
<style>

/* MATRIX BACKGROUND */

.matrix-bg{
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
z-index:-1;
background:black;
}

/* Profile image */

.profile-container{
display:flex;
justify-content:center;
align-items:center;
margin-top:40px;
}

.profile-container img{
width:220px;
height:220px;
border-radius:50%;
object-fit:cover;
box-shadow:0px 10px 40px rgba(0,0,0,0.8);
}

/* Name */

.title{
font-size:48px;
font-weight:700;
text-align:center;
color:white;
}

/* Role */

.role{
font-size:26px;
text-align:center;
color:#00FF9C;
}

/* Skills */

.skills-container{
display:flex;
flex-wrap:wrap;
justify-content:center;
gap:12px;
}

.skill{
background:#111;
padding:10px 16px;
border-radius:20px;
border:1px solid #00FF9C;
color:white;
}

/* Cards */

.card{
background:#111;
padding:25px;
border-radius:15px;
box-shadow:0px 10px 30px rgba(0,0,0,0.6);
}

</style>

<canvas id="matrixCanvas" class="matrix-bg"></canvas>

<script>

const canvas = document.getElementById("matrixCanvas");
const ctx = canvas.getContext("2d");

canvas.height = window.innerHeight;
canvas.width = window.innerWidth;

const letters = "01PYTHONSQLFLASKDATA";
const matrix = letters.split("");

const fontSize = 14;
const columns = canvas.width / fontSize;

const drops = [];

for(let x = 0; x < columns; x++)
drops[x] = 1;

function draw(){

ctx.fillStyle = "rgba(0,0,0,0.05)";
ctx.fillRect(0,0,canvas.width,canvas.height);

ctx.fillStyle = "#00FF9C";
ctx.font = fontSize + "px monospace";

for(let i = 0; i < drops.length; i++){

const text = matrix[Math.floor(Math.random()*matrix.length)];

ctx.fillText(text, i*fontSize, drops[i]*fontSize);

if(drops[i]*fontSize > canvas.height && Math.random() > 0.975)
drops[i] = 0;

drops[i]++;

}

}

setInterval(draw,35);

</script>
""", unsafe_allow_html=True)

# -------- PROFILE SECTION --------

st.markdown('<div class="profile-container">', unsafe_allow_html=True)
st.image("pic.jpeg")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="title">Gokul M</div>', unsafe_allow_html=True)

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