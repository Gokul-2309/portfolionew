import streamlit as st
import base64

st.set_page_config(page_title="Gokul Portfolio", layout="wide")

# ----------- BACKGROUND + STYLE -----------

st.markdown("""
<style>

body{
background-color:#0f172a;
color:white;
}

.neon{
color:#00f7ff;
text-shadow:0 0 10px #00f7ff;
}

.role{
color:#38bdf8;
font-size:28px;
font-weight:bold;
}

.card{
background:#1e293b;
padding:25px;
border-radius:15px;
transition:0.4s;
box-shadow:0 0 10px #000;
}

.card:hover{
transform:translateY(-10px);
box-shadow:0 0 25px #00f7ff;
}

.skill{
background:#0ea5e9;
padding:8px 18px;
border-radius:20px;
margin:5px;
display:inline-block;
}

.button{
background:#06b6d4;
padding:12px 28px;
border-radius:8px;
color:white;
text-decoration:none;
font-weight:bold;
}

.button:hover{
background:#0891b2;
}

</style>
""", unsafe_allow_html=True)

# ----------- PARTICLES BACKGROUND -----------

particles = """
<div id="particles-js"></div>

<script src="https://cdn.jsdelivr.net/npm/particles.js"></script>

<script>
particlesJS("particles-js", {

"particles":{
"number":{"value":80},
"size":{"value":3},
"color":{"value":"#00f7ff"},
"line_linked":{"enable":true,"color":"#00f7ff"},
"move":{"speed":2}
}

});
</script>

<style>
#particles-js{
position:fixed;
width:100%;
height:100%;
z-index:-1;
top:0;
left:0;
}
</style>
"""

st.components.v1.html(particles,height=0)

# ----------- HEADER -----------

col1,col2 = st.columns([1,2])

with col1:
    st.image("pic.jpeg",width=230)

with col2:

    st.markdown("<h1 class='neon'>Gokul M</h1>",unsafe_allow_html=True)

    st.markdown("""
<h3 class='role'>
<span id="typing"></span>
</h3>

<script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12"></script>

<script>
var typed = new Typed("#typing",{
strings:[
"Aspiring Data Analyst",
"Python Developer",
"Software Developer"
],
typeSpeed:70,
backSpeed:40,
loop:true
})
</script>
""",unsafe_allow_html=True)

    st.write("""
Currently pursuing **Python Developer Course** covering  
**Python • MySQL • Flask**.

6 Months Internship as **Software Developer** at  
**Expert Medical Billing**.

Passionate about building **data-driven applications, dashboards,
and automation solutions.**
""")

# ----------- BUTTONS -----------

col1,col2,col3 = st.columns(3)

with col1:
    st.download_button(
        "⬇ Download Resume",
        open("Gokul_Resume.pdf","rb"),
        file_name="Gokul_Resume.pdf"
    )

with col2:
    st.link_button("GitHub",
                   "https://github.com/Gokul-2309")

with col3:
    st.link_button("LinkedIn",
                   "https://www.linkedin.com/in/gokul-m-892903216")

st.write("---")

# ----------- SKILLS -----------

st.header("Skills")

skills = [
"Python","MySQL","Flask","SQL",
"Data Analysis","Excel",
"Tableau","Machine Learning"
]

for s in skills:
    st.markdown(f"<span class='skill'>{s}</span>",
                unsafe_allow_html=True)

st.write("---")

# ----------- EXPERIENCE -----------

st.header("Experience")

st.markdown("""
### Software Developer Intern  
**Expert Medical Billing**  
Duration: 6 Months

Worked on developing a **Client Portal Project**.

Project Goal:

• Consolidate all operational information  
• Display insights through a **GUI dashboard**  
• Provide regularly updated data to users  
• Improve accessibility and decision making
""")

st.write("---")

# ----------- PROJECTS -----------

st.header("Projects")

col1,col2 = st.columns(2)

with col1:
    st.markdown("""
<div class="card">

<h3>Client Portal Dashboard</h3>

Built during internship.

Features:

• Centralized business data  
• GUI dashboard  
• Real time updates  
• Improved workflow efficiency

Tech Used:

Python • Flask • MySQL

</div>
""",unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="card">

<h3>Lung Cancer Prediction</h3>

Capstone Project from Data Science program.

Features:

• Machine Learning model  
• Predict patient severity level  
• Data preprocessing & analysis

Tech Used:

Python • Pandas • Scikit Learn

</div>
""",unsafe_allow_html=True)

st.write("---")

# ----------- CONTACT -----------

st.header("Contact")

st.write("📧 gokulms2309@gmail.com")
st.write("📍 Chennai, India")
st.write("📞 9566260923")

st.write("---")

st.markdown(
"<center>⚡ Built with Streamlit | Gokul Portfolio</center>",
unsafe_allow_html=True

)
