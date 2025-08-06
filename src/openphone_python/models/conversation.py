"""
Conversation model for the OpenPhone Python SDK.
"""

from typing import List, Optional, Dict, Any
from datetime import datetime
from .base import BaseModel


class Conversation(BaseModel):
    """Represents an OpenPhone conversation."""

    def _parse_data(self) -> None:
        """Parse conversation-specific data."""
        # Parse timestamps
        if "createdAt" in self._data:
            self._data["created_at"] = self._parse_datetime(self._data["createdAt"])
        if "updatedAt" in self._data:
            self._data["updated_at"] = self._parse_datetime(self._data["updatedAt"])

    @property
    def id(self) -> str:
        """Conversation ID."""
        return self._data.get("id", "")

    @property
    def phone_number_id(self) -> str:
        """OpenPhone number ID."""
        return self._data.get("phoneNumberId", "")

    @property
    def participants(self) -> List[str]:
        """Conversation participants."""
        return self._data.get("participants", [])

    @property
    def user_id(self) -> str:
        """User ID associated with the conversation."""
        return self._data.get("userId", "")

    @property
    def status(self) -> str:
        """Conversation status."""
        return self._data.get("status", "")

    @property
    def type(self) -> str:
        """Conversation type (sms, call, etc.)."""
        return self._data.get("type", "")

    @property
    def last_message(self) -> Optional[Dict[str, Any]]:
        """Last message in the conversation."""
        return self._data.get("lastMessage")

    @property
    def unread_count(self) -> int:
        """Number of unread messages."""
        return self._data.get("unreadCount", 0)

    @property
    def created_at(self) -> Optional[datetime]:
        """When the conversation was created."""
        return self._data.get("created_at")

    @property
    def updated_at(self) -> Optional[datetime]:
        """When the conversation was last updated."""
        return self._data.get("updated_at")
