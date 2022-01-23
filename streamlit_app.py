import streamlit as st
import pandas as pd
import numpy as np
import requests


DATA_URL = ('http://2bc5-83-57-44-98.ngrok.io') #Esto cambia 


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

colTeamMarketValue, colPlayerMarketValue = st.columns(2)

with colTeamMarketValue:
    st.subheader('Valor de mercado por equipos (millones de €)')
    st.text('Muestra el valor de mercado de mayor a menor en los primeros 20 equipos.')
    data_teammarketvalue = load_data_teamvalue()
    st.vega_lite_chart(data_teammarketvalue, {
        'mark': {'type': 'bar', 'tooltip': True},
        'height': 500,
        'width': 700,
        'encoding': {
            'x': {'field': 'Equipos', 'sort': '-y'},
            'y': {'field': 'Valor de mercado (millones €)', 'type': 'quantitative'},
            'color': {
                'field': 'Valor de mercado (millones €)', 
                'scale': {'scheme': 'spectral', 'reverse': True}
            }
        },
        'config': {
            'legend': {
                'disable': True
            }
        }
    })

with colPlayerMarketValue:
    st.subheader('Valor de mercado por jugadores (millones de €)')
    st.text('Muestra el valor de mercado de mayor a menor en los primeros 20 jugadores.')
    data_playermarketvalue = load_data_playervalue()
    st.vega_lite_chart(data_playermarketvalue, {
        'mark': {'type': 'bar', 'tooltip': True},
        'height': 500,
        'width': 700,
        'encoding': {
            'x': {'field': 'Jugadores', 'sort': '-y'},
            'y': {'field': 'Valor de mercado (millones €)', 'type': 'quantitative'},
            'color': {
                'field': 'Valor de mercado (millones €)', 
                'scale': {'scheme': 'spectral', 'reverse': True}
            }
        },
        'config': {
            'legend': {
                'disable': True
            }
        }
    })

st.subheader('Jugadores con más tarjetas rojas')
st.text('Muestra los 20 jugadores con más tarjetas rojas, además de mostrar el número de amarillas también.')
data_playercards = load_data_playercards()
st.vega_lite_chart(data_playercards, {
    'height': 700,
    'width': 1000,
    'encoding': {
        'x': {
            'field': 'Jugador',
            'type': 'nominal'
        }
    },
    'layer': [
        {
            'mark': {'type': 'bar', 'tooltip': True, 'xOffset': -10, 'size': 20, 'color': '#FB683F'},
            'encoding': {
                'y': {
                    'field': 'Tarjetas Rojas',
                    'type': 'quantitative',
                    'sort': '-y'
                }
            }
        },
        {
            'mark': {'type': 'bar', 'tooltip': True, 'xOffset': 10, 'size': 20, 'color': '#FCF951'},
            'encoding': {
                'y': {
                    'field': 'Tarjetas Amarillas',
                    'type': 'quantitative'
                }
            }
        }
    ],
    'resolve': {'scale': {'y': 'independent'}},
    'config': {
        'legend': {
            'disable': True
        }
    }
})