"""
Contact Custom Field model for the OpenPhone Python SDK.
"""

from typing import Dict, Any, Optional, List
from openphone_python.models.base import BaseModel


class ContactCustomField(BaseModel):
    """
    Represents a contact custom field in OpenPhone.

    Custom contact fields enhance your OpenPhone contacts with additional
    information beyond standard details like name, company, role, emails and
    phone numbers.
    """

    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)

    @property
    def id(self) -> str:
        """Get the unique identifier of the custom field."""
        return self._get_field("id")

    @property
    def name(self) -> str:
        """Get the name of the custom field."""
        return self._get_field("name")

    @property
    def field_type(self) -> str:
        """
        Get the type of the custom field.

        Possible values: 'string', 'number', 'boolean', 'date', 'address', 'url'
        """
        return self._get_field("type")

    @property
    def required(self) -> bool:
        """Get whether this field is required."""
        return self._get_field("required", False)

    @property
    def options(self) -> Optional[List[str]]:
        """Get the available options for this field (if applicable)."""
        return self._get_field("options")

    @property
    def description(self) -> Optional[str]:
        """Get the description of this field."""
        return self._get_field("description")

    def __repr__(self) -> str:
        """String representation of the contact custom field."""
        return f"ContactCustomField(id='{self.id}', name='{self.name}', type='{self.field_type}')"
