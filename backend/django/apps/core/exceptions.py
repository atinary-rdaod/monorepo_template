class ApplicationError(Exception):
    """Raised by services/selectors to report an expected error to the API layer."""

    def __init__(self, message: str, status: int = 400) -> None:
        super().__init__(message)
        self.message = message
        self.status = status
