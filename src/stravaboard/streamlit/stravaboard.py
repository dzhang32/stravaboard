from typing import List

import streamlit as st

from stravaboard.api.strava_api import StravaAPI
from stravaboard.streamlit.components import StravaboardComponent


class Stravaboard:
    """Responsible for creating a streamlit app displaying Strava data."""

    def __init__(self, client_id: str, client_secret: str, refresh_token: str) -> None:

        strava_api = StravaAPI(
            client_id=client_id,
            client_secret=client_secret,
            refresh_token=refresh_token,
        )

        self.activities = strava_api.get("activities")

    def display(self, components: List[StravaboardComponent]) -> None:
        """Display the components of a Stravaboard.

        Parameters
        ----------
        components : List[StravaboardComponent]
            objects have a display() method that displays streamlit
            component(s).
        """
        st.title("Stravaboard 🏃‍♂️🏃‍♀️")

        for component in components:

            component().display(self.activities)
