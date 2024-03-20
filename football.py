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

lottie_url_hello = "https://lottie.host/84e2487d-bcce-48b3-a30d-4e700ff9869b/fBWUkubaDT.json"
lottie_hello = load_lottieurl(lottie_url_hello)

st.header("การพยากรณ์ข้อมูล....ด้วยเทคนิค Linear Regression☠︎")
st.header("by Aomsin")

#การเรียกใช้งาาน lottie file
st_lottie(lottie_hello, key="hello")
st.balloons()