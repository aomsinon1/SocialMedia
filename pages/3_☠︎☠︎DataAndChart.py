import streamlit as st
import pandas as pd

st.header("Show Data Index Price")

df=pd.read_csv("./data/dummy_data.csv")
st.write(df.head(10))

st.header("Show Chart")

 st.line_chart(data_for_interest, x="platform", y="age", color="#FF0000", use_container_width=True, key=interest)
