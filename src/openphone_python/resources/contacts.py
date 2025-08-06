"""
Contacts resource for the OpenPhone Python SDK.
"""

from typing import List, Dict, Any, Optional, Iterator
from openphone_python.models.contact import Contact
from openphone_python.utils.validation import validate_pagination_params
from openphone_python.resources.base import BaseResource
from openphone_python.exceptions import ValidationError


class ContactsResource(BaseResource):
    """
    Handle all contact-related API operations.

    Endpoints covered:
    - GET /v1/contacts (List contacts)
    - POST /v1/contacts (Create contact)
    - GET /v1/contacts/{id} (Get contact)
    - PUT /v1/contacts/{id} (Update contact)
    - DELETE /v1/contacts/{id} (Delete contact)
    """

    def list(
        self,
        external_ids: Optional[List[str]] = None,
        sources: Optional[List[str]] = None,
        max_results: Optional[int] = None,
        page_token: Optional[str] = None,
        **kwargs,
    ) -> Iterator[Contact]:
        """
        List contacts with filtering and pagination.

        Args:
            external_ids: Filter by external IDs
            sources: Filter by contact sources
            max_results: Maximum results per page (1-50)
            page_token: Page token for pagination
            **kwargs: Additional parameters

        Returns:
            Iterator yielding Contact instances
        """
        # Validate pagination parameters
        params = validate_pagination_params(max_results, page_token)

        # Contacts API has different max_results limit (50 instead of 100)
        if max_results is not None and max_results > 50:

            raise ValidationError("max_results for contacts must be between 1 and 50")

        # Build request parameters
        if external_ids:
            params["externalIds"] = external_ids
        if sources:
            params["sources"] = sources

        # Add any additional parameters
        params.update(kwargs)

        return self._paginate("contacts", Contact, params)

    def create(self, contact_data: Dict[str, Any]) -> Contact:
        """
        Create a new contact.

        Args:
            contact_data: Contact information

        Returns:
            Contact instance
        """
        response = self._post("contacts", contact_data)
        return Contact(response)

    def get(self, contact_id: str) -> Contact:
        """
        Get a specific contact by ID.

        Args:
            contact_id: Contact ID

        Returns:
            Contact instance
        """
        response = self._get(f"contacts/{contact_id}")
        return Contact(response)

    def update(self, contact_id: str, contact_data: Dict[str, Any]) -> Contact:
        """
        Update an existing contact.

        Args:
            contact_id: Contact ID
            contact_data: Updated contact information

        Returns:
            Updated Contact instance
        """
        response = self._put(f"contacts/{contact_id}", contact_data)
        return Contact(response)

    def delete(self, contact_id: str) -> bool:
        """
        Delete a contact.

        Args:
            contact_id: Contact ID

        Returns:
            True if successful
        """
        self._delete(f"contacts/{contact_id}")
        return True
