import json
import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://tenor.com/th/view/amad-diallo-traore-amad-diallo-traore-gif-20723512"
lottie_hello = load_lottieurl(lottie_url_hello)

st.header("การพยากรณ์ข้อมูลการใช้platformด้วยเทคนิค Linear Regression☠︎")
st.header("by Aomsin")

#การเรียกใช้งาาน lottie file
st_lottie(lottie_hello, key="hello")
st.balloons()