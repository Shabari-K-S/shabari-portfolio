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

r0c1, r0c2 = st.columns([4, 2])

with r0c1:
    st.write("<div style='margin-top:130px;'></div>", unsafe_allow_html=True)
    st.write("""
    <div style="margin-left:70px">
        <p style="font-size:40px; font-weight: 600; letter-spacing:3px"> Hey There!, Welcome 👋 </p>
        <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=35&weight=500&pause=1000&random=false&width=600&lines=Hi+I'm+Shabari+K+S" alt="Typing SVG" style="height:180px;margin-top:-35px;width:100%" />
        <p style="font-size:20px; font-weight: 100; letter-spacing:1px; text-align: justify; color: #bfbfbf;width:85%; font-family: Courier New"> 
            I am currently pursuing a degree in Computer Science Engineering, with a strong passion for Ethical Hacking and Web Development. I am continually working to expand my knowledge and skills in these fields.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
with r0c2:
    st.write("<div style='margin-top:80px;'></div>", unsafe_allow_html=True)
    img = Image.open('assets/me.jpeg')

    # Convert the image to bytes
    byte_arr = io.BytesIO()
    img.save(byte_arr, format='JPEG')
    byte_arr = byte_arr.getvalue()

    # Encode the bytes to base64
    b64_string = base64.b64encode(byte_arr).decode()
    st.write(f"""
    <div style='border-radius: 50%; overflow: hidden; box-shadow: 0px 0px 40px 0px #6096fa;'>
        <img src='data:image/png;base64,{b64_string}' style='width: 100%; height: auto;'>
    </div>
    """, unsafe_allow_html=True)


