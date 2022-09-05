#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#pip install openpyxl
import pandas as pd #pip install pandas
import plotly.express as px #pip install plotly-express
import streamlit as st #pip install streamlit

import datetime #pip install datetime

import pickle 
from pathlib import Path #pip install pathlib

import altair as alt #pip install altair
import plotly.graph_objects as go #pip install plotly
import streamlit_authenticator as stauth #pip install streamlit-authenticator

st.title("Portafolio Inversiones:moneybag:")

st.write("Acciones Globales e Indicadores Macroeconomicos:bar_chart:") #texto


st.markdown("##")

df = pd.read_excel('Portafolio Inversion.xlsx')

st.write(df)

st.subheader("Indicadores Macroeconomicos")

col1, col2 = st.columns(2)

TRM = df.loc[(df['Asset'] == 'USD/COP')]

fig1 = go.Figure(data=[go.Candlestick(x=TRM['Date'],
                open=TRM['Open'],
                high=TRM['High'],
                low=TRM['Low'],
                close=TRM['Close'])])

fig1.update_layout(xaxis_rangeslider_visible=False)

col1.write(fig1)

WTI = df.loc[(df['Asset'] == 'WTI')]

graph2 = px.bar(WTI, x = 'Date', y = 'Close', title = "WTI Oil Price")

col2.write(graph2)


st.subheader("Acciones Globales")

col3, col4 = st.columns(2)


apple = df.loc[(df['Asset'] == 'Apple')]

fig3 = px.line(apple, x='Date', y='Close', title='Apple Stock Price')

fig3.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

col3.write(fig3)

Amazon = df.loc[(df['Asset'] == 'AMAZON')]

graph4 = px.line(Amazon, x = 'Date', y = 'Close', title = "Amazon")

col4.write(graph4)


col5, col6 = st.columns(2)


City = df.loc[(df['Asset'] == 'Citygroup')]

graph5 = px.line(apple, x = 'Date', y = 'Close', title = "City Group")

col5.write(graph5)

BOA = df.loc[(df['Asset'] == 'Bank of America')]

graph6 = px.line(Amazon, x = 'Date', y = 'Close', title = "Bank of America")

col6.write(graph6)


























                     
                     