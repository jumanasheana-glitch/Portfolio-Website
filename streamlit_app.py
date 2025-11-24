import streamlit as st 
import pandas as pd
from datetime import datetime

# Page Config
st.set_page_config(
  page_title = 'Asheana Juman | Portfolio',
  page_icon='🧿',
  layout = 'wide'
)

# Custom CSS (optional - for styling)
st.markdown('''
                <style>
                    .main-header {font-size: 42px; font-weight: bold; text-align:center;}
                    .sub-header {font_size: 24px; text-align:center; color: #666;}
                </style>
            ''', unsafe_allow_html = True) 

# Sidebar
st.sidebar.title('📍 Navigation')
page = st.sidebar.radio('Go to',
                        ['🐱‍💻 Welcome ', '🧍‍♀️ About', '🛠 Experience ', '📽 Project', '📩 Contact'])

# Home Page
if page == '🐱‍💻 Welcome':
 st.markdown('<p class="main-header">Asheana Juman</p>', unsafe_allow_html=True)
 st.markdown('<p class="sub-header">Aspiring Business Professional | Medgar Evers College</p>',unsafe_allow_html=True)

# Three Columns for stats
col1, col2, col3 = st.columns (3)

with col1:
    st.metric('GPA', '3,0', '📗')
with col2:
    st.metric('Projects', '5','💻')
with col3:
    st.metric('Skills', '10+', '🚀')

st.write('---')

 # Introduction with columns
col1, col2 = st.columns([2,1])
with col1:
    st.subheader('Welcome to my Portfolio Page!👋')
    st.write('''
                
                I am a student that currently attending Medagr Evers College. Who's currently learning HTML, CSS, Javascript, and Python to build innovative solutions.
               
                🎯 **Current Focus:** Building interactive web applications with Streamlit
            
                📚 **Currently Learning:** Internet and Emergin Technologies (CIS 211)
            
                🌱 **Fun Fact:** I can love doing cool makeup looks !
            ''')
  with col2:
    # Placeholder for image
  st.image('https://raw.githubusercontent.com/asheana.juman/cis211_project1/refs/heads/main/funny cat.jfif', use_column_width=True)

# About Page
 elif page == '🐱‍💻 Welcome':
  st. title ('About Me')

# Timeline of my professional Journey
 st.subheader('my journey 🗺')'

with st.expander('2023 - Present: Medgar Evers College'):
  st.write('''
            - Major: Business Admin
            - Relevant Coursework: Internet & Emerging Technologies, Programming, Database Systems, AI
                - Activities: 
            ''')

st.expander('2021 - 2023: Epic South High School')
 st.write('''
                - Graduated
                 ''')



  st.subheader('Interests & Hobbies 🏎')
  interests = ['Building legos', 'Reading Fictional books', 'Photography', 'Forumla 1', 'Cool Makeup looks']

  # Display the interests in columns
cols = st.columns(3)
  for i, interest in enumerate(interests):
    with cols[i % 3]:
      st.info(f'🔷 {interest}')
elif page == '🧍‍♀️ About':
  st.titlw('My Projects')

  st.write('Here are some projects I have worked on')
  # Project 1
  with st.container():
    col1, col2 = st.columns([1, 2])
  
    with col1:
        st.image('

    with col2:
        st.subheader(' Porjects that i worked on')
        st.write('Python web scraper that monitors Amazon prices and sends alerts')
        st.caption('**Technologies:** Python, BeautifulSoup, Streamlit')


# Project 2
with st.container():
    col1, col2 = st.columns([1,2])
    with col1:
      st.image('https://www.publicdomainpictures.net/pictures/90000/nahled/calculator-black-clipart.jpg')
    with col2:
      st.subheader('📊 Student Grade Calulator')
      st.write('Interactive web app for calculating and visualizing grades')
      st.caption('**Technologies:** Python, Pandas, Plotly')

elif page == '🛠 Skills':
  st.tile ('Technical Skills')

  # Skills with progress bars
  st.subheader('Programming Languages')

  skills_data = {
    'Python' : 85,
    'HTML/CSS' : 70,
    'JavaScript' : 60,
    'SQL' : 50,
    'Technical Writing' : 40
  }

  for skill, level in skills_data.items():
    col1, col2 = st.columns([1,3])
    with col1:
      st.write(skill)
    with col2:
      st.progress(level/100)

st.subheader('Tools & Technology')

col1, col2, col3 = st.columns(3)
with col1:
   st.success('Excel')
    st.info('Word')
    st.warning('Access')

  with col2:
    st.success('PowerPoint')
    st.info('Google Docs')
    st.warning('ChatGPT/AI Tools')
    
  with col3:
    st.success('Presentations')
    st.info('Writing')
    st.warning('Social Media')
    

elif page == '📄 Resume':
  st.title('Resume')

  # Read PDF from my GitHub repository
with open('my_resume.pdf', 'rb') as pdf_file:
  PDFbyte = pdf_file.read()

st.download_button(
  label ='🔻 Download Full Resume (PDF)',
  data = PDFbyte,
  file_name = 'my_resume.pdf',
  mime ='application/pdf'
)

elif page == '📩 Contact':
  st.title("Let's Connect!")

  col1, = st.columns(1)

  with col1:
    st.subheader('Send me a message.')

    st.write('''
        📧 **Email:** Jumanasheana@gmail.com

        🏢 **LinkedIn:** [linkedin.com/in/yourname]

        👩‍💻 **Github:** [/https://github.com/jumanasheana-glitch]

        📷 **Instagram:** [@yourhandle(https://instagram.com)]

    ''')

# Fun interative element
    st.subheader('Current Status')

    status = st.selectbox(
        "I'm currently:",
        [
            '👩‍💻 Coding',
            '📕 Studying',
            '☕ On a coffee break',
            '🎮 Gaming',
            '😴 Sleeping'
        ]
    )


    st.info(f'Status: {status}')
    
    # Footer
    st.write('---')
    st.markdown(
        f'<center>Made with 💗 using Streamlit | © {datetime.now().year} Avinash Jairam </center>',
        unsafe_allow_html = True
    )
