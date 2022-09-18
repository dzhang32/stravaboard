class BaseStravaboardError(Exception):
    pass


class AccessTokenRequestError(BaseStravaboardError):
    pass


class InvalidDataTypeError(BaseStravaboardError):
    pass
