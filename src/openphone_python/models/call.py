"""
Call model for the OpenPhone Python SDK.
"""

from typing import List, Optional
from datetime import datetime
from .base import BaseModel


class Call(BaseModel):
    """Represents an OpenPhone call."""

    def _parse_data(self) -> None:
        """Parse call-specific data."""
        # Parse timestamps
        if "answeredAt" in self._data:
            self._data["answered_at"] = self._parse_datetime(self._data["answeredAt"])
        if "completedAt" in self._data:
            self._data["completed_at"] = self._parse_datetime(self._data["completedAt"])
        if "createdAt" in self._data:
            self._data["created_at"] = self._parse_datetime(self._data["createdAt"])
        if "updatedAt" in self._data:
            self._data["updated_at"] = self._parse_datetime(self._data["updatedAt"])

    @property
    def id(self) -> str:
        """Call ID."""
        return self._data.get("id", "")

    @property
    def answered_at(self) -> Optional[datetime]:
        """When the call was answered."""
        return self._data.get("answered_at")

    @property
    def answered_by(self) -> Optional[str]:
        """User ID who answered the call."""
        return self._data.get("answeredBy")

    @property
    def initiated_by(self) -> Optional[str]:
        """User ID who initiated the call."""
        return self._data.get("initiatedBy")

    @property
    def direction(self) -> str:
        """Call direction (incoming/outgoing)."""
        return self._data.get("direction", "")

    @property
    def status(self) -> str:
        """Call status."""
        return self._data.get("status", "")

    @property
    def completed_at(self) -> Optional[datetime]:
        """When the call was completed."""
        return self._data.get("completed_at")

    @property
    def duration(self) -> Optional[int]:
        """Call duration in seconds."""
        return self._data.get("duration")

    @property
    def forwarded_from(self) -> Optional[str]:
        """Number call was forwarded from."""
        return self._data.get("forwardedFrom")

    @property
    def forwarded_to(self) -> Optional[str]:
        """Number call was forwarded to."""
        return self._data.get("forwardedTo")

    @property
    def phone_number_id(self) -> str:
        """OpenPhone number ID."""
        return self._data.get("phoneNumberId", "")

    @property
    def participants(self) -> List[str]:
        """Call participants."""
        return self._data.get("participants", [])

    @property
    def user_id(self) -> str:
        """User ID associated with the call."""
        return self._data.get("userId", "")

    @property
    def created_at(self) -> Optional[datetime]:
        """When the call record was created."""
        return self._data.get("created_at")

    @property
    def updated_at(self) -> Optional[datetime]:
        """When the call record was last updated."""
        return self._data.get("updated_at")
