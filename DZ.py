import os
from datetime import datetime

from dotenv import load_dotenv

import streamlit as st
from stravaboard.streamlit import display_breakdown, display_summary, load_activities

st.set_page_config(page_title="Stravaboard")

##### Load environmental variables #####

load_dotenv()

##### Main #####

# load and tidy activity data
now = datetime.now().strftime("%d/%m/%Y-%H")

dz_act = load_activities(
    datetime_now=now,
    client_id=os.environ.get("STRAVA_CLIENT_ID_DZ"),
    client_secret=os.environ.get("STRAVA_CLIENT_SECRET_DZ"),
    refresh_token=os.environ.get("STRAVA_REFRESH_TOKEN_DZ"),
)

st.title("David's Stravaboard 🏃‍♂️🏃‍♀️")

display_summary(dz_act)

st.header("The breakdown")

display_breakdown(
    dz_act, title="Date (x) vs distance (y), coloured by speed (white = fastest)"
)

display_breakdown(
    dz_act,
    title="Date (x) vs speed (y), coloured by distance (blue = shortest)",
    y="speed_mins_per_km",
    color="distance_km",
    color_continuous_scale=["blue", "purple", "violet"],
)
