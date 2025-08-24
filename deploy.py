# type: ignore

"""
Deploy the Stravaboard app.

See the README for deploying the app to streamlit.

To deploy the app locally when developing:

```bash
# Install stravaboard locally (NOT in editable mode).
uv pip install .
streamlit run deploy.py
```
"""

import os

import streamlit as st
from dotenv import load_dotenv

from stravaboard.streamlit.components import Mileage, SpeedBreakdown, Summary
from stravaboard.streamlit.stravaboard import Stravaboard

# Load strava credentials from .env file.
load_dotenv()

# Change the name of the page shown on browser.
st.set_page_config(page_title="Stravaboard")

sb = Stravaboard(
    client_id=os.environ.get("STRAVA_CLIENT_ID"),
    client_secret=os.environ.get("STRAVA_CLIENT_SECRET"),
    refresh_token=os.environ.get("STRAVA_REFRESH_TOKEN"),
)
sb.display(components=[Summary, SpeedBreakdown, Mileage])
