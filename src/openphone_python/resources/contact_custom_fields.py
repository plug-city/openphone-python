"""
Contact Custom Fields resource for the OpenPhone Python SDK.
"""

from typing import List
from openphone_python.models.contact_custom_field import ContactCustomField
from openphone_python.resources.base import BaseResource


class ContactCustomFieldsResource(BaseResource):
    """
    Handle contact custom fields API operations.

    Endpoints covered:
    - GET /v1/contact-custom-fields (Get contact custom fields)
    """

    def list(self) -> List[ContactCustomField]:
        """
        Get contact custom fields.

        Custom contact fields enhance your OpenPhone contacts with additional
        information beyond standard details. These user-defined fields let you
        capture business-specific data.

        Returns:
            List of ContactCustomField instances
        """
        response = self._get("contact-custom-fields")
        return [ContactCustomField(field) for field in response.get("data", [])]

    def get_all(self) -> List[ContactCustomField]:
        """
        Alias for list() method for consistency.

        Returns:
            List of ContactCustomField instances
        """
        return self.list()
