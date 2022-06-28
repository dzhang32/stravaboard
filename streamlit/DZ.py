import os
from datetime import datetime

from dotenv import load_dotenv

import streamlit as st
from stravaboard.streamlit import stravaboard

st.set_page_config(page_title="Stravaboard")

##### Load environmental variables #####

load_dotenv()

##### Main #####

# load and tidy activity data
# trigger streamlit reload
now = datetime.now().strftime("%d/%m/%Y-%H")

stravaboard(
    name="David",
    datetime_now=now,
    client_id=os.environ.get("STRAVA_CLIENT_ID_DZ"),
    client_secret=os.environ.get("STRAVA_CLIENT_SECRET_DZ"),
    refresh_token=os.environ.get("STRAVA_REFRESH_TOKEN_DZ"),
    y="speed_mins_per_km",
    color="distance_km",
    color_continuous_scale=["blue", "purple", "violet"],
)
