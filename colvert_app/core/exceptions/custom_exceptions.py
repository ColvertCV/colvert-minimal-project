"""Custom exceptions for the application."""

class InvalidTokenException(Exception):
    """Exception raised when a token is invalid."""
    def __init__(self, message: str = "Invalid token"):
        self.message = message
        super().__init__(self.message)

class UnauthorizedAccessException(Exception):
    """Exception raised when access is unauthorized."""
    def __init__(self, message: str = "Unauthorized access"):
        self.message = message
        super().__init__(self.message)
