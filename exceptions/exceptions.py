class MissingParameterError(Exception):
    """
    Exception raised when parameters are missing.
    """

    pass


class UserValueError(ValueError):
    """
    Exception raised when a user supplies an invalid value to the Arthur SDK.
    """

    pass
