import streamlit as st
import pandas as pd

st.title("💘💘Websit Developing using python💘💘")
st.header("💣💣Websit Developing using python💣💣")

st.image('./img/myphoto.jpg')
st.subheader("Nattwut Limchai")

dt=pd.read_csv('./data/iris.csv')
st.header("ข้อมูลดอกไม้")
st.write(dt.head(10))