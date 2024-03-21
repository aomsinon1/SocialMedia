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

chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('platform:N', title='Platform'),
    y=alt.Y('time_spent', title='Time Spent'),  
    color='platform:N',
    tooltip=['platform', 'time_spent']
).properties(
    width=600,
    height=400,
    title='Time Spent Distribution by Platform'
)

st.altair_chart(chart, use_container_width=True)

max_age_by_platform = df.groupby('platform')['age'].max().reset_index()

# Create bar chart using Altair
bar_chart = alt.Chart(max_age_by_platform).mark_bar().encode(
    x=alt.X('platform:N', title='Platform'),
    y=alt.Y('age:Q', title='Max Age'),
    color=alt.Color('platform:N', legend=None),
    tooltip=['platform', 'age']
).properties(
    width=600,
    height=400,
    title='Max Age by Platform'
)

st.altair_chart(bar_chart, use_container_width=True)

# Filter data by gender
# Filter data by gender and count the occurrences
gender_counts = df['gender'].value_counts()

# Display counts using subheaders
st.subheader('ชาย')
st.subheader(gender_counts.get('ชาย', 0))  # ใช้ .get() เพื่อรับค่าจำนวนของ 'ชาย' และกำหนดให้เป็น 0 ถ้าไม่พบค่านี้
st.subheader('หญิง')
st.subheader(gender_counts.get('หญิง', 0))  # ใช้ .get() เพื่อรับค่าจำนวนของ 'หญิง' และกำหนดให้เป็น 0 ถ้าไม่พบค่านี้


# Create a DataFrame for plotting
dtSex = [NumM[1], NumF[1]]
dtSexb = pd.DataFrame(dtSex, index=["ชาย", "หญิง"])

# Plot a bar chart using Streamlit
st.bar_chart(dtSexb)

import streamlit as st
import pandas as pd

# Assuming dt is your DataFrame containing data

# Filter data by 'Sex'
NumM = dt[dt['gender'] == 'ชาย'].count()
NumF = dt[dt['gender'] == 'หญิง'].count()

# Display counts using subheaders
st.subheader('ชาย')
st.subheader(NumM.iloc[0])
st.subheader('หญิง')
st.subheader(NumF.iloc[0])

# Create a DataFrame for plotting
dtSex = [NumM.iloc[0], NumF.iloc[0]]
dtSexb = pd.DataFrame(dtSex, index=["ชาย", "หญิง"])

# Plot a bar chart using Streamlit
st.bar_chart(dtSexb)


