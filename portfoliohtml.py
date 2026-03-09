import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Gokul Portfolio", layout="wide")

html_code = """
<!DOCTYPE html>
<html>

<head>

<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

<script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12"></script>

<script src="https://cdn.jsdelivr.net/npm/particles.js"></script>

<style>

body{
margin:0;
font-family: 'Poppins', sans-serif;
background:#0f172a;
color:white;
overflow:hidden;
}

#particles-js{
position:fixed;
width:100%;
height:100%;
z-index:-1;
}

.container{
text-align:center;
padding-top:120px;
}

h1{
font-size:60px;
}

h1 span{
color:#00e5ff;
}

#typing{
color:#a855f7;
font-size:30px;
font-weight:600;
}

.profile{
width:180px;
border-radius:50%;
border:4px solid #00e5ff;
box-shadow:0 0 30px #00e5ff;
margin-bottom:20px;
}

.btn{
padding:12px 25px;
background:#00e5ff;
border-radius:30px;
text-decoration:none;
color:black;
font-weight:bold;
transition:0.3s;
}

.btn:hover{
transform:scale(1.1);
}

.skills{
margin-top:60px;
}

.skill{
display:inline-block;
background:#1e293b;
padding:12px 20px;
margin:10px;
border-radius:20px;
transition:0.3s;
}

.skill:hover{
background:#00e5ff;
color:black;
transform:translateY(-8px);
}

.projects{
margin-top:70px;
}

.card{
display:inline-block;
width:250px;
background:#1e293b;
margin:20px;
padding:25px;
border-radius:15px;
transition:0.4s;
}

.card:hover{
transform:scale(1.08);
box-shadow:0 0 25px #00e5ff;
}

.footer{
margin-top:80px;
}

</style>

</head>

<body>

<div id="particles-js"></div>

<div class="container">

<img src="https://i.imgur.com/2DhmtJ4.png" class="profile">

<h1>Hi I'm <span>Gokul</span></h1>

<div id="typing"></div>

<br>

<a class="btn">Download Resume</a>

<div class="skills">

<h2>Skills</h2>

<div class="skill">Python</div>
<div class="skill">Data Analysis</div>
<div class="skill">MySQL</div>
<div class="skill">Power BI</div>
<div class="skill">Flask</div>
<div class="skill">Machine Learning</div>

</div>

<div class="projects">

<h2>Projects</h2>

<div class="card">
<h3>Client Portal</h3>
<p>Dashboard consolidating business data into one platform.</p>
</div>

<div class="card">
<h3>Cancer Severity</h3>
<p>ML model predicting cancer severity from habits.</p>
</div>

<div class="card">
<h3>Data Analysis</h3>
<p>Analyzing datasets using Python libraries.</p>
</div>

</div>

<div class="footer">

<p>📧 gokulms2309@gmail.com</p>
<p>💻 github.com/Gokul-2309</p>

</div>

</div>

<script>

var typed = new Typed("#typing",{
strings:[
"Data Analyst",
"Python Developer",
"Software Developer"
],
typeSpeed:70,
backSpeed:40,
loop:true
});

particlesJS("particles-js",{

particles:{
number:{value:80},
size:{value:3},
color:{value:"#00e5ff"},
line_linked:{
enable:true,
color:"#00e5ff"
}
}

});

</script>

</body>
</html>
"""

components.html(html_code, height=900, scrolling=True)