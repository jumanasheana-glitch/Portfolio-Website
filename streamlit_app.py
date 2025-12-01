import streamlit as st 
import pandas as pd
from datetime import datetime

import streamlit as st

# Configure the page

st.set_page_config(
    page_title="Asheana Juman - Portfolio",
    page_icon="🎨",
    layout="wide")


# Create sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Skills", "Projects", "Contact"])

# Display different pages based on selection
if page == "Home":
    st.title("Welcome to My Portfolio")
    st.write("This is the home page")
    
elif page == "About Me":
    st.title("About Me")
    st.write("This is the about page")
    
elif page == "Skills":
    st.title("Skills & Experience")
    st.write("This is the skills page")
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
    with tab3:
        st.write("My ultimate goal is to earn a bachelor's and associate's degree in business administration.  My goal is to become an investor and contribute to raising awareness of a small business with a mission.")


elif page == "Skills":
    st.header("Skills & Experience")
    Col1, col2 = st.columns(2)
    with col1:
        st.write("### Technical Skills")
        for skill in technical_skills:
            st.write(f"- {skill}")
        st.write("### Tools & Platforms")
        st.write("- Streamlit  - Python - Excel - Canva")
         st.write("### Technical Proficiency")
         py = st.slider("Python proficiency", 0, 100, 60)
         ex = st.slider("Excel proficiency", 0, 100, 80)
         html = st.slider("HTML/CSS proficiency", 0, 100, 40)
    with col2:
        st.write("### Soft Skills")
        for skill in soft_skills:
            st.write(f"- {skill}")
        st.write("### Portfolio Snapshot")
        df = pd.DataFrame({
             "Skill Category": ["Technical", "Analytical", "Communication", "Leadership"],
             "Proficiency": [py, ex, 75, 65]
       })
       st.bar_chart(df.set_index("Skill Category"))
       st.write("---")
       st.write("### Photography Sample (describe here)")
       st.write("I photograph makeup work for portfolios and events. (Add image files to expand.)")
            
# Add progress bar for in-progress projects
  if project["status"] == "In Progress":
         progress = st.progress(0.6)
         st.write("60% Complete")
 elif project["status"] == "Completed":
         st.success("Project Completed!")

    for project in projects:
        display_project(project)
        st.write("---")  # Separator line
    
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
        name = st.text_input("Asheana Juman")
        email = st.text_input("jumanasheana@gmail.com")
        subject = st.selectbox("Subject", 
                              ["General Inquiry", "Project Collaboration", 
                               "Job Opportunity", "Other"])
        message = st.text_area("Message", height=105)
        
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
    
def calculate_gpa(grades):
    """Calculate GPA from a list of letter grades"""
    grade_points = { 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D': 1.0, 'F': 0.0}
    if not grades:
        return 0.0
    
    total_points = sum(grade_points.get(grade, 0) for grade in grades)
    return total_points / len(grades)


st.write("### GPA Calculator")
st.write("2.9")

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
    
