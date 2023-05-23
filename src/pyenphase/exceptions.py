class EnvoyFirmwareCheckError(Exception):
    """Exception raised when unable to query the Envoy firmware version."""

    def __init__(self, status_code, status):
        self.status_code = status_code
        self.status = status


class EnvoyAuthenticationError(Exception):
    """Exception raised when unable to query the Envoy firmware version."""

    def __init__(self, status):
        self.status = status
