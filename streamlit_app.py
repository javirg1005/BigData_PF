import streamlit as st
import pandas as pd
import numpy as np
import requests


DATA_URL = ('http://2477-83-57-44-98.ngrok.io') #Esto cambia 


def recoger(url):
    response = requests.get(url)
    return response.json()
    

@st.cache
def load_data_teamvalue():
    datos = recoger((DATA_URL +'/api/v1/teamvalue'))
    data = pd.DataFrame(datos)
    data = data.iloc[:, ::-1]
    return data

@st.cache
def load_data_playervalue():
    datos = recoger((DATA_URL +'/api/v1/playervalue'))
    data = pd.DataFrame(datos)
    data = data.iloc[:, ::-1]
    return data

@st.cache
def load_data_playercards():
    datos = recoger((DATA_URL +'/api/v1/playercards'))
    data = pd.DataFrame(datos)
    data = data.iloc[:, ::-1]
    return data       

@st.cache
def load_data_countrycups():
    datos = recoger((DATA_URL +'/api/v1/countrycups'))
    data = pd.DataFrame(datos)
    data = data.iloc[:, ::-1]
    return data

@st.cache
def load_data_countryplayes():
    datos = recoger((DATA_URL +'/api/v1/countryplayes'))
    data = pd.DataFrame(datos)
    data = data.iloc[:, ::-1]
    return data

@st.cache
def load_data_goalsteams():
    datos = recoger((DATA_URL +'/api/v1/goalsteams'))
    data = pd.DataFrame(datos)
    data = data.iloc[:, ::-1]
    return data

@st.cache
def load_data_goalsplayer():
    datos = recoger((DATA_URL +'/api/v1/goalsplayer'))
    data = pd.DataFrame(datos)
    data = data.iloc[:, ::-1]
    return data

@st.cache
def load_data_mvpais():
    datos = recoger((DATA_URL +'/api/v1/mvpais'))
    data = pd.DataFrame(datos)
    data = data.iloc[:, ::-1]
    return data

st.subheader('Valor de mercado por equipos (millones de €)')
data_teammarketvalue = load_data_teamvalue()
st.vega_lite_chart(data_teammarketvalue, {
    'mark': {'type': 'bar', 'tooltip': True},
    'height': 500,
    'width': 700,
    'encoding': {
        'x': {'field': 'Equipos', 'sort': '-y'},
        'y': {'field': 'Valor de mercado (millones €)', 'type': 'quantitative'},
        'color': {'field': 'Valor de mercado (millones €)', 'scale': {
            'scheme': 'spectral'
        }}
    },
    'config': {
        'legend': {
            'disable': True
        }
    }
})