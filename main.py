import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf




st.title('Начало странички')
#st.write('Для загрузки котировок компаний напишите её тикер')

text = st.text_input('Для загрузки котировок компаний напишите её тикер')



if text is not None and text!='':
    data = yf.Ticker(text)
    df = data.history( start='2010-5-31', end='2026-5-3')
    if len(df)>0:   
        st.write(df.head(5))
        st.line_chart(df[['Open', 'Close']],
                color=["#FF0000", "#0000FF"]
                )
        fig, ax = plt.subplots()
        ax.plot(df.index, df['Volume'])
        
        st.pyplot(fig = fig )
    else:
        st.write('Тикер не найден')    

