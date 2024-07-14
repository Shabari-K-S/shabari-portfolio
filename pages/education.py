import streamlit as st
from PIL import Image
import base64
import io
import json
from streamlit_lottie import st_lottie

def load_lottie_file(filepath: str):
    with open(filepath) as f:
        return json.load(f)

st.set_page_config(page_title='Portfolio', page_icon='😎', layout='wide')

with st.sidebar:
    st.header("Navigation")
    st.page_link("main.py", label = "Home", icon=":material/home:")
    st.page_link("pages/education.py", label = "Education", icon=":material/school:")
    st.page_link("pages/projects.py", label = "Projects", icon=":material/workspaces:")
    st.page_link("pages/resume.py", label = "Resume", icon=":material/description:")
    st.page_link("pages/contact me.py", label = "Contact me", icon=":material/contact_page:")

r1c1,r1c2 = st.columns(2)
with r1c1:
    st.write(""" 
        <div style="" ></div>
        <div style="margin-left:30px" >
            <div style="font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">
                <p style="font-size: 32px; font-weight: 600; "> Undergraduate Degree </p>
                <p style="font-size: 28px; font-weight: 600; color: #6096fa; margin-top: -10px"> B.E Computer Science and Engineering </p>
                <p style="font-size: 15px; font-weight: 500;  color: #cfcfcf;" > Knowledge Institute Of Technology </p>
                <p style="font-size:20px; font-weight: 100; letter-spacing:1px; text-align: justify; color: #cfcfcf;"> 2021 - 2025</p>
                <p style="font-size:20px; font-weight: 100; letter-spacing:1px; text-align: justify; color: #cfcfcf;"> CGPA : 7.89/10 ( upto: 5th semester )  </p>
            </div>
            <div style="font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">
                <p style="font-size: 32px; font-weight: 600; "> Higher Secondary School </p>
                <p style="font-size: 28px; font-weight: 600; color: #6096fa; margin-top: -10px"> HSclearC </p>
                <p style="font-size: 15px; font-weight: 500;  color: #cfcfcf;" > Bharathi Vidyalaya  Higher Secodary School </p>
                <p style="font-size:20px; font-weight: 100; letter-spacing:1px; text-align: justify; color: #cfcfcf;"> 2020 - 2021</p>
                <p style="font-size:20px; font-weight: 100; letter-spacing:1px; text-align: justify; color: #cfcfcf;"> Percentage : 80 % </p>
            </div>
            <div style="font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">
                <p style="font-size: 32px; font-weight: 600; "> Secondary School </p>
                <p style="font-size: 28px; font-weight: 600; color: #6096fa; margin-top: -10px"> SSLC </p>
                <p style="font-size: 15px; font-weight: 500;  color: #cfcfcf;" > Bala Bharathi Matriculation Higher Secodary School </p>
                <p style="font-size:20px; font-weight: 100; letter-spacing:1px; text-align: justify; color: #cfcfcf;"> 2018 - 2019</p>
                <p style="font-size:20px; font-weight: 100; letter-spacing:1px; text-align: justify; color: #cfcfcf;"> Percentage : 72.3 % </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with r1c2:
    education_lottie = load_lottie_file('assets/education.json')
    st_lottie(education_lottie, speed=1, width=500, height=750, key="education")
