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
    x='platform',
    y='age',
    tooltip=['platform', 'age']
).properties(
    width=600,
    height=400,
    title='Age Distribution by Platform'
)

st.altair_chart(chart, use_container_width=True)








