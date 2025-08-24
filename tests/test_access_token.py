from datetime import datetime

import pytest

from stravaboard.api.access_token import AccessTokenManager
from stravaboard.exceptions import AccessTokenRequestError


def test_AccessTokenRequestError_retrieves_access_token_correctly(
    access_token_manager: AccessTokenManager,
) -> None:
    assert len(access_token_manager.access_token) == 40
    assert isinstance(access_token_manager.access_token, str)
    assert isinstance(access_token_manager.last_updated, datetime)


def test_AccessTokenManager_errors_on_bad_credentials() -> None:
    with pytest.raises(AccessTokenRequestError, match="Strava credentials"):
        AccessTokenManager(
            client_id="a",
            client_secret="b",
            refresh_token="c",
        )
