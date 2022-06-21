from datetime import datetime

import pandas as pd
import plotly.express as px
from dateutil.relativedelta import relativedelta

import streamlit as st
from stravaboard.activities import Activities


@st.cache
def load_activities(
    client_id: str, client_secret: str, refresh_token: str, datetime_now: str
) -> pd.DataFrame:
    """Load activity data using the Strava API.

    Parameters
    ----------
    client_id : str
        Strava client ID.
    client_secret : str
        Strava client secret.
    refresh_token : str
        Strava client refresh token.
    datetime_now : str
        The current time in the format "%d/%m/%Y-%H". Combined with st.cache, this
        should monitor the state of the function, such that re-requests will only occur
        if an hour has passed since the last request.

    Returns
    -------
    pd.DataFrame
        contains the Strava activity data.
    """
    act = Activities(
        client_id=client_id,
        client_secret=client_secret,
        refresh_token=refresh_token,
    )

    act.request_activities()
    act.tidy_activities()

    return act.activities


def display_summary(activities: pd.DataFrame) -> None:
    """Display a summary of the Strava activity data via Streamlit.

    Parameters
    ----------
    activities : pd.DataFrame
        Strava activity data obtained through load_activities().
    """

    st.header("The summary")

    st.write(
        "You've run a total of ",
        str(round(activities["distance_km"].sum(), 2)),
        "km over ",
        str(round(activities["elapsed_min"].sum() / 60, 2)),
        " sweaty hours 🥳",
    )

    total_across = st.radio(
        "Across the last _____, that's: ", ("week", "month", "year")
    )

    if total_across == "week":
        date_delta = relativedelta(days=7)
    elif total_across == "month":
        date_delta = relativedelta(months=1)
    else:
        date_delta = relativedelta(years=1)

    latest_date = datetime.now()
    total_across_df = activities.loc[activities["date"] > (latest_date - date_delta)]
    total_km = total_across_df["distance_km"].sum()
    total_hours = round(total_across_df["distance_km"].sum() / 60, 2)

    st.write(str(total_km), "km and ", str(total_hours), " hours 💪")


def display_breakdown(activities: pd.DataFrame) -> None:
    """Display a breakdown as a scatterplot on Streamlit.

    Parameters
    ----------
    activities : pd.DataFrame
        Strava activity data obtained through load_activities().
    """

    st.header("The breakdown")

    fig = px.scatter(
        activities,
        x="date",
        y="distance_km",
        color="speed_mins_per_km",
        color_continuous_scale=["white", "yellow", "red"],
        trendline="rolling",
        trendline_options=dict(window=10),
        labels={
            "date": "Date of run",
            "distance_km": "Distance (km)",
            "speed_mins_per_km": "Split speed (mins per km)",
            "elapsed_min": "Elapsed time (mins)",
            "total_elevation_gain": "Total elevation gain (m)",
        },
        hover_data=[
            "date",
            "distance_km",
            "speed_mins_per_km",
            "elapsed_min",
            "total_elevation_gain",
        ],
        width=800,
        height=600,
        title="Date (x) vs distance (y), coloured by speed (white = fastest)",
    )

    fig.update_traces(marker={"size": 10})
    fig.add_hline(
        y=1.25,
        line_dash="dot",
        line_color="green",
        annotation_text="Short, pace runs ",
        annotation_position="bottom right",
        annotation_font_color="green",
        annotation_font_size=15,
    )

    st.plotly_chart(fig, use_container_width=False)
