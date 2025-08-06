"""
Exception classes for the OpenPhone Python SDK.
"""

from typing import Optional, Dict, Any


class OpenPhoneError(Exception):
    """Base exception for all OpenPhone API errors."""


class AuthenticationError(OpenPhoneError):
    """Raised when authentication fails."""


class RateLimitError(OpenPhoneError):
    """Raised when rate limit is exceeded."""

    def __init__(self, message: str, retry_after: Optional[int] = None):
        super().__init__(message)
        self.retry_after = retry_after


class ValidationError(OpenPhoneError):
    """Raised when input validation fails."""


class NotFoundError(OpenPhoneError):
    """Raised when a resource is not found."""


class ApiError(OpenPhoneError):
    """Raised for general API errors."""

    def __init__(
        self,
        message: str,
        status_code: int,
        response_data: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(message)
        self.status_code = status_code
        self.response_data = response_data or {}


class InvalidApiKeyError(AuthenticationError):
    """Raised when API key is invalid or missing."""


class OpenPhonePermissionError(OpenPhoneError):
    """Raised when the user doesn't have permission for the requested operation."""


class ServerError(OpenPhoneError):
    """Raised when the server encounters an internal error."""
