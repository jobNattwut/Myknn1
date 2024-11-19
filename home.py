import streamlit as st
import pandas as pd

st.title("💘💘Websit Developing using python💘💘")
st.header("💣💣Websit Developing using python💣💣")

st.image('./img/myphoto.jpg')
st.subheader("Nattwut Limchai")

dt=pd.read_csv('./data/iris-3.csv')
st.header()
st.write(dt.head(10))