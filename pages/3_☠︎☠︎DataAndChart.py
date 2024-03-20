import streamlit as st
import pandas as pd

st.header("Show Data Index Price")

df=pd.read_csv("./data/dummy_data.csv")
st.write(df.head(10))

st.header("Show Chart")



age_range = st.slider("Select age range", min_value=df["age"].min(), max_value=df["age"].max(), value=(df["age"].min(), df["age"].max()))
filtered_df = df[(df["age"] >= age_range[0]) & (df["age"] <= age_range[1])]

st.bar_chart(filtered_df.set_index('platform')['age'])


import altair as alt

# สร้างกราฟแท่งโดยกำหนดแกน y เป็นอายุ
chart = alt.Chart(filtered_df).mark_bar(color='#3182bd').encode(
    x=alt.X('platform', title='Platform', axis=alt.Axis(labelAngle=-45)),
    y=alt.Y('age', title='Age'),
    tooltip=['platform', 'age']
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


import altair as alt

# สร้างกราฟวงกลม
chart = alt.Chart(filtered_df).mark_circle(size=500).encode(
    x=alt.X('age', title='Age'),
    y=alt.Y('time_spent', title='Time Spent'),
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







