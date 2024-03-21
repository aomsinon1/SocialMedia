import json
import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner



# ถ้ามีการอัปโหลดไฟล์ GIF
if uploaded_file is not None:
    # แสดงรูปภาพ GIF
    st.image(uploaded_file, caption='https://media1.tenor.com/m/_3FJpcm3xgwAAAAd/fun-pet-pet-fun.gif', use_column_width=True)


#การเรียกใช้งาาน lottie file
st_lottie(lottie_hello, key="hello")
st.balloons()

