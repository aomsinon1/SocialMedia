import streamlit as st
import pandas as pd

st.header("Show Data Index Price")

df=pd.read_csv("./data/dummy_data.csv")
st.write(df.head(10))

st.header("Show Chart")



st.header("Bar Chart")

# สร้างช่องสไลเดอร์สำหรับการเลือกช่วงอายุ
min_age = df["age"].min()
max_age = df["age"].max()
age_range = st.slider("Select age range", min_value=min_age, max_value=max_age, value=(min_age, max_age))

# กรองข้อมูลตามช่วงอายุที่ผู้ใช้เลือก
filtered_df = df[(df["age"] >= age_range[0]) & (df["age"] <= age_range[1])]

# สร้างกราฟแท่งโดยให้แกน x เป็นช่วงอายุและแกน y เป็นจำนวนของบุคคลในแต่ละช่วงอายุ
age_counts = filtered_df.groupby(pd.cut(filtered_df["age"], bins=range(age_range[0], age_range[1]+1, 10))).size()
st.bar_chart(age_counts)