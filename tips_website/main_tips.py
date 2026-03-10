import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



st.title('Начало странички')
st.header('На этом восхитительном сайте вы можете посмотреть и скачать инфорацию играфики по датасету tips.csv')


path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'

if 'tips' not in st.session_state:
    st.session_state.tips = pd.read_csv(path)
    st.session_state.tips['time_order'] = np.random.choice(
        pd.date_range('2023-01-01', '2023-01-31'),
        size=len(st.session_state.tips),
        replace=True
    )

# Кнопка для перезагрузки
if st.sidebar.button('Перезагрузить датафрейм с новым временем'):
    st.session_state.tips = pd.read_csv(path)
    st.session_state.tips['time_order'] = np.random.choice(
        pd.date_range('2023-01-01', '2023-01-31'),
        size=len(st.session_state.tips),
        replace=True
    )
tips = st.session_state.tips

if st.sidebar.button(label = 'посмотреть табличку'):
    st.write(tips)
    st.download_button(label = 'Скачать табличку',
                        data = tips.to_csv().encode('utf-8'),
                        file_name="raw_tips.csv" )
    

if st.sidebar.button(label = 'показать график чаевых от времени'):
    fig = plt.figure(figsize=(10,5))
    sns.lineplot(data=tips,
        x = 'time_order',
        y = 'tip',
        errorbar=('ci', 95),
        #estimator= 'median'
        )
    plt.xticks(rotation= 45)
    st.pyplot(fig)
if st.sidebar.button(label = 'показать распределение размера счета'):
    fig = plt.figure()
    sns.histplot(data=tips,
             x= 'total_bill',
             bins= 50
             )
    st.pyplot(fig)

if st.sidebar.button(label ='скатерплот размера счета и чаевых'):
    st.scatter_chart(tips, x='total_bill', y= 'tip', color ='sex')


if st.sidebar.button(label ='распределение чаевых по дням неедли'):  
    fig, ax = plt.subplots()
    sns.barplot(data=tips, x = 'day', y = 'total_bill')
    ax.set_title('распределение чаевых по дням неедли')
    ax.set_xlabel('день недели')
    ax.set_ylabel('сколько оставили')
    st.pyplot(fig)

if st.sidebar.button(label ='когда дают больше чаевых'):
    fig, ax = plt.subplots()
    sns.boxplot(data= tips, x = 'time', y = 'total_bill',hue = 'time')
    
    ax.set_title('распределение стоимости заказа по времени дня')
    ax.set_xlabel('вид приёма пищи')
    ax.set_ylabel('стоимость')
    st.pyplot(fig)

if st.sidebar.button(label ='распределение размера счёта по дням'):
    fig, ax = plt.subplots()
    sns.boxplot(data= tips, x = 'time_order', y = 'total_bill', hue = 'time')
    plt.xticks(rotation= 45, size =7)
   
    st.pyplot(fig)

if st.sidebar.button(label ='2 скатера'):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), sharex=True, sharey=True)

    sns.scatterplot(data=tips[tips['sex']=='Male'], x = 'tip', y = 'total_bill', hue = 'smoker', ax =ax1)
    sns.scatterplot(data=tips[tips['sex']=='Female'], x = 'tip', y = 'total_bill', hue = 'smoker', ax =ax2 )

    ax1.set_title('Мужчины')
    ax2.set_title('Женщины')
    st.pyplot(fig)    

if st.sidebar.button(label ='тепловая карта'):
    fig, ax = plt.subplots()
    sns.heatmap(tips.corr(numeric_only=True), annot=True)
    st.pyplot(fig)