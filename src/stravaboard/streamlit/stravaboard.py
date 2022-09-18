from typing import List

import streamlit as st
from stravaboard.api.strava_api import StravaAPI
from stravaboard.streamlit.components import StravaboardComponent


class Stravaboard:
    def __init__(self, client_id, client_secret, refresh_token):

        strava_api = StravaAPI(
            client_id=client_id,
            client_secret=client_secret,
            refresh_token=refresh_token,
        )

        self.activities = strava_api.get("activities")

    def display(self, components=List[StravaboardComponent]):

        st.title("Stravaboard 🏃‍♂️🏃‍♀️")

        for component in components:

            component.display(self.activities)
