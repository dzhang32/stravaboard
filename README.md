# stravaboard

A dashboard for flexibly displaying and tracking Strava runs.

## Usage

1. Obtain your personal Strava API credentials (client id, client secret and refresh token). If it's your first time using these, you may find the instructions in this [article](https://towardsdatascience.com/using-the-strava-api-and-pandas-to-explore-your-activity-data-d94901d9bfde) helpful.
2. Create an account on [streamlit](https://streamlit.io), this must be connected to your GitHub account.
3. Fork this repo on your GitHub account.
4. Create a [New app](https://share.streamlit.io):
    - Seed from your forked repo's `master` branch.
    - Set the "Main file path" as `deploy.py`.
    - In "Advanced settings", input your Strava API credentials in the format:

        ```bash
        STRAVA_CLIENT_ID = "your_client_id"
        STRAVA_CLIENT_SECRET = "your_client_secret"
        STRAVA_REFRESH_TOKEN = "your_refresh_token"
        ```

## Customising stravaboard

The main advantage of stravaboard is it's flexibility to track and present your run metrics and in any form you like. To add new components to stravaboard:

1. Create a new subclass of `StravaboardComponent` in `src/stravaboard/streamlit/components.py`. Essentially, this requires a single method, `display()`, which should generate your desired data/plots via streamlit-compatible functions.
2. Add your new subclass to the list of components in `deploy.py`.

## Credits

Data is retreived through the [Strava API](https://developers.strava.com) and the dashboard is deployed using [Streamlit](https://streamlit.io).
