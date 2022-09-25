import os

import streamlit as st
from dotenv import load_dotenv

from stravaboard.streamlit.components import Mileage, SpeedBreakdown, Summary
from stravaboard.streamlit.stravaboard import Stravaboard

# load strava credentials from .env
load_dotenv()

# change the name of the page shown on browser
st.set_page_config(page_title="Stravaboard")

sb = Stravaboard(
    client_id=os.environ.get("STRAVA_CLIENT_ID"),
    client_secret=os.environ.get("STRAVA_CLIENT_SECRET"),
    refresh_token=os.environ.get("STRAVA_REFRESH_TOKEN"),
)
sb.display(components=[Summary, SpeedBreakdown, Mileage])
