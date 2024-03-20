import streamlit as st
import pandas as pd

st.header("Show Data Index Price")

df=pd.read_csv("./data/dummy_data.csv")
st.write(df.head(10))

st.header("Show Chart")

st.line_chart(
   df, x="platform", y=["age"], color=["#FF0000"]  )

age_range = st.slider("Select age range", min_value=df["1"].min(), max_value=df["99"].max(), value=(df["age"].min(), df["age"].max()))
filtered_df = df[(df["age"] >= age_range[0]) & (df["age"] <= age_range[1])]

# สร้างกราฟแท่ง
st.bar_chart(filtered_df.set_index('platform')['age'])