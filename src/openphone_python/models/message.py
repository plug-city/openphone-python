"""
Message model for the OpenPhone Python SDK.
"""

from typing import List, Optional
from datetime import datetime
from .base import BaseModel


class Message(BaseModel):
    """Represents an OpenPhone message."""

    def _parse_data(self) -> None:
        """Parse message-specific data."""
        # Parse timestamps
        if "createdAt" in self._data:
            self._data["created_at"] = self._parse_datetime(self._data["createdAt"])
        if "updatedAt" in self._data:
            self._data["updated_at"] = self._parse_datetime(self._data["updatedAt"])

    @property
    def id(self) -> str:
        """Message ID."""
        return self._data.get("id", "")

    @property
    def to(self) -> List[str]:
        """List of recipient phone numbers."""
        return self._data.get("to", [])

    @property
    def from_number(self) -> str:
        """Sender phone number."""
        return self._data.get("from", "")

    @property
    def text(self) -> str:
        """Message content."""
        return self._data.get("text", "")

    @property
    def phone_number_id(self) -> str:
        """OpenPhone number ID."""
        return self._data.get("phoneNumberId", "")

    @property
    def direction(self) -> str:
        """Message direction (incoming/outgoing)."""
        return self._data.get("direction", "")

    @property
    def user_id(self) -> str:
        """User ID who sent/received the message."""
        return self._data.get("userId", "")

    @property
    def status(self) -> str:
        """Message status."""
        return self._data.get("status", "")

    @property
    def created_at(self) -> Optional[datetime]:
        """When the message was created."""
        return self._data.get("created_at")

    @property
    def updated_at(self) -> Optional[datetime]:
        """When the message was last updated."""
        return self._data.get("updated_at")
