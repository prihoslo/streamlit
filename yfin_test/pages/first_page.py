import streamlit as st
import pandas as pd

st.header('Можете загрузить сюда любой датафрейм')

uploaded_file = st.file_uploader("выберете файл")
if uploaded_file is not None:
    st.write('спасибо, сделать с ним ничего нельзя')