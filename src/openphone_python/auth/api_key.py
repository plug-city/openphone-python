"""
Authentication handling for the OpenPhone Python SDK.
"""

from typing import Dict
from openphone_python.exceptions import InvalidApiKeyError


class ApiKeyAuth:
    """
    Handle API key authentication for OpenPhone.

    Principles:
    - Secure key storage
    - Automatic header injection
    - Key validation
    """

    def __init__(self, api_key: str):
        self.api_key = api_key
        self._validate_key()

    def _validate_key(self) -> None:
        """Validate API key format."""
        if not self.api_key or not isinstance(self.api_key, str):
            raise InvalidApiKeyError("API key must be a non-empty string")

        if len(self.api_key.strip()) == 0:
            raise InvalidApiKeyError("API key cannot be empty or whitespace")

    def get_headers(self) -> Dict[str, str]:
        """Get authentication headers."""
        return {"Authorization": self.api_key}

    def __repr__(self) -> str:
        """String representation (without exposing the key)."""
        return f"ApiKeyAuth(key='***{self.api_key[-4:] if len(self.api_key) >= 4 else '***'}')"
