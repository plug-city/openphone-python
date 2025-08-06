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
)

__all__ = [
    "OpenPhoneClient",
    "OpenPhoneError",
    "AuthenticationError",
    "RateLimitError",
    "ValidationError",
    "NotFoundError",
    "ApiError",
    "__version__",
]


def main() -> None:
    print("Hello from openphone-python!")
