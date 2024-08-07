import streamlit as st

st.set_page_config(page_title='Portfolio', page_icon='😎', layout='wide')

with st.sidebar:
    st.header("Navigation")
    st.page_link("main.py", label = "Home", icon=":material/home:")
    st.page_link("pages/education.py", label = "Education", icon=":material/school:")
    st.page_link("pages/projects.py", label = "Projects", icon=":material/workspaces:")
    st.page_link("pages/resume.py", label = "Resume", icon=":material/description:")
    st.page_link("pages/contact me.py", label = "Contact me", icon=":material/contact_page:")

r0 = st.columns(2)

with r0[0]:
    st.html(
"""
<style>
* {
    font-family: Calibri, sans-serif;
}
.name {
    font-size: 70px;
    font-weight: 600;
    letter-spacing: 3px;
    color: #5aadfa;
}
</style>
<p class="name">
SHABARI <br> K S
</p>
"""
    )

with r0[1]:
    st.html(
"""
<style>
.c {
    list-style-type: none;
    margin: 0;
    margin-top: 10px;
    padding: 0;
    overflow: hidden;
    text-align: right;
    font-size: 20px;
}
a {
    all: unset;
    color: #5aadfa;
    text-decoration: none;
}
</style>
<ul class="c">
    <li><a href="https://shabari-portfolio.onrender.com">shabari-portfolio.onrender.com</a></li>
    <li>shabaricse2003@gmail.com</li>
    <li>431 Anna Nagar, Ponnamapet, Salem, Tamil Nadu, India</li>
    <li>+91 90039 99784</li>
    <li><a href="https://github.com/Shabari-K-S">github.com/Shabari-K-S</a></li>
    <li><a href="https://linkedin.com/in/shabari-k-s">linkedin.com/in/shabari-k-s</a></li>

"""
    )




