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
NumM = df[df['gender'] == 'ชาย'].count()
NumF = df[df['gender'] == 'หญิง'].count()

# Display counts using subheaders
st.subheader('ชาย')
st.subheader(NumM[1])
st.subheader('หญิง')
st.subheader(NumF[1])

# Create a DataFrame for plotting
dtSex = [NumM[1], NumF[1]]
dtSexb = pd.DataFrame(dtSex, index=["ชาย", "หญิง"])

# Plot a bar chart using Streamlit
st.bar_chart(dtSexb)

# Plot a pie chart using Streamlit
st.subheader("Pie Chart")
st.write(dtSexb.plot.pie(y=0, autopct='%1.1f%%'))

#กราฟวงกลม

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header("Show Data Index Price")

df = pd.read_csv("./data/dummy_data.csv")
st.write(df.head(10))

st.header("Show Chart")

# Filtered data based on age_range
age_range = st.slider("Select age range", min_value=df["age"].min(), max_value=df["age"].max(), value=(df["age"].min(), df["age"].max()))
filtered_df = df[(df["age"] >= age_range[0]) & (df["age"] <= age_range[1])]

# Create chart using Altair (example provided in the previous response)

# Plot a bar chart using Streamlit and Altair (example provided in the previous response)

# Plot a pie chart using Matplotlib
st.subheader("Pie Chart")
fig, ax = plt.subplots()
ax.pie(dtSexb[0], labels=dtSexb.index, autopct='%1.1f%%')
st.pyplot(fig)