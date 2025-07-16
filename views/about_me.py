import streamlit as st


from form.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


resume_file_path = "cv.pdf"

# Read the PDF file as bytes
with open(resume_file_path, "rb") as pdf_file:
    pdf_bytes = pdf_file.read()

# Define the file name for the download button
resume_filename = "cv.pdf"


# Adjust the width ratios and add a spacer column between col1 and col2
col1, spacer, col2 = st.columns([2, 0.2, 3.8], gap="small")

with col1:
    st.image("221.png" , use_container_width=True)

with col2:
    st.title("Caryll Franz M. Cariño", anchor=False)
    st.write(
        "Aspiring AI Engineer and Data Scientist"
    )

    st.write(
      "📧 caryllcarino@gmail.com"
    )
   
    st.download_button(
    label="Download Resume",
    data=pdf_bytes,
    file_name=resume_filename,
    mime="application/pdf"
)




    # if st.button("📩 Contact me"):
    #     show_contact_form()





st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" '
    'integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" '
    'crossorigin="anonymous">',
    unsafe_allow_html=True
)

# #--SKILLS

# st.write("\n")

# st.subheader("Hard Skills", anchor=False)

# st.write(
#     """
#     - Technical skills: Excel, Sql, Figma, Cisco, MS Word, Tinkercad, Tableau, Power BI

#     - Programming and Development: Python, Javascript, HTML, CSS, Arduino (C++), XAML, PHP

#     - Specialized Tools and Libraries: Roboflow, Open CV, Pandas

#     """
# )

# # EXPERIENCES

# st.write("\n")

# st.subheader("Education", anchor=False)

# st.write(
#     """
#     **Adamson University**


#     - BS IN COMPUTER ENGINEERING Aug 2020 – July 2024


#     **Kings Montessori School**
#     - ABM  (ACCOUNTANCY, BUSINESS, AND MANAGEMENT) Aug 2018 – April 2020


#     """
# )

# st.write("\n")
# st.subheader("Experience", anchor=False)
# st.write(
#     """
#     **Technomancer**

#     - Web developer intern July 2023 – Aug 2023

#     - developed web applications with PHP, created CRUD functionalities, and gained experience with Laravel routing, while assisting with
#     front-end development.



#     """
# )


# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**BS Computer Engineering**, *Adamson University*, Philippines',
'2020-2024')
st.markdown('''
- GPA: `2.00`
- Research thesis entitled `SPOTSECURE:PARKING RESERVATION SYSTEM WITH PLATE NUMBER RECOGNITION THROUGH IMAGE PROCESSING`.
''')

# txt('**ABM** (ACCOUNTANCY, BUSINESS, AND MANAGEMENT), *Kings Montessori School*, Philippines',
# '2018-2020')
# st.markdown('''
# - GPA: `3.65`
# ''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Technomancer**', 'July 2023- Aug 2023')
st.markdown('''
- Developed web applications with PHP
- Created CRUD functionalities
- Gained experience with Laravel routing
- Assisted with front-end development
''')

txt('**Accenture – Java Full Stack Trainee**', 'Oct 2024–Dec 2025')
st.markdown('''
- Completed a 3-month Java Full Stack Bootcamp covering Java, Spring Boot, HTML, CSS, JavaScript, and MySQL
- Debugged and enhanced backend applications using Spring Boot
- Practiced problem-solving through LeetCode challenges
- Gained exposure to DevOps tools like Jenkins and testing with Selenium
''')

txt('**Accenture – Package App Development Assosciate**', 'Jan 2025–Present')
st.markdown('''
- Automated SQL-based report generation using Python, including pivot tables and email delivery
- Resolved support tickets using ServiceNow and debugged Java backend applications
- Performed minor code enhancements in production systems
- Participated in a company hackathon and used GitHub Copilot to improve workflow
''')


########

st.markdown('''
## Projects
''')

# 1st project – SPOTSECURE
st.markdown('**SPOTSECURE: Parking Reservation System with Plate Number Recognition through Image Processing**', unsafe_allow_html=True)
st.markdown('`HTML, Flutter, CSS, SQLite, Python, YOLOv5, API`')
st.markdown('''
Developed a mobile app for parking reservations and a web app for admin users, displaying user and vehicle data. Integrated a Python script using YOLOv5 for automatic plate recognition and database validation. The system was connected to an Arduino-controlled barrier that triggered access or alerts based on recognition results.
''')

# 2nd project – Object Detection
st.markdown('**YOLOv5-based Object Detection for AC, DC, and Battery Chargers**')
st.markdown('`Python, Google Colab, Roboflow`')
st.markdown('''
Built an object detection system using YOLOv5 to classify AC power supplies, DC power supplies, and battery chargers from images and video frames.
''')

# 3rd project – Network Design
st.markdown('**Designing a Scalable Network Topology for Region 2 in the Philippines Using EIGRP and VLSM**')
st.markdown('`Cisco`')
st.markdown('''
Designed a scalable and efficient network topology for Region 2 using Enhanced Interior Gateway Routing Protocol (EIGRP) and Variable Length Subnet Masking (VLSM).
''')

# 4th project – Automated Reporting Tool
st.markdown('**Automated Reporting Tool for SQL-Based Reports**')
st.markdown('`Python, SQL, pandas, openpyxl`')
st.markdown('''
Created a Python script to automate data extraction from SQL databases, generate pivot-based Excel reports, and send them via email, improving reporting accuracy and reducing manual work.
''')

# # 5th project – Heart Disease Prediction
# st.markdown('**Heart Disease Prediction Using Machine Learning**')
# st.markdown('`Python, pandas, matplotlib, scikit-learn`')
# st.markdown('''
# Analyzed heart disease datasets to identify key risk factors and correlations. Preprocessed data, trained ML models, and evaluated performance to predict heart disease likelihood with improved accuracy.
# ''')







#####################
st.markdown('''
## Skills
''')


# Replacing with your skills
txt3('Programming Languages', '`Python`, `Java`, `JavaScript`')
txt3('Web & Backend Development', '`Spring Boot`, `HTML`, `CSS`, `JavaScript`, `Bootstrap`')
txt3('Data Handling & Analysis', '`SQL`, `pandas`, `numpy`, `Excel`')
txt3('Data Visualization', '`matplotlib`, `Power BI`, `Tableau`')
txt3('Machine Learning & CV', '`YOLO`, `Roboflow`, `OpenCV`')
txt3('Deployment & Automation', '`streamlit`, `Vercel`, `Jenkins`, `Selenium`, `Git`')
txt3('Other Tools & Platforms', '`Figma`, `MS Office`, `ServiceNow`, `GitHub Copilot`, `Cisco`')



#####################
st.markdown('''
## Social Media
''')



txt2('LinkedIn', 'https://www.linkedin.com/in/caryllfmc/')
txt2('GitHub', 'https://github.com/caryllfranz')
txt2('Facebook', 'https://www.facebook.com/seeshaboat/')
