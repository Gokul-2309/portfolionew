import streamlit as st

st.set_page_config(page_title="Gokul Portfolio", layout="wide")

# Navbar
st.markdown("""
<style>
body{
background:#0f0f0f;
color:white;
}

.hero{
text-align:center;
padding-top:60px;
}

.profile-pic{
width:200px;
height:200px;
border-radius:100%;
object-fit:cover;
border:4px solid #00d9ff;
box-shadow:0 0 25px rgba(0,217,255,0.6);
}

.name{
font-size:60px;
background:linear-gradient(90deg,#00d9ff,#8a2be2);
-webkit-background-clip:text;
color:transparent;
}

.skill{
display:inline-block;
padding:10px 20px;
margin:10px;
background:#1a1a1a;
border-radius:20px;
}

.card{
background:#1a1a1a;
padding:25px;
border-radius:15px;
margin:10px;
}

</style>
""", unsafe_allow_html=True)


# HERO SECTION
st.markdown('<div class="hero">', unsafe_allow_html=True)

st.image("pic.jpeg", width=200)

st.markdown('<h1 class="name">Hi, I\'m Gokul Mohan</h1>', unsafe_allow_html=True)
st.write("Python Developer | Web Developer")

st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ABOUT
st.header("About Me")

st.write(
"I am a passionate developer who loves building modern web applications using Python and web technologies."
)

st.divider()

# SKILLS
st.header("Skills")

skills = [
"Python","MySQL","KNIME","Tabulae","Flask",
"MS Excel","Power BI","Problem Solving"
]

for skill in skills:
    st.markdown(f'<span class="skill">{skill}</span>', unsafe_allow_html=True)

st.divider()

# PROJECTS
st.header("Projects")

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
<div class="card">
<h3>Client Portal Project</h3>
<p>Consolidate all the information in a GUI dashboard that is regularly updated.</p>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="card">
<h3>Cancer Severity</h3>
<p>Predict the severity of cancer based on habitual behaviour.</p>
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="card">
<h3>Data Analysis</h3>
<p>Analyzing data using Python libraries.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# CONTACT
st.header("Contact")

st.write("📧 Email: gokulms2309@gmail.com")
st.write("💻 GitHub: https://github.com/Gokul-2309")
st.write("🔗 LinkedIn: https://www.linkedin.com/in/gokul-m-892903216")

st.divider()

st.caption("© 2026 Gokul Mohan")