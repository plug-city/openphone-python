"""
OpenPhone Python SDK

A comprehensive Python SDK for integrating with the OpenPhone API.
"""

from ._version import __version__
from .client import OpenPhoneClient
from .exceptions import (
    OpenPhoneError,
    AuthenticationError,
    RateLimitError,
    ValidationError,
    NotFoundError,
    ApiError,
    BadRequestError,
    ForbiddenError,
    ConflictError,
    ServerError,
    NotEnoughCreditsError,
    A2PRegistrationNotApprovedError,
    TooManyParticipantsError,
    NotPhoneNumberUserError,
    InvalidVersionError,
)

__all__ = [
    "OpenPhoneClient",
    "OpenPhoneError",
    "AuthenticationError",
    "RateLimitError",
    "ValidationError",
    "NotFoundError",
    "ApiError",
    "BadRequestError",
    "ForbiddenError",
    "ConflictError",
    "ServerError",
    "NotEnoughCreditsError",
    "A2PRegistrationNotApprovedError",
    "TooManyParticipantsError",
    "NotPhoneNumberUserError",
    "InvalidVersionError",
    "__version__",
]


def main() -> None:
    print("Hello from openphone-python!")
