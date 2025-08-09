"""
Exception classes for the OpenPhone Python SDK.
"""

from typing import Optional, Dict, Any, List


class OpenPhoneError(Exception):
    """Base exception for all OpenPhone API errors."""

    def __init__(
        self,
        message: str,
        code: Optional[str] = None,
        status_code: Optional[int] = None,
        docs: Optional[str] = None,
        title: Optional[str] = None,
        errors: Optional[List[Dict[str, Any]]] = None,
        trace: Optional[str] = None,
    ):
        super().__init__(message)
        self.code = code
        self.status_code = status_code
        self.docs = docs
        self.title = title
        self.errors = errors or []
        self.trace = trace


class AuthenticationError(OpenPhoneError):
    """Raised when authentication fails (401)."""


class ForbiddenError(OpenPhoneError):
    """Raised when access is forbidden (403)."""


class NotFoundError(OpenPhoneError):
    """Raised when a resource is not found (404)."""


class ConflictError(OpenPhoneError):
    """Raised when there's a conflict (409)."""


class ValidationError(OpenPhoneError):
    """Raised when input validation fails (400)."""


class BadRequestError(OpenPhoneError):
    """Raised for bad requests (400)."""


class NotEnoughCreditsError(OpenPhoneError):
    """Raised when organization doesn't have enough prepaid credits (402)."""


class A2PRegistrationNotApprovedError(OpenPhoneError):
    """Raised when A2P registration is not approved."""


class TooManyParticipantsError(OpenPhoneError):
    """Raised when too many participants are specified."""


class NotPhoneNumberUserError(OpenPhoneError):
    """Raised when user is not associated with the phone number."""


class InvalidVersionError(OpenPhoneError):
    """Raised when API version is invalid."""


class ServerError(OpenPhoneError):
    """Raised when the server encounters an internal error (500)."""


class RateLimitError(OpenPhoneError):
    """Raised when rate limit is exceeded."""

    def __init__(self, message: str, retry_after: Optional[int] = None, **kwargs):
        super().__init__(message, **kwargs)
        self.retry_after = retry_after


class ApiError(OpenPhoneError):
    """Raised for general API errors."""

    def __init__(
        self,
        message: str,
        status_code: int,
        response_data: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        super().__init__(message, status_code=status_code, **kwargs)
        self.response_data = response_data or {}


# Legacy aliases for backward compatibility
InvalidApiKeyError = AuthenticationError
OpenPhonePermissionError = ForbiddenError
