import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error

st.title("Index Price Prediction")
st.header("Index Price Prediction from NPRU")

df=pd.read_csv('./data/2022worldcup.csv')
st.write(df.head(10))

#st.line_chart(df)
#st.line_chart(df, x="interest_rate", y="unemployment_rate", color="stock_index_price")
st.line_chart(
   df, x="interest_rate", y=["unemployment_rate", "stock_index_price"], color=["#FF0000", "#0000FF"]  # Optional
)

x=df[['interest_rate','unemployment_rate']]
y=df['stock_index_price']
pf=PolynomialFeatures(degree=3)
x_poly=pf.fit_transform(x)

x_train,x_test,y_train,y_test =train_test_split(x_poly,y,random_state=0)

modelRegress=LinearRegression()
modelRegress.fit(x_train,y_train)
x1=st.number_input("กรุณาป้อนข้อมูล interest_rate:")
x2=st.number_input("กรุณาป้อนข้อมูล unemployment_rate:")

if st.button("พยากรณ์ข้อมูล"):
    x_input=[[x1,x2]]
    y_predict=modelRegress.predict(pf.fit_transform(x_input))
    st.write(y_predict)
    st.button("ไม่พยากรณ์ข้อมูล")
else:
    st.button("ไม่พยากรณ์ข้อมูล")