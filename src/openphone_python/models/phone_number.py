"""
Phone number model for the OpenPhone Python SDK.
"""

from typing import List, Dict, Any, Optional
from datetime import datetime
from .base import BaseModel


class PhoneNumber(BaseModel):
    """Represents an OpenPhone number."""

    def _parse_data(self) -> None:
        """Parse phone number-specific data."""
        # Parse timestamps
        if "createdAt" in self._data:
            self._data["created_at"] = self._parse_datetime(self._data["createdAt"])
        if "updatedAt" in self._data:
            self._data["updated_at"] = self._parse_datetime(self._data["updatedAt"])

    @property
    def id(self) -> str:
        """Phone number ID."""
        return self._data.get("id", "")

    @property
    def group_id(self) -> str:
        """Group ID."""
        return self._data.get("groupId", "")

    @property
    def name(self) -> str:
        """Phone number name/label."""
        return self._data.get("name", "")

    @property
    def number(self) -> str:
        """Phone number."""
        return self._data.get("number", "")

    @property
    def formatted_number(self) -> str:
        """Formatted phone number."""
        return self._data.get("formattedNumber", "")

    @property
    def forward(self) -> Optional[str]:
        """Forward number."""
        return self._data.get("forward")

    @property
    def port_request_id(self) -> Optional[str]:
        """Port request ID."""
        return self._data.get("portRequestId")

    @property
    def porting_status(self) -> Optional[str]:
        """Porting status."""
        return self._data.get("portingStatus")

    @property
    def symbol(self) -> Optional[str]:
        """Phone number symbol/emoji."""
        return self._data.get("symbol")

    @property
    def users(self) -> List[Dict[str, Any]]:
        """Users associated with this phone number."""
        return self._data.get("users", [])

    @property
    def restrictions(self) -> Dict[str, Any]:
        """Usage restrictions."""
        return self._data.get("restrictions", {})

    @property
    def created_at(self) -> Optional[datetime]:
        """When the phone number was created."""
        return self._data.get("created_at")

    @property
    def updated_at(self) -> Optional[datetime]:
        """When the phone number was last updated."""
        return self._data.get("updated_at")
