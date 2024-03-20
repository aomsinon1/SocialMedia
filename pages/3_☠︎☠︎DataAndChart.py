import streamlit as st
import pandas as pd
import altair as alt

st.header("Show Data Index Price")

df = pd.read_csv("./data/dummy_data.csv")
st.write(df.head(10))

st.header("Show Chart")

# Filtered data based on age_range
age_range = st.slider("Select age range", min_value=df["age"].min(), max_value=df["age"].max(), value=(df["age"].min(), df["age"].max()))
filtered_df = df[(df["age"] >= age_range[0]) & (df["age"] <= age_range[1])]

# Create chart
chart = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X('age', title='Age'),
    y=alt.Y('count()', title='Count'),  # Using count() to count the number of data points in each age group
    color='platform:N',
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

# นับจำนวนข้อมูลในแต่ละแพลตฟอร์ม
platform_count = filtered_df['platform'].value_counts().reset_index()
platform_count.columns = ['male', 'platform']

# สร้าง Pie Chart
pie_chart = alt.Chart(platform_count).mark_arc().encode(
    color='platform:N',
    tooltip=['male', 'platform']
).properties(
    width=600,
    height=400,
    title='Platform Distribution by Male'
)

st.altair_chart(pie_chart, use_container_width=True)