st.html(
"""
<style>
.heading {
    font-size: 35px;
    font-weight: 500;
    letter-spacing: 3px;
    color: #5aadfa;
}

hr {
    color : #5aadfa;
    margin-top: -10px;
    border-top: .1px solid #5aadfaa0;
}
.passage-1 {
    text-align: justify;
    font-size: 20px;
    font-weight: 100;
    letter-spacing: 1px;
    color: #cfcfcf;
}
ul {
    text-align: justify;
    list-style-type: circle;
    margin: 0;
    padding: 0;
    font-size: 20px;
    font-weight: 100;
    letter-spacing: 1px;
    font-family: mono;
}
h1 {
    color: #5aadfa;
}
li {
    color: #cfcfcf;
}
.dot::before {
    content: "•"; /* Insert content that looks like bullets */
    padding-right: 8px;
    color: white; /* Or a color you prefer */
}

li {
    width: 100%;
}

</style>
<p class="heading">
SUMMARY
</p>
<hr>
<p class="passage-1">
My name is Shabari K S. I am currently pursuing Final Year in Knowledge Institute of Technology as a Computer Science Engineer. I am passionate in Ethical Hacking and Web development. I am Pro Hacker on Hack The Box. I am competitive programmer and also web developer.
</p>
<p class="heading">
PROJECTS
</p>
<hr>
<h1 class="dot" style='margin-top: 7.15pt; margin-right: 0in; margin-bottom: 0.0001pt; font-size:  20px; font-family: "Trebuchet MS", sans-serif;'> STUDENT MARK AND PLACEMENT PREDICTION</h1>

<ul style="margin-left: 49px;">
    <li style="font-size:  20px; font-family: Calibri, sans-serif; margin-top: 4.25pt; margin-right: 0in; margin-bottom: 0.0001pt; color: rgb(255, 255, 255);">We created this project as a team.</li>
    <li style="font-size:  20px; font-family: Calibri, sans-serif; margin-top: 3.25pt; margin-right: 0in; margin-bottom: 0.0001pt; color: rgb(255, 255, 255);">I played the role of both Web Developer and Data Analyst</li>
    <li style="font-size:  20px; font-family: Calibri, sans-serif; margin-top: 3.2pt; margin-right: 0in; margin-bottom: 0.0001pt; color: rgb(255, 255, 255);">In this i gained some knowledge in Python Programming Language.</li>
</ul>
<h1 class="dot" style='margin-top: 7.15pt; margin-right: 0in; margin-bottom: 0.0001pt; font-size:  20px; font-family: "Trebuchet MS", sans-serif;'> PHISHING DETECTION WEBSITE</h1>

<ul style="margin-left: 49px ;">
    <li style="font-size:  20px; font-family: Calibri, sans-serif; margin-top: 4.2pt; margin-right: 231.5pt; margin-bottom: 0.0001pt; line-height: 123%; color: rgb(255, 255, 255);"><span style="font-size: 13px; line-height: 123%;">  </span>Led team to develop a phishing detection website.</li>
    <li style="font-size:  20px; font-family: Calibri, sans-serif; margin-top: 4.2pt; margin-right: 231.5pt; margin-bottom: 0.0001pt; line-height: 123%; color: rgb(255, 255, 255);"> Built and deployed a phishing detection ML model.</li>
    <li style="font-size:  20px; font-family: Calibri, sans-serif; margin-top: 0.05pt; margin-right: 0in; margin-bottom: 0.0001pt; color: rgb(255, 255, 255);"><span style="font-size: 13px;"> </span>Enhanced online security with advanced detection systems..</li>
</ul>
<h1 class="dot" style='margin-top: 10.15pt; margin-right: 0in; margin-bottom: 0.0001pt; font-size:  20px; font-family: "Trebuchet MS", sans-serif;' >  WEATHER FORECASTING APP</h1>

<ul style="margin-left: 49px ;">
    <li style="font-size:  20px; font-family: Calibri, sans-serif; margin-top: 4.15pt; margin-right: 177.95pt; margin-bottom: 0.0001pt; line-height: 123%; color: rgb(255, 255, 255);">Developed a weather forecasting app using Tkinter in Python. </li>
    <li style="font-size: 20px; font-family: Calibri, sans-serif; margin-top: 4.15pt; margin-right: 177.95pt; margin-bottom: 0.0001pt; line-height: 123%; color: rgb(255, 255, 255);">Integrated OpenWeather API for real-time weather data.</li>
    <li style="font-size: 20px; font-family: Calibri, sans-serif; margin-top: 0.1pt; margin-right: 0in; margin-bottom: 0.0001pt; color: rgb(255, 255, 255);">Completed project independently, ensuring accurate and user-friendly interface.</li>
</ul>
<h1 class="dot" style='margin-top: 10.15pt; margin-right: 0in; margin-bottom: 0.0001pt; font-size: 20px; font-family: "Trebuchet MS", sans-serif;'> JSW-OHC MEDICAL RECORD MANAGEMENT APP</h1>
<ul style="margin-left: 49px ;">
    <li style="font-size: 20px; font-family: Calibri, sans-serif; margin-top: 4.15pt; margin-right: 183.20pt; margin-bottom: 0.0001pt; line-height: 123%; color: rgb(255, 255, 255);">Developed a web app for managing medical records at JSW. </li>
    <li style="font-size: 20px; font-family: Calibri, sans-serif; margin-top: 4.15pt; margin-right: 183.15pt; margin-bottom: 0.0001pt; line-height: 123%; color: rgb(255, 255, 255);">Utilized Python for the app development.</li>
    <li style="font-size: 20px; font-family: Calibri, sans-serif; margin-top: 0.1pt; margin-right: 0in; margin-bottom: 0.0001pt; color: rgb(255, 255, 255);">Ensured efficient handling and secure storage of medical data.</li>
</ul>
<h1 class="dot" style='margin-top: 7.15pt; margin-right: 0in; margin-bottom: 0.0001pt; font-size: 20px; font-family: "Trebuchet MS", sans-serif;'> MULTI-LANGUAGE CODE EDITOR</h1>
<ul style="margin-left: 49px ;">
    <li style="font-size: 20px; font-family: Calibri, sans-serif; margin-top: 4.15pt; margin-right: 0in; margin-bottom: 0.0001pt; color: rgb(255, 255, 255);">Hackathon Project, inspired by VS Code</li>
    <li style="font-size: 20px; font-family: Calibri, sans-serif; margin-top: 3.25pt; margin-right: 0in; margin-bottom: 0.0001pt; color: rgb(255, 255, 255);">Created a multi-language code editor using Python.</li>
    <li style="font-size: 20px; font-family: Calibri, sans-serif; margin-top: 3.2pt; margin-right: 0in; margin-bottom: 0.0001pt; color: rgb(255, 255, 255);">Enabled support for multiple programming languages.</li>
    <li style="font-size: 20px; font-family: Calibri, sans-serif; margin-top: 3.25pt; margin-right: 0in; margin-bottom: 0.0001pt; color: rgb(255, 255, 255);">Designed and developed the project inspired by VS Code&apos;s functionality.</li>
</ul>
<div style="width:100%;height:70px">

</div>
<p class="heading">
EDUCATION
</p>
<hr>
"""
)
def education(year:str, name:str, course:str, grade:str):
    with st.container():
        r1 = st.columns([2,9])
        with r1[0]:
            st.subheader(year)
        with r1[1]:
            st.subheader(f":blue[{name}]")
            st.html(f"<p class='passage-1'>{course}")
            st.write(f"{grade}")


