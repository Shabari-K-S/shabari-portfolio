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

st.html(
"""
<style>
@import url('https://fonts.googleapis.com/css?family=Lato:300,400,700');
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css");
*{
  margin: 0;
  padding: 0;
}
i {
    width: 100%;
    height: 100%;
    color: #5aadfa;
}
.wrap{
  height: 650px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Lato', sans-serif;
}
.icon{
  height: 100px;
  width: 100px;
  background-color: #5aadfa;
  -webkit-border-radius: 50%;
  -moz-border-radius: 50%;
  -webkit-transition: border-radius .5s, transform .5s, height .5s, width .5s, background-color .2s;
  -moz-transition: border-radius .5s, transform .5s, height .5s, width .5s, background-color .2s;
  display: flex;
  align-items: center;
  justify-content: center;
  
  .first{
    color: white;
    font-weight: 700;
    font-size: 17px;
    text-align: center;
  }
  .second{
    display: none;
    width: 100%;
    height: 100%;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    grid-template-areas: 
      "square1 square2"
      "square3 square4";
    div{
      display: flex;
      align-items: center;
      justify-content: center;
      transform: rotate(180deg); 
      a{
        color: black;
        text-decoration: none;
      }
    }
    .square-1{
      grid-area: square1;
    }
    .square-2{
      grid-area: square2;
    }
    .square-3{
      grid-area: square3;
    }
    .square-4{
      grid-area: square4;
    }
  }
  
  &:hover{
    height: 200px;
    width: 200px;
    border-radius: 0;
    transform: rotate(180deg);
    background-color: white;
    border: 5px solid #5aadfa;
    
    //cursor: pointer;
    
    .first{
      display: none;
    }
    .second{
      display: grid;
    }
  }
}
.signature{
  position: absolute;
  bottom: 0;
  right: 0;
  padding: 5px;
}
</style>
<script>
//This is just for the icon svgs
feather.replace({
    'height': 50,
    'width': 50,
    'stroke-width': 1
});
</script>
<div class="wrap">
  <div class="icon">
    <div class="first">Let's<br>Connect!</div>
    <div class="second">
      <div class="square-1"><a href="http://www.linkedin.com/in/shabari-k-s" target="_blank"><h1><i class="bi bi-linkedin"></i></h1></a></div>
      <div class="square-2"><a href="https://www.instagram.com/_.sourcecode._/" target="_blank"><h1><i class="bi bi-instagram"></i></h1></a></div>
      <div class="square-3"><a href="https://app.hackthebox.com/profile/1104708" target="_blank"><h1><i class="bi bi-box"></i></h1></a></div>
      <div class="square-4"><a href="https://github.com/Shabari-K-S" target="_blank"><h1><i class="bi bi-github"></i></h1></a></div>
    </div>
  </div>
</div>
"""
)
