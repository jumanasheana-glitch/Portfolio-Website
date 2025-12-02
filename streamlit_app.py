# streamlit_app.py
# Professional interactive portfolio for CIS 211
import streamlit as st
import pandas as pd
from datetime import datetime

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(page_title="Asheana Juman — Portfolio",
                   page_icon="🎨",
                   layout="wide")

# -----------------------------
# Data structures (dictionary, lists)
# -----------------------------
personal_info = {
    "name": "Asheana Juman",
    "title": "Business Information Systems Student",
     "email": "jumanasheana@gmail.com",
|     "location": "Queens, NY",
|     "graduation": "June 2026"
 }

technical_skills = ["Python", "Data Analysis", "Streamlit", "HTML/CSS", "Photography"]
soft_skills = ["Communication", "Teamwork", "Time Management", "Leadership"]

projects = [
    {"title": "Makeup Recreation Project", "description": "Bring Pinterest makeup looks to life; photography documentation.", "technologies": ["Makeup", "Photography"], "status": "Completed"},
    {"title": "Office of Communication Internship", "description": "Developed photography and communication materials for campus events.", "technologies": ["Photography", "Social Media"], "status": "Completed"},
    {"title": "Streamlit Portfolio", "description": "This portfolio built using Streamlit for CIS 211.", "technologies": ["Python", "Streamlit"], "status": "In Progress"}
]

# -----------------------------
# Helper functions (3+ custom functions)
# -----------------------------
def calculate_gpa(grades):
   """Calculate GPA from a list of letter grades."""
   grade_points = {'A':4.0,'A-':3.7,'B+':3.3,'B':3.0,'B-':2.7,'C+':2.3,'C':2.0,'C-':1.7,'D':1.0,'F':0.0}
   if not grades:
      return 0.0
   points = [grade_points.get(g.strip().upper(), 0) for g in grades]
   return sum(points) / len(points)

def display_project(project: dict):
    """Display a single project in an expander with metadata and progress."""
    with st.expander(project["title"]):
         st.write(f"**Description:** {project['description']}")
         st.write(f"**Skills / Tools:** {', '.join(project['technologies'])}")
         st.write(f"**Status:** {project['status']}")
         if project["status"] == "In Progress":
             st.progress(0.6)
             st.write("Progress: 60%")
         elif project["status"] == "Completed":
             st.success("Project Completed ✅")

def send_contact_message(name, email, subject, message):
    """Simulate sending a contact message (would integrate with email in production)."""
    # This is a placeholder for an actual email or database integration.
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"name": name, "email": email, "subject": subject, "message": message, "time": timestamp}

# -----------------------------
# Sidebar navigation
# -----------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Skills", "Projects", "Contact"])

# -----------------------------
# Home page
# -----------------------------
if page == "Home":
    st.markdown("<h1 style='color:#1E3A8A'>Welcome to My Portfolio</h1>", unsafe_allow_html=True)
    st.subheader(f"Hi — I'm {personal_info['name']}, {personal_info['title']}")
    col1, col2 = st.columns([2,1])
    with col1:
         st.write("""I am a makeup creator and photography enthusiast studying Business Information Systems. 
                  I combine creativity and business skills to build a career as an entrepreneur and investor in small businesses.""")
         st.write("**What I do:**")
         st.write("- Create artistic makeup looks and document them with photography")
         st.write("- Build web apps using Python and Streamlit")
         st.write("- Learn business and technical skills to launch and support small businesses")
    with col2:
         st.write("## Quick Facts")
         st.write(f"**Location:** {personal_info['location']}")
         st.write(f"**Expected Graduation:** {personal_info['graduation']}")
         st.write(f"**Contact:** {personal_info['email']}")
     st.write("---")

# -----------------------------
# About Page
# -----------------------------
elif page == "About":
     st.header("About Me")
     tabs = st.tabs(["Education", "Interests", "Goals"])
     with tabs[0]:
          st.write("**Medgar Evers College, CUNY**")
          st.write("Bachelor of Science — Business Information Systems")
          st.write("Relevant coursework:")
          coursework = ["Internet & Emerging Technologies", "Database Management", "Business Analysis", "Programming Fundamentals"] 
          for c in coursework:
              st.write(f"- {c}")
 with tabs[1]:
         st.write("**Interests:** Makeup artistry, photography, web development, entrepreneurship, small business support.")
         st.write("**Hobbies:** Reading, building small projects, trying new creative styles.")
 with tabs[2]:
       st.write("**Career Goals:** Become a business owner and investor, support small businesses, and integrate creative work with technology.")

