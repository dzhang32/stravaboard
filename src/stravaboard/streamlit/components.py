from abc import ABC, abstractmethod
from datetime import datetime

import plotly.express as px
import streamlit as st
from dateutil.relativedelta import relativedelta


class StravaboardComponent(ABC):
    @abstractmethod
    def display() -> None:
        pass


class Summary(StravaboardComponent):
    @staticmethod
    def display(activities) -> None:

        st.write(
            "In total, you've run ",
            str(round(activities["distance_km"].sum(), 2)),
            "km over ",
            str(round(activities["elapsed_min"].sum() / 60, 2)),
            " hours 🥳",
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
        total_across_df = activities.loc[
            activities["date"] > (latest_date - date_delta)
        ]
        total_km = round(total_across_df["distance_km"].sum(), 2)
        total_hours = round(total_across_df["elapsed_min"].sum() / 60, 2)

        st.write(str(total_km), "km and ", str(total_hours), " hours 💪")


class SpeedBreakdown(StravaboardComponent):
    def display(self, activities):

        st.header("The speed breakdown")

        threshold = st.slider(
            "Short/long run threshold (km)",
            activities["distance_km"].min(),
            activities["distance_km"].max(),
            3.0,
        )

        self._plot_speed_breakdown(
            activities.loc[
                activities["distance_km"] < threshold,
            ],
            title=f"Short runs (< {threshold}km)",
        )

        self._plot_speed_breakdown(
            activities.loc[
                activities["distance_km"] >= threshold,
            ],
            title=f"Long runs (>= {threshold}km)",
        )

    @staticmethod
    def _plot_speed_breakdown(activities, title):

        fig = px.scatter(
            activities,
            x="date",
            y="speed_mins_per_km",
            color="distance_km",
            color_continuous_scale=["white", "yellow", "red"],
            trendline="rolling",
            trendline_options=dict(window=5),
            labels={
                "date": "Date of run",
                "distance_km": "Distance (km)",
                "speed_mins_per_km": "Pace (min/km)",
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
            title=title,
        )

        fig.update_traces(marker={"size": 10, "line": dict(width=1, color="white")})

        st.plotly_chart(fig, use_container_width=False)
