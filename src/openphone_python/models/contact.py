"""
Contact model for the OpenPhone Python SDK.
"""

from typing import List, Dict, Any, Optional
from datetime import datetime
from .base import BaseModel


class DefaultFields(BaseModel):
    """Default contact fields."""

    @property
    def company(self) -> Optional[str]:
        """Company name."""
        return self._data.get("company")

    @property
    def emails(self) -> List[Dict[str, str]]:
        """Email addresses."""
        return self._data.get("emails", [])

    @property
    def first_name(self) -> Optional[str]:
        """First name."""
        return self._data.get("firstName")

    @property
    def last_name(self) -> Optional[str]:
        """Last name."""
        return self._data.get("lastName")

    @property
    def phone_numbers(self) -> List[Dict[str, str]]:
        """Phone numbers."""
        return self._data.get("phoneNumbers", [])

    @property
    def role(self) -> Optional[str]:
        """Role/title."""
        return self._data.get("role")


class Contact(BaseModel):
    """Represents an OpenPhone contact."""

    def _parse_data(self) -> None:
        """Parse contact-specific data."""
        # Parse timestamps
        if "createdAt" in self._data:
            self._data["created_at"] = self._parse_datetime(self._data["createdAt"])
        if "updatedAt" in self._data:
            self._data["updated_at"] = self._parse_datetime(self._data["updatedAt"])

        # Parse default fields
        if "defaultFields" in self._data:
            self._data["default_fields"] = DefaultFields(self._data["defaultFields"])

    @property
    def id(self) -> str:
        """Contact ID."""
        return self._data.get("id", "")

    @property
    def external_id(self) -> Optional[str]:
        """External system ID."""
        return self._data.get("externalId")

    @property
    def source(self) -> str:
        """Contact source."""
        return self._data.get("source", "")

    @property
    def source_url(self) -> str:
        """Source URL."""
        return self._data.get("sourceUrl", "")

    @property
    def default_fields(self) -> Optional[DefaultFields]:
        """Default contact fields."""
        return self._data.get("default_fields")

    @property
    def custom_fields(self) -> List[Dict[str, Any]]:
        """Custom contact fields."""
        return self._data.get("customFields", [])

    @property
    def created_at(self) -> Optional[datetime]:
        """When the contact was created."""
        return self._data.get("created_at")

    @property
    def updated_at(self) -> Optional[datetime]:
        """When the contact was last updated."""
        return self._data.get("updated_at")

    @property
    def created_by_user_id(self) -> str:
        """User ID who created the contact."""
        return self._data.get("createdByUserId", "")