# -----------------------------
# Skills Page
# -----------------------------
elif page == "Skills":
    st.title("Skills & Experience")

    col1, col2 = st.columns(2)

    # -------- LEFT COLUMN: Technical Skills --------
    with col1:
        st.subheader("Technical Skills")
        technical_skills = [
            "Python",
            "HTML & CSS",
            "running a social media account",
            "Microsoft Excel",
            "Photography",
            "Digital Content Editing"
        ]
 # -------- RIGHT COLUMN: Soft Skills --------
    with col2:
        st.subheader("Soft Skills")
        soft_skills = [
            "Communication",
            "Creativity",
            "Leadership",
            "Time Management",
            "Team Collaboration",
            "Adaptability",
            "Problem-Solving"
        ]
        for skill in soft_skills:
            st.write(f"- {skill}")

        st.subheader("Skills Distribution Chart")
        chart_data = {
            "Skill Category": ["Technical", "Creativity", "Communication", "Leadership"],
            "Proficiency": [70, 85, 80, 65]
        }
        st.bar_chart(chart_data, x="Skill Category", y="Proficiency")

# GPA calculator interactive widget (meets interactive element requirement)
st.write("---")
st.write("### GPA Calculator")
num_courses = st.number_input("How many courses to include in GPA calc?", min_value=1, max_value=10, value=4)
grades = []
for i in range(num_courses):
    grades.append(st.selectbox(f"Course {i+1} Grade", ['A','A-','B+','B','B-','C+','C','C-','D','F'], key=f"grade_{i}"))
if st.button("Calculate GPA"):
     gpa = calculate_gpa(grades)
     st.write(f"Your GPA is: **{gpa:.2f}**")
     if gpa >= 3.5:
         st.success("Excellent work! Dean's List level.")
     elif gpa >= 3.0:
          st.info("Good job! Keep improving.")
     else:
          st.warning("Consider seeking academic support.")

# -----------------------------
# Projects Page
# -----------------------------
elif page == 

        {
            "title": "Pinterest Makeup Recreation",
            "description": "Recreated several Pinterest makeup looks and documented the process through before/after photos. This helped develop my creativity and beauty-content skills.",
            "technologies": ["Makeup Skills", "Photography", "Lighting Setup"],
            "status": "Completed"
        },
        {
            "title": "Office of Communication Internship",
            "description": "Expanded my photography skills by capturing campus events, editing photos, and collaborating with the communications team.",
            "technologies": ["Photography", "Photo Editing", "Team Collaboration"],
            "status": "Completed"
        },
        {
            "title": "Portfolio Website (CIS 211 Project)",
            "description": "Built a complete Streamlit portfolio website using Python, including interactive features, GPA calculator, and multipage navigation.",
            "technologies": ["Python", "Streamlit", "Web Development"],
            "status": "In Progress"
        }
    ]

    # Function to display each project in an expandable card
    def display_project(project):
        with st.expander(project["title"]):
            st.write(f"**Description:** {project['description']}")
            st.write(f"**Technologies Used:** {', '.join(project['technologies'])}")
            st.write(f"**Status:** {project['status']}")
            if project["status"] == "In Progress":
                st.progress(0.5)

    # Filter option
    status_filter = st.selectbox("Filter by status:", ["All", "Completed", "In Progress"])

    # Apply filter
    for project in projects:
        if status_filter == "All" or project["status"] == status_filter:
            display_project(project)
            st.write("---")

# -----------------------------
# Contact Page
# -----------------------------
elif page == "Contact":
    st.header("Contact Me")
    st.write("I'd love to collaborate — please send a message.")
    with st.form("contact_form", clear_on_submit=True):
         name = st.text_input("Asheana Juman")
         email = st.text_input("Jumanasheana@gmail.com")
         subject = st.selectbox("Subject", ["General Inquiry", "Collab", "Job Opportunity", "Other"])
         message = st.text_area("Message", height=105)
         submit = st.form_submit_button("Send")
         if submit:
            if not name or not email or not message:
               st.error("Please fill all fields.")
            else:
                 record = send_contact_message(name, email, subject, message)
                 st.success(f"Thanks {name}! Message recorded at {record['time']}.")
                 st.write("**Message preview:**")
                 st.write(f"From: {record['name']} ({record['email']})")
                 st.write(f"Subject: {record['subject']}")
                 st.write(record['message'])

# -----------------------------
# Footer & style
# -----------------------------
st.markdown("""<hr style='border:1px solid #e6e6e6'>""", unsafe_allow_html=True)
st.caption("© Asheana Juman — Portfolio created for CIS 211. Built with Streamlit.")
214 |
215 | # End of file
