import streamlit as st 
import pandas as pd
from datetime import datetime

import streamlit as st

# Configure the page
st.set_page_config(
    page_title="Asheana Juman - Portfolio",
    page_icon=":book:",
    layout="wide"
)

# Create sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home 🧿", "About Me 👾", "Skills⚙️", "Projects 🔍", "Contact📲"])

# Display different pages based on selection
if page == "Home🧿":
    st.title("Welcome to My Portfolio")
    st.write("This is the home page")
    
elif page == "About Me👾":
    st.title("About Me")
    st.write("Hello, my name is Asheana Juman, and I'm invested in creating something significant for myself and other people, as well as beauty and creativity. I adore making daring and distinctive makeup looks and posting them online because it allows me to showcase my artistic abilities and interact with others who share my passion for creation. 
In addition, I'm striving to become a future investor and businesswoman. Supporting small companies and assisting in the realization of innovative ideas are my objectives. In order to broaden my capabilities and comprehend how digital technologies fuel modern companies, I'm now acquiring the technical skills I'll need along the way, such as coding in my CIS 211 class. This space is dedicated to my personal, professional, and artistic development. Stay tuned to follow my journey as I develop my abilities and pursue my goals.
")
    
elif page == "Skills ⚙️":
    st.title("Skills & Experience")
    st.write("This is the skills page")
    
elif page == "Projects🔍":
    st.title("My Projects")
    st.write("This is the projects page")
    
elif page == "Contact📲":
    st.title("Contact Me")
    st.write("This is the contact page")
    # Add this after imports, before the page config

# Dictionary for personal information
personal_info = {
    "name": "Your Name",
    "title": "Business Information Systems Student",
    "email": "your.email@example.com",
    "location": "Brooklyn, NY",
    "graduation": "May 2027"
}

# List of skills
technical_skills = ["Python", "Data Analysis", "Streamlit", "Problem Solving"]
soft_skills = ["Communication", "Team Work", "Time Management", "Leadership"]

# List of dictionaries for projects
projects = [
    {
        "title": "Project 1 Name",
        "description": "Brief description of what this project does",
        "technologies": ["Python", "Streamlit"],
        "status": "Completed"
    },
    {
        "title": "Project 2 Name",
        "description": "Brief description of what this project does",
        "technologies": ["Excel", "Data Analysis"],
        "status": "In Progress"
    }
]
if page == "Home":
    st.title(f"Welcome! I'm {personal_info['name']}")
    st.subheader(personal_info['title'])
    
    # Create columns for layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("## Quick Introduction")
        st.write("""
        I am a motivated student studying Business Information Systems 
        at Medgar Evers College. I am passionate about technology and 
        its applications in business.
        """)
        
    with col2:
        st.write("## Quick Facts")
        st.write(f"**Location:** {personal_info['location']}")
        st.write(f"**Expected Graduation:** {personal_info['graduation']}")
        st.write(f"**Email:** {personal_info['email']}")
        elif page == "About Me":
    st.title("About Me")
    
    # Add tabs for organization
    tab1, tab2, tab3 = st.tabs(["Education", "Interests", "Goals"])
    
    with tab1:
        st.write("### Educational Background")
        st.write("**Medgar Evers College, CUNY**")
        st.write("Bachelor of Science in Business Information Systems")
        st.write("Expected Graduation: " + personal_info['graduation'])
        
        # Add GPA or relevant coursework
        st.write("**Relevant Coursework:**")
        courses = ["Internet and Emerging Technologies", "Database Management", 
                  "Business Analysis", "Programming Fundamentals"]
        for course in courses:
            st.write(f"- {course}")
    
    with tab2:
        st.write("### My Interests")
        # Add your interests here
        
    with tab3:
        st.write("### Career Goals")
        # Add your goals here
elif page == "Skills":
    st.title("Skills & Experience")
    
    # Create two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### Technical Skills")
        for skill in technical_skills:
            st.write(f"- {skill}")
        
        # Add skill proficiency bars
        st.write("### Skill Proficiency")
        python_level = st.slider("Python", 0, 100, 60, disabled=True)
        excel_level = st.slider("Excel", 0, 100, 80, disabled=True)
        html_level = st.slider("HTML/CSS", 0, 100, 40, disabled=True)
        
    with col2:
        st.write("### Soft Skills")
        for skill in soft_skills:
            st.write(f"- {skill}")
            
        # Add a simple chart
        st.write("### Skills Distribution")
        import random
        chart_data = {
            "Skill Category": ["Technical", "Analytical", "Communication", "Leadership"],
            "Proficiency": [70, 65, 80, 60]
        }
        st.bar_chart(data=chart_data, x="Skill Category", y="Proficiency")
    elif page == "Projects":
    st.title("My Projects")
    
    # Function to display project cards
    def display_project(project):
        with st.expander(project["title"]):
            st.write(f"**Description:** {project['description']}")
            st.write(f"**Technologies Used:** {', '.join(project['technologies'])}")
            st.write(f"**Status:** {project['status']}")
            
            # Add progress bar for in-progress projects
            if project["status"] == "In Progress":
                progress = st.progress(0.6)
                st.write("60% Complete")
            elif project["status"] == "Completed":
                st.success("Project Completed!")
    
    # Display all projects
    for project in projects:
        display_project(project)
        st.write("---")  # Separator line
    
    # Add option to filter projects
    st.write("### Filter Projects")
    status_filter = st.selectbox("Filter by status:", 
                                 ["All", "Completed", "In Progress"])
    
    if status_filter != "All":
        filtered = [p for p in projects if p["status"] == status_filter]
        st.write(f"Showing {len(filtered)} projects with status: {status_filter}")
  elif page == "Contact":
    st.title("Contact Me")
    
    st.write("Feel free to reach out for collaborations or opportunities!")
    
    # Create a form
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        subject = st.selectbox("Subject", 
                              ["General Inquiry", "Project Collaboration", 
                               "Job Opportunity", "Other"])
        message = st.text_area("Message", height=150)
        
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            if name and email and message:
                st.success(f"Thank you {name}! Your message has been received.")
                # In a real application, you would send an email here
                st.write("**Message Summary:**")
                st.write(f"From: {name} ({email})")
                st.write(f"Subject: {subject}")
                st.write(f"Message: {message[:100]}...")
            else:
                st.error("Please fill in all required fields.")
    # Add this function before your main page logic
def calculate_gpa(grades):
    """Calculate GPA from a list of letter grades"""
    grade_points = {
        'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0,
        'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D': 1.0, 'F': 0.0
    }
    
    if not grades:
        return 0.0
    
    total_points = sum(grade_points.get(grade, 0) for grade in grades)
    return total_points / len(grades)

# Add to your Skills or About page
st.write("### GPA Calculator")
st.write("Enter your grades to calculate your GPA")

num_courses = st.number_input("How many courses?", min_value=1, max_value=10, value=4)
grades = []

for i in range(num_courses):
    grade = st.selectbox(f"Course {i+1} Grade:", 
                         ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'F'],
                         key=f"grade_{i}")
    grades.append(grade)

if st.button("Calculate GPA"):
    gpa = calculate_gpa(grades)
    st.write(f"Your GPA is: {gpa:.2f}")
    
    if gpa >= 3.5:
        st.success("Excellent work! Dean's List level performance!")
    elif gpa >= 3.0:
        st.info("Good job! Keep up the solid work!")
    elif gpa >= 2.0:
        st.warning("You're passing, but there's room for improvement.")
    else:
        st.error("Consider seeking academic support.")
# Add custom CSS (place after page config)
st.markdown("""
<style>
    .main-header {
        font-size: 42px;
        font-weight: bold;
        color: #1E3A8A;
    }
    .sub-header {
        font-size: 20px;
        color: #64748B;
    }
</style>
""", unsafe_allow_html=True)

# Use in your pages
st.markdown('<p class="main-header">Welcome to My Portfolio</p>', 
            unsafe_allow_html=True)
    
