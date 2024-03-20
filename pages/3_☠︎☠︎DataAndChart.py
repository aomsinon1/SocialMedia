import streamlit as st
import pandas as pd

st.header("Show Data Index Price")

df = pd.read_csv("./data/dummy_data.csv")
st.write(df.head(10))

st.header("Show Chart")

# Define data_for_interest, colors, and interest
data_for_interest = df  # ให้ data_for_interest เป็น DataFrame ที่ต้องการแสดงในกราฟ
colors = ['#FF0000', '#00FF00', '#0000FF']  # กำหนดสีของเส้นกราฟ
interest = "interest_1"  # กำหนดชื่อสำหรับกราฟ

# Plot line chart
st.line_chart(
   data_for_interest, x="platform", y="age", color=colors[0], use_container_width=True, key=interest)
