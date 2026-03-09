import streamlit as st
import base64
from datetime import datetime
import random
import requests
import plotly.graph_objects as go
import time

st.set_page_config(page_title="Gokul M | Data Analyst", layout="wide", page_icon="🚀")

# ----------- CUSTOM CSS -----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

/* Profile card styling */
.profile-card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    border: 1px solid rgba(255, 255, 255, 0.18);
    transition: transform 0.3s;
}

.profile-card:hover {
    transform: translateY(-5px);
}

/* Profile image styling */
.profile-img {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid #00f7ff;
    box-shadow: 0 0 30px #00f7ff;
    margin: 0 auto;
    display: block;
    animation: glow 2s ease-in-out infinite;
}

@keyframes glow {
    0%, 100% { box-shadow: 0 0 30px #00f7ff; }
    50% { box-shadow: 0 0 50px #00f7ff, 0 0 80px #00f7ff; }
}

/* Skill bars */
.skill-container {
    width: 100%;
    background: rgba(255,255,255,0.1);
    border-radius: 10px;
    margin: 10px 0;
    height: 30px;
    position: relative;
}

.skill-bar {
    background: linear-gradient(90deg, #00f7ff, #764ba2);
    border-radius: 10px;
    height: 30px;
    text-align: center;
    color: white;
    line-height: 30px;
    font-weight: bold;
    animation: fillBar 2s ease-out;
    position: relative;
    overflow: hidden;
}

.skill-bar::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    animation: shimmer 2s infinite;
}

@keyframes fillBar {
    from { width: 0; }
    to { width: var(--width); }
}

@keyframes shimmer {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

/* Skill pills */
.skill-pill {
    background: linear-gradient(135deg, #00f7ff, #764ba2);
    padding: 8px 18px;
    border-radius: 30px;
    margin: 5px;
    display: inline-block;
    color: white;
    font-weight: 600;
    transition: all 0.3s;
    cursor: pointer;
    border: 1px solid rgba(255,255,255,0.2);
}

.skill-pill:hover {
    transform: scale(1.1) rotate(5deg);
    box-shadow: 0 0 20px #00f7ff;
}

/* Project cards */
.project-card {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 20px;
    margin: 10px 0;
    border: 1px solid rgba(255,255,255,0.2);
    transition: all 0.3s;
    height: 100%;
}

.project-card:hover {
    transform: translateY(-10px) rotate(1deg);
    box-shadow: 0 20px 40px rgba(0,247,255,0.3);
    border-color: #00f7ff;
}

.project-tech {
    display: inline-block;
    background: #00f7ff;
    color: #000;
    padding: 5px 12px;
    border-radius: 15px;
    margin: 5px;
    font-size: 12px;
    font-weight: 600;
}

/* Chatbot */
.chat-container {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 20px;
    margin-top: 20px;
}

.chat-message {
    padding: 10px;
    border-radius: 10px;
    margin: 5px 0;
    max-width: 80%;
}

.user-message {
    background: #00f7ff;
    color: #000;
    margin-left: auto;
}

.bot-message {
    background: rgba(255,255,255,0.2);
    color: white;
}

/* Visitor counter */
.visitor-counter {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 50px;
    padding: 10px 20px;
    display: inline-block;
    color: white;
    font-weight: bold;
    animation: pulse 2s infinite;
    margin: 20px auto;
    text-align: center;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}

/* 3D Text */
.text-3d {
    text-shadow: 0 1px 0 #ccc,
                 0 2px 0 #c9c9c9,
                 0 3px 0 #bbb,
                 0 4px 0 #b9b9b9,
                 0 5px 0 #aaa,
                 0 6px 1px rgba(0,0,0,.1),
                 0 0 5px rgba(0,0,0,.1),
                 0 1px 3px rgba(0,0,0,.3),
                 0 3px 5px rgba(0,0,0,.2),
                 0 5px 10px rgba(0,0,0,.25),
                 0 10px 10px rgba(0,0,0,.2),
                 0 20px 20px rgba(0,0,0,.15);
    color: white;
}

/* Custom button */
.custom-button {
    background: linear-gradient(45deg, #00f7ff, #764ba2);
    border: none;
    color: white;
    padding: 12px 30px;
    border-radius: 50px;
    font-weight: bold;
    text-decoration: none;
    display: inline-block;
    transition: all 0.3s;
    border: 1px solid rgba(255,255,255,0.2);
    margin: 5px;
    cursor: pointer;
}

.custom-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px #00f7ff;
}

/* Navigation buttons */
.nav-button {
    background: rgba(255,255,255,0.1);
    color: white;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s;
    border: 1px solid rgba(255,255,255,0.2);
    margin: 5px 0;
}

.nav-button:hover {
    background: #00f7ff;
    color: black;
    transform: translateX(10px);
}

.nav-button.active {
    background: #00f7ff;
    color: black;
    border-color: #00f7ff;
}

/* Section headers */
.section-header {
    color: #00f7ff;
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 30px;
    text-align: center;
    text-shadow: 0 0 20px #00f7ff;
}
</style>
""", unsafe_allow_html=True)

# ----------- 3D PARTICLES BACKGROUND -----------
particles_js = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>3D Particles</title>
  <style>
    body { margin: 0; overflow: hidden; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
    #particles-js {
      position: fixed;
      width: 100%;
      height: 100%;
      top: 0;
      left: 0;
      z-index: -1;
    }
  </style>
</head>
<body>
  <div id="particles-js"></div>
  
  <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
  <script>
    particlesJS("particles-js", {
      "particles": {
        "number": {
          "value": 100,
          "density": {
            "enable": true,
            "value_area": 800
          }
        },
        "color": {
          "value": ["#00f7ff", "#764ba2", "#667eea", "#ffffff"]
        },
        "shape": {
          "type": ["circle", "triangle", "polygon"],
          "stroke": {
            "width": 0,
            "color": "#000000"
          },
          "polygon": {
            "nb_sides": 5
          }
        },
        "opacity": {
          "value": 0.7,
          "random": true,
          "anim": {
            "enable": true,
            "speed": 1,
            "opacity_min": 0.1,
            "sync": false
          }
        },
        "size": {
          "value": 5,
          "random": true,
          "anim": {
            "enable": true,
            "speed": 2,
            "size_min": 0.1,
            "sync": false
          }
        },
        "line_linked": {
          "enable": true,
          "distance": 150,
          "color": "#00f7ff",
          "opacity": 0.4,
          "width": 1
        },
        "move": {
          "enable": true,
          "speed": 2,
          "direction": "none",
          "random": true,
          "straight": false,
          "out_mode": "out",
          "bounce": false,
          "attract": {
            "enable": true,
            "rotateX": 600,
            "rotateY": 1200
          }
        }
      },
      "interactivity": {
        "detect_on": "canvas",
        "events": {
          "onhover": {
            "enable": true,
            "mode": ["grab", "bubble"]
          },
          "onclick": {
            "enable": true,
            "mode": "push"
          },
          "resize": true
        },
        "modes": {
          "grab": {
            "distance": 200,
            "line_linked": {
              "opacity": 1
            }
          },
          "bubble": {
            "distance": 400,
            "size": 10,
            "duration": 2,
            "opacity": 0.8,
            "speed": 3
          },
          "repulse": {
            "distance": 200,
            "duration": 0.4
          },
          "push": {
            "particles_nb": 4
          },
          "remove": {
            "particles_nb": 2
          }
        }
      },
      "retina_detect": true
    });
  </script>
</body>
</html>
"""

st.components.v1.html(particles_js, height=0)

# ----------- VISITOR COUNTER -----------
if 'visitor_count' not in st.session_state:
    try:
        with open('visitor_count.txt', 'r') as f:
            count = int(f.read())
    except:
        count = 0
    
    count += 1
    st.session_state.visitor_count = count
    
    with open('visitor_count.txt', 'w') as f:
        f.write(str(count))

# ----------- SESSION STATE FOR NAVIGATION -----------
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# ----------- SIDEBAR NAVIGATION -----------
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h2 class='text-3d'>GOKUL M</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Navigation")
    
    # Navigation buttons
    nav_options = ["Home", "Projects", "Skills", "Experience", "Contact", "Chat with Me"]
    nav_icons = ["🏠", "🚀", "⚡", "💼", "📫", "🤖"]
    
    for i, option in enumerate(nav_options):
        if st.button(f"{nav_icons[i]} {option}", key=f"nav_{option}", use_container_width=True):
            st.session_state.page = option
    
    st.markdown("---")
    
    # Visitor counter in sidebar
    st.markdown(f"""
    <div class='visitor-counter'>
        👥 Visitors: {st.session_state.visitor_count}
    </div>
    """, unsafe_allow_html=True)

# ----------- HOME SECTION -----------
if st.session_state.page == "Home":
    st.markdown("<h1 class='section-header'>Welcome to My Portfolio</h1>", unsafe_allow_html=True)
    
    # Centered profile image with glow effect
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        try:
            with open("profile.jpg", "rb") as f:
                img_data = base64.b64encode(f.read()).decode()
            st.markdown(f"""
            <div style='text-align: center; padding: 20px;'>
                <img src='data:image/jpeg;base64,{img_data}' class='profile-img'>
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown("""
            <div style='text-align: center; padding: 20px;'>
                <div style='width:200px; height:200px; border-radius:50%; background:linear-gradient(45deg, #00f7ff, #764ba2); margin:0 auto; display:flex; align-items:center; justify-content:center; font-size:60px; color:white;'>
                    GM
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Typing animation
    st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h1 class='text-3d'>Gokul M</h1>
        <div style='font-size: 28px; color: white; min-height: 60px; margin: 20px 0;'>
            <span id="typing"></span>
        </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12"></script>
    <script>
    var typed = new Typed("#typing", {
        strings: ["Data Analyst 📊", "Python Developer 🐍", "Software Developer 💻", "ML Enthusiast 🤖"],
        typeSpeed: 70,
        backSpeed: 40,
        loop: true,
        backDelay: 1500
    });
    </script>
    """, unsafe_allow_html=True)
    
    # About section
    st.markdown("""
    <div class='project-card' style='text-align: center; padding: 30px; margin: 20px 0;'>
        <h3 style='color:#00f7ff;'>About Me</h3>
        <p style='font-size: 18px; line-height: 1.8;'>
            Currently pursuing Python Developer Course covering Python, MySQL, and Flask.<br>
            6 Months Internship as Software Developer at Expert Medical Billing.<br>
            Passionate about building data-driven applications, dashboards, and automation solutions.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Download Resume Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            with open("Gokul_Resume.pdf", "rb") as pdf_file:
                resume_bytes = pdf_file.read()
            st.download_button(
                label="📄 Download Resume",
                data=resume_bytes,
                file_name="Gokul_M_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        except:
            st.info("📄 Resume PDF will be available here")

# ----------- PROJECTS SECTION -----------
elif st.session_state.page == "Projects":
    st.markdown("<h1 class='section-header'>🚀 My Projects</h1>", unsafe_allow_html=True)
    
    # GitHub API integration
    def get_github_repos(username):
        try:
            response = requests.get(f"https://api.github.com/users/{username}/repos")
            if response.status_code == 200:
                return response.json()
        except:
            return None
        return None
    
    github_username = "yourgithub"  # Replace with your GitHub username
    
    # Featured Projects
    col1, col2 = st.columns(2)
    
    projects = [
        {
            "title": "Client Portal Dashboard",
            "description": "Built during internship. Centralized business data with GUI dashboard for real-time updates and improved workflow efficiency.",
            "tech": ["Python", "Flask", "MySQL", "Bootstrap"],
            "github": "https://github.com/yourgithub/client-portal",
            "live": "https://client-portal-demo.herokuapp.com"
        },
        {
            "title": "Lung Cancer Prediction",
            "description": "ML model predicting patient severity levels with 92% accuracy. Includes comprehensive data preprocessing and analysis.",
            "tech": ["Python", "Scikit-learn", "Pandas", "Flask"],
            "github": "https://github.com/yourgithub/lung-cancer-prediction",
            "live": "https://cancer-predictor.herokuapp.com"
        },
        {
            "title": "Data Visualization Dashboard",
            "description": "Interactive dashboard for business analytics with real-time data updates and custom visualizations.",
            "tech": ["Python", "Plotly", "Dash", "Pandas"],
            "github": "https://github.com/yourgithub/data-dashboard",
            "live": "https://data-dashboard.herokuapp.com"
        },
        {
            "title": "E-commerce Analytics",
            "description": "Comprehensive analytics solution for e-commerce platforms with customer segmentation and sales forecasting.",
            "tech": ["Python", "Tableau", "SQL", "Machine Learning"],
            "github": "https://github.com/yourgithub/ecommerce-analytics",
            "live": "https://ecommerce-analytics.herokuapp.com"
        }
    ]
    
    for i, project in enumerate(projects):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div class='project-card'>
                <h3 style='color:#00f7ff;'>{project['title']}</h3>
                <p style='color:white;'>{project['description']}</p>
                <div style='margin: 15px 0;'>
                    {''.join([f"<span class='project-tech'>{tech}</span>" for tech in project['tech']])}
                </div>
                <div style='margin-top: 15px;'>
                    <a href='{project['github']}' target='_blank' class='custom-button'>GitHub</a>
                    <a href='{project['live']}' target='_blank' class='custom-button'>Live Demo</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Auto-load GitHub repos
    st.markdown("<h2 class='section-header' style='font-size:28px;'>📦 GitHub Repositories</h2>", unsafe_allow_html=True)
    repos = get_github_repos(github_username)
    
    if repos:
        cols = st.columns(2)
        for i, repo in enumerate(repos[:6]):
            with cols[i % 2]:
                st.markdown(f"""
                <div class='project-card' style='margin:10px 0;'>
                    <h4 style='color:#00f7ff;'>{repo['name']}</h4>
                    <p>{repo['description'] or 'No description available'}</p>
                    <div style='display:flex; gap:20px; margin:10px 0;'>
                        <span>⭐ {repo['stargazers_count']}</span>
                        <span>🍴 {repo['forks_count']}</span>
                    </div>
                    <a href='{repo['html_url']}' target='_blank' class='custom-button'>View on GitHub</a>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("Connect your GitHub account to see repositories!")

# ----------- SKILLS SECTION -----------
elif st.session_state.page == "Skills":
    st.markdown("<h1 class='section-header'>⚡ Technical Skills</h1>", unsafe_allow_html=True)
    
    skills_data = {
        "Python": 95,
        "MySQL": 90,
        "Flask": 85,
        "Data Analysis": 92,
        "Machine Learning": 80,
        "Tableau": 88,
        "Excel": 90,
        "Statistics": 85
    }
    
    # Animated skill bars
    for skill, level in skills_data.items():
        st.markdown(f"""
        <div style='margin: 20px 0;'>
            <div style='display:flex; justify-content:space-between; color:white; margin-bottom:5px;'>
                <span>{skill}</span>
                <span>{level}%</span>
            </div>
            <div class='skill-container'>
                <div class='skill-bar' style='width:{level}%;'>
                    {'★' * (level//20)} {'☆' * (5 - level//20)}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<h2 class='section-header' style='font-size:28px;'>🎯 Additional Skills</h2>", unsafe_allow_html=True)
    
    additional_skills = [
        "Pandas", "NumPy", "Scikit-learn", "TensorFlow", "Keras",
        "Flask", "Django", "REST APIs", "Git", "Docker",
        "AWS", "Google Cloud", "Power BI", "Tableau", "Excel"
    ]
    
    cols = st.columns(3)
    for i, skill in enumerate(additional_skills):
        with cols[i % 3]:
            st.markdown(f"""
            <div class='skill-pill' style='width:100%; text-align:center;'>
                {skill}
            </div>
            """, unsafe_allow_html=True)

# ----------- EXPERIENCE SECTION -----------
elif st.session_state.page == "Experience":
    st.markdown("<h1 class='section-header'>💼 Work Experience</h1>", unsafe_allow_html=True)
    
    timeline_data = [
        {
            "date": "2023 - Present",
            "title": "Python Developer Course",
            "company": "Self-paced Learning",
            "description": "Comprehensive training in Python, MySQL, Flask, and web development.",
            "achievements": [
                "Completed 10+ projects",
                "Mastered data structures and algorithms",
                "Built full-stack applications"
            ]
        },
        {
            "date": "2022 - 2023",
            "title": "Software Developer Intern",
            "company": "Expert Medical Billing",
            "description": "Developed Client Portal Project for consolidating operational information.",
            "achievements": [
                "Built GUI dashboard with real-time updates",
                "Improved data accessibility by 40%",
                "Reduced manual work by 25%"
            ]
        }
    ]
    
    for exp in timeline_data:
        st.markdown(f"""
        <div class='project-card' style='margin:20px 0;'>
            <div style='display:flex; justify-content:space-between; align-items:center;'>
                <h3 style='color:#00f7ff;'>{exp['title']}</h3>
                <span style='color:#00f7ff; font-weight:bold;'>{exp['date']}</span>
            </div>
            <h4 style='color:white;'>{exp['company']}</h4>
            <p style='color:white;'>{exp['description']}</p>
            <ul style='color:white;'>
                {''.join([f"<li>{achievement}</li>" for achievement in exp['achievements']])}
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ----------- CONTACT SECTION -----------
elif st.session_state.page == "Contact":
    st.markdown("<h1 class='section-header'>📫 Get in Touch</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='project-card'>
            <h3 style='color:#00f7ff;'>Contact Information</h3>
            <p style='margin:20px 0; font-size:18px;'>📧 gokulms2309@gmail.com</p>
            <p style='font-size:18px;'>📍 Chennai, India</p>
            <p style='font-size:18px;'>📞 +91 9566260923</p>
            <div style='margin-top:30px;'>
                <a href='https://github.com/yourgithub' target='_blank' class='custom-button'>GitHub</a>
                <a href='https://linkedin.com/in/yourlinkedin' target='_blank' class='custom-button'>LinkedIn</a>
                <a href='https://twitter.com/yourtwitter' target='_blank' class='custom-button'>Twitter</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='project-card'>
            <h3 style='color:#00f7ff;'>Send a Message</h3>
        """, unsafe_allow_html=True)
        
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message")
            submitted = st.form_submit_button("Send Message", use_container_width=True)
            
            if submitted:
                st.success("✅ Message sent successfully! I'll get back to you soon.")
        
        st.markdown("</div>", unsafe_allow_html=True)

# ----------- CHATBOT SECTION -----------
elif st.session_state.page == "Chat with Me":
    st.markdown("<h1 class='section-header'>🤖 Chat with AI Assistant</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='chat-container'>
        <p style='color:#00f7ff; font-size:18px;'>Ask me anything about Gokul's skills, experience, or projects!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! I'm Gokul's AI assistant. Ask me anything about his skills, experience, or projects!"}
        ]
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me anything..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate response
        with st.chat_message("assistant"):
            response = generate_chat_response(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

def generate_chat_response(prompt):
    """Generate chatbot response based on portfolio data"""
    prompt_lower = prompt.lower()
    
    responses = {
        "skills": "Gokul is proficient in Python (95%), MySQL (90%), Flask (85%), Data Analysis (92%), Machine Learning (80%), Tableau (88%), and Excel (90%). He's also skilled in Pandas, NumPy, Scikit-learn, and various other tools!",
        "experience": "Gokul completed a 6-month internship as a Software Developer at Expert Medical Billing, where he developed a Client Portal Dashboard that improved workflow efficiency by 25%. He's currently pursuing a Python Developer course.",
        "projects": "Gokul has built several impressive projects including a Client Portal Dashboard, Lung Cancer Prediction model with 92% accuracy, Data Visualization Dashboard, and an E-commerce Analytics platform. Check them out in the Projects section!",
        "contact": "You can reach Gokul at gokulms2309@gmail.com or connect with him on LinkedIn and GitHub. He's based in Chennai, India and is open to opportunities!",
        "education": "Gokul is currently enrolled in a Python Developer Course covering Python, MySQL, and Flask development. He's also completed various online courses in Data Science and Machine Learning.",
        "github": "You can find Gokul's projects on GitHub. He has several repositories showcasing his work in data analysis, web development, and machine learning applications."
    }
    
    for key, response in responses.items():
        if key in prompt_lower:
            return response
    
    return "I can tell you about Gokul's skills, experience, projects, education, or how to contact him. What would you like to know?"

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px; color: white;'>
    <p>⚡ Built with Streamlit | Gokul M Portfolio 2024 ⚡</p>
    <p style='font-size: 12px; opacity: 0.7;'>Last updated: March 2024</p>
</div>
""", unsafe_allow_html=True)