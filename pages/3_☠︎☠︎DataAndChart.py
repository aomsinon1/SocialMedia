import streamlit as st
import pandas as pd

st.header("Show Data Index Price")

df=pd.read_csv("./data/dummy_data.csv")
st.write(df.head(10))

st.header("Show Chart")

import altair as alt

# สร้างกราฟแท่ง
chart = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X('age', title='Age'),
    y=alt.Y('count()', title='Count'),  # ใช้ count() เพื่อนับจำนวนข้อมูลที่มีในแต่ละช่วงอายุ
    color='platform:N',
    tooltip=['platform', 'age']  # แก้ไขเป็นชื่อฟิลด์ที่ต้องการแสดงใน tooltip
).properties(
    width=600,
    height=400,
    title='Age Distribution by Platform'
).configure_title(
    fontSize=20,
    fontWeight='bold',
    color='gray'
).configure_axis(
    labelFontSize=12,
    titleFontSize=16,
    titleFontWeight='normal'
)

st.altair_chart(chart, use_container_width=True)







