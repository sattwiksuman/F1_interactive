# %%
# Import dependencies
from statistics import mode
import fastf1 as ff1
from fastf1 import plotting
from fastf1 import utils

from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

import numpy as np
import pandas as pd
from requests import Session

import plotly.graph_objects as go

import streamlit as st


# Enable the cache by providing the name of the cache folder
ff1.Cache.enable_cache('cache') 


# Get data of lap for both drivers
def get_telemetry_for_lap_number(laps_driver, lap_number):
    return laps_driver.loc[laps_driver[laps_driver['LapNumber']==lap_number].index.to_list()[0]].get_telemetry().add_distance()


# Load data
@st.cache
def load_data(year, grand_prix, session):
    session_data = ff1.get_session(year, grand_prix, session)
    session_data.load()
    return session_data

# Plot Race summary = LapTime vs LapNumber
def plot_race_summary(year, grand_prix, session, driver_1, driver_2):
    '''
    INPUT:
    year: year of the season; data type = int
    grand_prix: name of the grand_prix; data type = str
    session: FP1, FP2, FP3, Q or R, always set to R by default; data type = str
    driver_1: 3 letter code of driver 1; data type = str
    driver_2: 3 letter code of driver 2; data type = str
    lap_number: lap number for lap to be compared; data type = int
    OUTPUT:
    This Function prints the chart LapTime against the LapNumber for both drivers from telemetry.
    Returns the Plotly Figure_Object.
    '''
    session_data = load_data(year, grand_prix, session)

    laps_driver_1 = session_data.laps.pick_driver(driver_1)
    laps_driver_2 = session_data.laps.pick_driver(driver_2)

# Plot driver data comparison
def plot_driver_comparison_for_lap_number(year, grand_prix, session, driver_1, driver_2, lap_number):
    '''
    INPUT:
    year: year of the season; data type = int
    grand_prix: name of the grand_prix; data type = str
    session: FP1, FP2, FP3, Q or R, always set to R by default; data type = str
    driver_1: 3 letter code of driver 1; data type = str
    driver_2: 3 letter code of driver 2; data type = str
    lap_number: lap number for lap to be compared; data type = int
    OUTPUT:
    This Function prints the chart comparing variation of speed of both drivers vs distance over one lap from telemetry data.
    Returns the Plotly Figure_Object.
    '''
    session_data = load_data(year, grand_prix, session)

    laps_driver_1 = session_data.laps.pick_driver(driver_1)
    laps_driver_2 = session_data.laps.pick_driver(driver_2)

    telemetry_driver_1 = get_telemetry_for_lap_number(laps_driver_1,lap_number)
    telemetry_driver_2 = get_telemetry_for_lap_number(laps_driver_2,lap_number)

    fig = go.Figure()
    fig = fig.add_trace(go.Scatter(x=telemetry_driver_1['Distance'], 
                                    y=telemetry_driver_1['Speed'], 
                                    mode='lines', 
                                    name=driver_1,
                                    hovertemplate = 'Speed: %{y}km/h'
                                    )
                        )
    fig = fig.add_trace(go.Scatter(x=telemetry_driver_2['Distance'], 
                                    y=telemetry_driver_2['Speed'], 
                                    mode='lines', 
                                    name=driver_2,
                                    hovertemplate = 'Speed: %{y}km/h'
                                    )
                        )

    # Edit the layout
    fig.update_layout(title='Comparing Speed of both drivers through the Lap',
                    xaxis_title='Distance in m',
                    yaxis_title='Speed in km/h')

    # fig.show()

    return fig


    


# %%

if __name__=='__main__':
    fig = plot_driver_comparison_for_lap_number(year=2022, grand_prix='Imola', session='R', driver_1='VER', driver_2='LEC', lap_number=5)
    fig.show()






    # # Getting into the session
    # year, grand_prix, session = 2022, 'Imola', 'R'

    # session_data = ff1.get_session(year, grand_prix, session)
    # session_data.load() # This is new with Fastf1 v.2.2

    # # This is how it used to be:
    # # laps = quali.load_laps(with_telemetry=True)
    
    # # Driver names as Input
    # driver_1, driver_2 = 'PER', 'VER'

    # # Laps can now be accessed through the .laps object coming from the session
    # laps_driver_1 = session_data.laps.pick_driver(driver_1)
    # laps_driver_2 = session_data.laps.pick_driver(driver_2)

    # # Select the fastest lap
    # fastest_driver_1 = laps_driver_1.pick_fastest()
    # fastest_driver_2 = laps_driver_2.pick_fastest()

    # # Retrieve the telemetry and add the distance column
    # telemetry_driver_1 = fastest_driver_1.get_telemetry().add_distance()
    # telemetry_driver_2 = fastest_driver_2.get_telemetry().add_distance()

    # fig, ax = plt.subplots()
    # ax.plot(telemetry_driver_1['Distance'], telemetry_driver_1['Speed'], color='red', label=driver_1)
    # ax.plot(telemetry_driver_2['Distance'], telemetry_driver_2['Speed'], color='blue', label=driver_2)

    # ax.set_xlabel('Distance in m')
    # ax.set_ylabel('Speed in km/h')

    # ax.legend()
    # plt.suptitle(f"Fastest Lap Comparison \n "
    #             f"{session_data.event['EventName']} {session_data.event.year} Race")

    # plt.show()