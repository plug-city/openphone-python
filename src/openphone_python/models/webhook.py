"""
Webhook model for the OpenPhone Python SDK.
"""

from typing import List, Optional
from datetime import datetime
from .base import BaseModel


class Webhook(BaseModel):
    """Represents an OpenPhone webhook."""

    def _parse_data(self) -> None:
        """Parse webhook-specific data."""
        # Parse timestamps
        if "createdAt" in self._data:
            self._data["created_at"] = self._parse_datetime(self._data["createdAt"])
        if "updatedAt" in self._data:
            self._data["updated_at"] = self._parse_datetime(self._data["updatedAt"])
        if "deletedAt" in self._data:
            self._data["deleted_at"] = self._parse_datetime(self._data["deletedAt"])

    @property
    def id(self) -> str:
        """Webhook ID."""
        return self._data.get("id", "")

    @property
    def user_id(self) -> str:
        """User ID who owns the webhook."""
        return self._data.get("userId", "")

    @property
    def org_id(self) -> str:
        """Organization ID."""
        return self._data.get("orgId", "")

    @property
    def label(self) -> str:
        """Webhook label."""
        return self._data.get("label", "")

    @property
    def status(self) -> str:
        """Webhook status (enabled/disabled)."""
        return self._data.get("status", "")

    @property
    def url(self) -> str:
        """Webhook URL."""
        return self._data.get("url", "")

    @property
    def key(self) -> str:
        """Webhook signing key."""
        return self._data.get("key", "")

    @property
    def events(self) -> List[str]:
        """List of events this webhook subscribes to."""
        return self._data.get("events", [])

    @property
    def resource_ids(self) -> List[str]:
        """List of resource IDs this webhook is associated with."""
        return self._data.get("resourceIds", [])

    @property
    def created_at(self) -> Optional[datetime]:
        """When the webhook was created."""
        return self._data.get("created_at")

    @property
    def updated_at(self) -> Optional[datetime]:
        """When the webhook was last updated."""
        return self._data.get("updated_at")

    @property
    def deleted_at(self) -> Optional[datetime]:
        """When the webhook was deleted."""
        return self._data.get("deleted_at")
