# %%
import streamlit as st
from utils import *

# MAPS
SEASON_RACE_DICT={
    2022: ['Imola', 'Australia', 'Saudi Arabia', 'Bahrain']
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

DRIVERS_DETAILS = [[44, 'HAM', 'Mercedes'], [63, 'RUS', 'Mercedes'],
            [55, 'SAI', 'Ferrari'], [16, 'LEC', 'Ferrari'],
            [33, 'VER', 'Red Bull'], [11, 'PER', 'Red Bull'],
            [3, 'RIC', 'McLaren'], [4, 'NOR', 'McLaren'],
            [5, 'VET', 'Aston Martin'], [18, 'STR', 'Aston Martin'],
            [14, 'ALO', 'Alpine'], [31, 'OCO', 'Alpine'],
            [22, 'TSU', 'AlphaTauri'], [10, 'GAS', 'AlphaTauri'],
            [47, 'MSC', 'Haas F1 Team'], [10, 'MAG', 'Haas F1 Team'],
            [77, 'BOT', 'Alfa Romeo'], [24, 'ZHO', 'Alfa Romeo'],
            [6, 'LAT', 'Williams'], [53, 'ALB', 'Williams']]

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
MAX_LAPS = int(load_data(year, grand_prix, session).laps.LapNumber.max())
lap_number = st.slider(label='Lap Number', min_value=1, max_value=MAX_LAPS, value=1, step=1)
st.plotly_chart(plot_driver_comparison_for_lap_number(year, grand_prix, session, driver_1, driver_2, lap_number), use_container_width=True)
