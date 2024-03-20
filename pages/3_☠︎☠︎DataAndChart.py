import streamlit as st
import pandas as pd

st.header("Show Data Index Price")

df=pd.read_csv("./data/dummy_data.csv")
st.write(df.head(10))

st.header("Show Chart")



age_range = st.slider("Select age range", min_value=df["age"].min(), max_value=df["age"].max(), value=(df["age"].min(), df["age"].max()))
filtered_df = df[(df["age"] >= age_range[0]) & (df["age"] <= age_range[1])]

# สร้างกราฟแท่ง
st.bar_chart(filtered_df.set_index('platform')['age'])


st.header("Bar Chart")

# สร้างช่องสไลเดอร์สำหรับการเลือกช่วงอายุ
min_age = df["age"].min()
max_age = df["age"].max()
age_range = st.slider("Select age range", min_value=min_age, max_value=max_age)

# ตรวจสอบว่าค่าที่ได้จากช่องสไลเดอร์เป็นตัวเลขที่สามารถแปลงเป็น int ได้
if isinstance(age_range[0], (int, float)) and isinstance(age_range[1], (int, float)):
    # แปลงค่าที่ได้จากช่องสไลเดอร์เป็น int
    age_range = (int(age_range[0]), int(age_range[1]))
else:
    # หากไม่เป็นตัวเลขที่สามารถแปลงเป็น int ได้ให้ใช้ค่าเริ่มต้นของช่วงอายุ
    age_range = (min_age, max_age)

# กรองข้อมูลตามช่วงอายุที่ผู้ใช้เลือก
filtered_df = df[(df["age"] >= age_range[0]) & (df["age"] <= age_range[1])]

# แบ่งข้อมูลตามช่วงอายุและนับจำนวนบุคคลในแต่ละช่วงอายุ
age_groups = pd.cut(filtered_df["age"], bins=range(age_range[0], age_range[1]+1, 10))
age_counts = age_groups.value_counts().sort_index()

# สร้างกราฟแท่งโดยให้แกน x เป็นช่วงอายุและแกน y เป็นจำนวนของบุคคลในแต่ละช่วงอายุ
st.bar_chart(age_counts)



