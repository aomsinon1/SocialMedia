import streamlit as st
import pandas as pd

st.header("Show Data Index Price")

df=pd.read_csv("./data/dummy_data.csv")
st.write(df.head(10))

st.header("Show Chart")

st.line_chart(
   df, x="age", y=["'goals_overall", "unemployment_rate"], color=["#FF0000", "#0000FF"]  # Optional
)