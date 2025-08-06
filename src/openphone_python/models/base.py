"""
Base model classes for the OpenPhone Python SDK.
"""

from typing import Dict, Any, Optional, Union
from datetime import datetime
from dateutil import parser as date_parser


class BaseModel:
    """
    Base model class for all data objects.

    Principles:
    - Consistent data access patterns
    - Type safety with optional runtime validation
    - Easy serialization/deserialization
    """

    def __init__(self, data: Dict[str, Any]):
        self._data = data
        self._parse_data()

    def _parse_data(self) -> None:
        """Parse and validate incoming data. Override in subclasses for custom parsing."""

    def _parse_datetime(self, value: Union[str, datetime, None]) -> Optional[datetime]:
        """Parse datetime from string or return as-is if already datetime."""
        if value is None:
            return None
        if isinstance(value, datetime):
            return value
        if isinstance(value, str):
            try:
                return date_parser.parse(value)
            except (ValueError, TypeError):
                return None
        return None

    def to_dict(self) -> Dict[str, Any]:
        """Convert model to dictionary."""
        return self._data.copy()

    def __getattr__(self, name: str) -> Any:
        """Access data attributes."""
        if name in self._data:
            return self._data[name]
        raise AttributeError(f"'{self.__class__.__name__}' has no attribute '{name}'")

    def __repr__(self) -> str:
        """String representation of the model."""
        class_name = self.__class__.__name__
        id_field = getattr(self, "id", None)
        if id_field:
            return f"{class_name}(id='{id_field}')"
        return f"{class_name}({dict(list(self._data.items())[:3])})"

    def __eq__(self, other: object) -> bool:
        """Check equality based on data."""
        if not isinstance(other, BaseModel):
            return False
        return self._data == other._data
