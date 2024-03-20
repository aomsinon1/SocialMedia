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

lottie_url_hello = "https://lottie.host/04a73bbb-ad0e-4cf6-8200-7aae7ccc332f/oOspXtZYfI.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello, key="hello")

st.header("ทฤษฎีที่เกี่ยวข้อง")

st.subheader("1.ทฤษฎีเหมืองข้อมูล")
st.info("""
xxxxxxxxxx
""")

st.subheader("2.เทคนิคการการทำจินตทัศน์ข้อมูล")
st.info("""
xxxxxxxxxx
""")