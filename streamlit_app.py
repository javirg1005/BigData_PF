import streamlit as st
import pandas as pd
import numpy as np
import requests
from PIL import Image


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
raimon = Image.open('Raimon.png')
royal = Image.open('Royal.png')
col1, col2, col3 = st.columns([3, 6, 1])
with col1:
    st.image(raimon)
with col2:
    st.title('Estadísticas relevantes en el mundo del fútbol')
with col3:
    st.image(royal)

colTeamMarketValue, colPlayerMarketValue = st.columns(2)

with colTeamMarketValue:
    st.subheader('Valor de mercado por equipos (millones de €)')
    st.text('Muestra el valor de mercado de mayor a menor en los primeros 20 equipos.')
    data_teammarketvalue = load_data_teamvalue()
    st.vega_lite_chart(data_teammarketvalue, {
        'mark': {'type': 'bar', 'tooltip': True},
        'height': 600,
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
        'height': 600,
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

st.subheader('Valor de mercado por país (millones de €)')
st.text('Muestra el valor de mercado ordenado de mayor a menor en los países.')
data_mvpaises = load_data_mvpais()
st.vega_lite_chart(data_mvpaises, {
    'mark': {'type': 'bar', 'tooltip': True},
    'height': 850,
    'width': 1200,
    'encoding': {
        'x': {'field': 'País', 'sort': '-y'},
        'y': {'field': 'Valor de mercado (millones €)', 'type': 'quantitative'},
        'color': {
            'field': 'Valor de mercado (millones €)', 
            'scale': {'scheme': 'rainbow', 'reverse': True}
        }
    },
    'config': {
        'legend': {
            'disable': True
        }
    }
})

colCountryCups, colCountryPlayers = st.columns(2)

with colCountryCups:
    st.subheader('Ligas en países')
    st.text('Muestra el número de ligas de cada país.')
    data_countrycups = load_data_countrycups()
    st.vega_lite_chart(data_countrycups, {
        'mark': {'type': 'bar', 'tooltip': True},
        'height': 600,
        'width': 700,
        'encoding': {
            'x': {'field': 'País', 'sort': '-y'},
            'y': {'field': 'Nº de ligas', 'type': 'quantitative'},
            'color': {
                'field': 'País', 
                'scale': {'scheme': 'pastel2'}
            }
        },
        'config': {
            'legend': {
                'disable': True
            }
        }
    })

with colCountryPlayers:
    st.subheader('Jugadores de países')
    st.text('Muestra el número de jugadores originarios de cada país.')
    data_countryplayers = load_data_countryplayes()
    st.vega_lite_chart(data_countryplayers, {
        'mark': {'type': 'bar', 'tooltip': True},
        'height': 600,
        'width': 700,
        'encoding': {
            'x': {'field': 'País', 'sort': '-y'},
            'y': {'field': 'Nº de jugadores', 'type': 'quantitative'},
            'color': {
                'field': 'Nº de jugadores', 
                'scale': {'scheme': 'set3'}
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
    'height': 800,
    'width': 1200,
    'encoding': {
        'x': {
            'field': 'Jugador',
            'type': 'nominal',
            'sort': '-layer'
        }
    },
    'layer': [
        {
            'mark': {'type': 'bar', 'tooltip': True, 'xOffset': -10, 'size': 20, 'color': '#FB683F'},
            'encoding': {
                'y': {
                    'field': 'Tarjetas Rojas',
                    'type': 'quantitative'
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

colGolTeams, colGolPlayer = st.columns(2)

with colGolTeams:
    st.subheader('Goles por equipos')
    st.text('Muestra el número de goles de los 20 equipos con más goles.')
    data_golteams = load_data_goalsteams()
    st.vega_lite_chart(data_golteams, {
        'mark': {'type': 'bar', 'tooltip': True},
        'height': 600,
        'width': 700,
        'encoding': {
            'x': {'field': 'Equipos', 'sort': '-y'},
            'y': {'field': 'Goles totales', 'type': 'quantitative'},
            'color': {
                'field': 'Goles totales', 
                'scale': {'scheme': 'pinkyellowgreen'}
            }
        },
        'config': {
            'legend': {
                'disable': True
            }
        }
    })

with colGolPlayer:
    st.subheader('Goles por jugadores')
    st.text('Muestra el número de goles de los 20 jugadores con más goles.')
    data_golplayer = load_data_goalsplayer()
    st.vega_lite_chart(data_golplayer, {
        'mark': {'type': 'bar', 'tooltip': True},
        'height': 700,
        'width': 700,
        'encoding': {
            'x': {'field': 'Jugador', 'sort': '-y'},
            'y': {'field': 'Goles totales', 'type': 'quantitative'},
            'color': {
                'field': 'Goles totales', 
                'scale': {'scheme': 'brownbluegreen', 'reverse': True}
            }
        },
        'config': {
            'legend': {
                'disable': True
            }
        }
    })