education("2021 - 2025", "Knowledge Institute of Technology, Salem", "B.E Computer Science and Engineering", "CGPA : 8/10")
education("2020 - 2021", "Bharathi Vidyalaya Higher Secondary School, Salem", "HSC", "Percentage : 80 %")
education("2018 - 2019", "Bala Bharathi Matriculation Higher Secondary School, Salem", "SSLC", "Percentage : 72.3 %")


st.html(
"""
<p class="heading">
SKILLS
</p>
<hr>
"""
)
r2 = st.columns([1,6,9])
with r2[1]:
    st.html(
"""
<ul style="margi-left:10px">
<li>Python (Advanced)</li>
<li>C / C++ (Basic)</li>
<li>HTML / CSS / JavaScript</li>
<ul>
""")

with r2[2]:
    st.html(
"""
<ul style="margi-left:10px">
<li>Java (Intermediate)</li>
<li>Basic Communication Skills</li>
<li>React</li>
</ul>
""")

st.html(
"""
<p class="heading" style="margin-top:10px">
CERTIFICATIONS
</p>
<hr>
"""
)

def certification(date: str,name:str, desc:str):
    with st.container():
        r1 = st.columns([1,9])
        with r1[0]:
            st.subheader(date)
        with r1[1]:
            st.subheader(name)
            st.html(f"<p class='passage-1'>{desc}")

certification("2023", "Foundation of AIML - Naan Mudhalvan", "I learned Fundamentals and basic concepts in Artificial Intelligence and Machine Learning")
certification("2023", "INTRODUCTION TO IT & CYBERSECURITY - CYBRARY", "Upskilled myself to the world of cyber security")
certification("2022", "JAVA – HACKER RANK", "Earned 5 star successfully in Hacker Rank")
certification("2022", "PYTHON – HACKER RANK", "Earned 5 star successfully in Hacker Rank")
certification("2022", "CISCO NETWORK ACADEMY – PYTHON ESSENTIAL - INTERNSHIP", "Cisco Virtual Intern on the topic of PCAP: Programming Essential In Python")
certification("2022", "CYBER SECURITY – INTERNSHIP", "I have successfully completed my project in Verzeo intenship based on cyber security")
certification("2019", "PGDCA", "I got my Certificate of Post Graduate Diploma in Computer Applications in Computer center")
certification("2019", "DHN", "I got my Certificate of Diploma in Hardware & Networking	in Computer center")

st.html(
"""
<p class="heading">
PROFESSIONAL AFFILIATIONS
</p>
<hr>
"""
)

r4 = st.columns([1,9])
with r4[0]:
    st.subheader("2023")

with r4[1]:
    st.subheader("STREAMLIT")
    st.html("<p class='passage-1' style='margin-top:-10px'>Student Ambassador in the Streamlit Community</p>")


st.html(
"""
<p class="heading">
HONORS AND AWARDS
</p>
<hr>
"""
)

def honors(date:str, name:str, desc:str):
    with st.container():
        r1 = st.columns([1,9])
        with r1[0]:
            st.subheader(date)
        with r1[1]:
            st.subheader(name)
            st.html(f"<p class='passage-1'>{desc}")

honors("2023", "AKERVA FORTRESSES – HACK THE BOX", "I've pwned the Akerva fortress on Hack The Box! After many fails and persistent effort, I successfully breached its defenses and emerged victorious!")
honors("2023", "FARADAY FORTRESSES – HACK THE BOX", "I've pwned the Faraday fortress on Hack The Box!, I successfully breached its defenses and emerged victorious!")
honors("2023", "ACHIEVER’S AWARD", "I got this award in my college Knowledge Institute Of Technology")
honors("2024", "CERTIFICATE OF APPRECIATION", "I got this award in my college Knowledge Institute Of Technology")
