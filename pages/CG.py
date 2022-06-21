import os
from datetime import datetime

from dotenv import load_dotenv

import streamlit as st
from stravaboard.streamlit import display_breakdown, display_summary, load_activities

##### Load environmental variables #####

load_dotenv()

##### Main #####

st.set_page_config(page_title="Stravaboard")

# load and tidy activity data
now = datetime.now().strftime("%d/%m/%Y-%H")

cg_act = load_activities(
    datetime_now=now,
    client_id=os.environ.get("STRAVA_CLIENT_ID_CG"),
    client_secret=os.environ.get("STRAVA_CLIENT_SECRET_CG"),
    refresh_token=os.environ.get("STRAVA_REFRESH_TOKEN_CG"),
)

st.title("Celestia's Stravaboard 🏃‍♂️🏃‍♀️")

display_summary(cg_act)

display_breakdown(cg_act)
