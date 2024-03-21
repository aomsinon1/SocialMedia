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

lottie_url_hello = "https://lottie.host/e1e288b5-1a12-470f-9f29-45e1171dc7e8/Way5aKuCFU.json"
lottie_hello = load_lottieurl(lottie_url_hello)

st.header("การพยากรณ์ข้อมูลการใช้platformด้วยเทคนิค Linear Regression☠︎")
st.header("by A0MS1N")


#การเรียกใช้งาาน lottie file
st_lottie(lottie_hello, key="hello")
st.balloons()

