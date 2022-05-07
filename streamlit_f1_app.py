# %%
import streamlit as st
from utils import *

# MAPS
SEASON_RACE_DICT={
    2022: ['Miami', 'Imola', 'Australia', 'Saudi Arabia', 'Bahrain']
}

SESSIONS = {
    'R': 'Race',
    'Q': 'Qualifying',
    'S': 'Sprint',
    'SQ': 'Sprint Qualifying',
    'FP1': 'Practice 1',
    'FP2': 'Practice 2',
    'FP3': 'Practice 3'
}

DRIVERS = ['HAM', 'RUS',
            'SAI','LEC',
            'VER', 'PER',
            'RIC', 'NOR',
            'VET', 'STR',
            'ALO', 'OCO', 
            'TSU', 'GAS',
            'MSC', 'MAG',
            'BOT', 'ZHO', 
            'LAT', 'ALB']

DRIVERS_DETAILS = {
            'HAM':[44, 'Hamilton', 'Mercedes'], 'RUS': [63, 'Russel', 'Mercedes'],
            'SAI':[55, 'Sainz', 'Ferrari'], 'LEC': [16, 'Leclerc', 'Ferrari'],
            'VER': [33, 'Verstappen', 'Red Bull'], 'PER': [11, 'Perez', 'Red Bull'],
            'RIC': [3, 'Ricciardo', 'McLaren'], 'NOR': [4, 'Norris', 'McLaren'],
            'VET': [5, 'Vettel', 'Aston Martin'], 'STR': [18, 'Stroll', 'Aston Martin'],
            'ALO': [14, 'Alonso', 'Alpine'], 'OCO': [31, 'Ocon', 'Alpine'],
            'TSU': [22, 'Tsunoda', 'AlphaTauri'], 'GAS': [10, 'Gasly', 'AlphaTauri'],
            'MSC': [47, 'Schumacher', 'Haas F1 Team'], 'MAG': [10, 'Magnussen', 'Haas F1 Team'],
            'BOT': [77, 'Bottas', 'Alfa Romeo'], 'ZHO': [24, 'Zhou', 'Alfa Romeo'],
            'LAT': [6, 'Latifi', 'Williams'], 'ALB': [53, 'Albon', 'Williams']
            }

# %%
# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")

# Streamlit App Layout

# Sidebar
with st.sidebar:
    st.header('Inputs')
    year = st.selectbox(label='Year:', options=SEASON_RACE_DICT.keys(), index=0)
    grand_prix = st.selectbox(label='Grand Prix', options=SEASON_RACE_DICT[year], index=0)
    session = st.selectbox(label='Session', options=SESSIONS.values(), index=0)
    driver_1 = st.selectbox(label='Driver 1', options=DRIVERS, index=0)
    driver_2 = st.selectbox(label='Driver 2', options=DRIVERS, index=1)
    # lap_number = st.selectbox(label='Session', options=SESSIONS.values(), index=0)

# Main Body
st.title('F1 INTERACTIVE')
st.plotly_chart(plot_race_summary(year, grand_prix, session, driver_1, driver_2), use_container_width=True)
laps_driver_1 = load_laps_for_driver(year, grand_prix, session, driver_1)
laps_driver_2 = load_laps_for_driver(year, grand_prix, session, driver_2)
MAX_LAPS = int(min(laps_driver_1.LapNumber.max(), laps_driver_2.LapNumber.max()))
if MAX_LAPS==0:
    st.warning('No laps to compare!')
else:
    lap_number = st.slider(label='Lap Number', min_value=1, max_value=MAX_LAPS, value=1, step=1)
    st.plotly_chart(plot_driver_comparison_for_lap_number(year, grand_prix, session, driver_1, driver_2, lap_number), use_container_width=True)
