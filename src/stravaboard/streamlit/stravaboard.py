import streamlit as st

from stravaboard.api.strava_api import StravaAPI
from stravaboard.streamlit.components import StravaboardComponent


class Stravaboard:
    """
    Top-level class used to create a streamlit app displaying Strava data.
    """

    def __init__(self, client_id: str, client_secret: str, refresh_token: str) -> None:
        strava_api = StravaAPI(
            client_id=client_id,
            client_secret=client_secret,
            refresh_token=refresh_token,
        )

        self.activities = strava_api.get("activities")

    def display(self, components: list[StravaboardComponent]) -> None:
        """
        Display the desired streamlit components for Stravaboard.

        Args:
            components: List of streamlit components to display.
        """
        st.title("Stravaboard 🏃‍♂️🏃‍♀️")

        for component in components:
            component_instance = component()  # type: ignore
            component_instance.display(self.activities)
