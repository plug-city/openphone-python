"""
Conversations resource for the OpenPhone Python SDK.
"""

from typing import List, Optional, Iterator, Union
from openphone_python.models.conversation import Conversation
from openphone_python.utils.validation import validate_pagination_params
from openphone_python.utils.formatting import format_phone_numbers_list
from openphone_python.resources.base import BaseResource


class ConversationsResource(BaseResource):
    """
    Handle all conversation-related API operations.

    Endpoints covered:
    - GET /v1/conversations (List conversations)
    """

    def list(
        self,
        phone_number: Optional[str] = None,  # DEPRECATED
        phone_numbers: Optional[List[str]] = None,
        user_id: Optional[str] = None,
        updated_after: Optional[str] = None,
        updated_before: Optional[str] = None,
        max_results: Optional[int] = None,
        page_token: Optional[str] = None,
        **kwargs,
    ) -> Iterator[Conversation]:
        """
        List conversations with automatic pagination.

        Args:
            phone_number: DEPRECATED - use phone_numbers instead. Single OpenPhone number
            phone_numbers: List of OpenPhone numbers to filter by (up to 100)
            user_id: Filter by user ID
            updated_after: Filter conversations updated after this timestamp (ISO 8601)
            updated_before: Filter conversations updated before this timestamp (ISO 8601)
            max_results: Maximum results per page (1-100, default 10)
            page_token: Page token for pagination
            **kwargs: Additional parameters

        Returns:
            Iterator yielding Conversation instances
        """
        # Validate pagination parameters
        params = validate_pagination_params(max_results, page_token)

        # Handle phone number filtering
        if phone_numbers and phone_number:
            # If both are provided, phone_numbers takes precedence
            phone_numbers = format_phone_numbers_list(phone_numbers)
            params["phoneNumbers"] = phone_numbers
        elif phone_numbers:
            phone_numbers = format_phone_numbers_list(phone_numbers)
            params["phoneNumbers"] = phone_numbers
        elif phone_number:
            # Use deprecated parameter for backward compatibility
            params["phoneNumber"] = phone_number

        # Add optional filters
        if user_id:
            params["userId"] = user_id
        if updated_after:
            params["updatedAfter"] = updated_after
        if updated_before:
            params["updatedBefore"] = updated_before

        # Add any additional parameters
        params.update(kwargs)

        return self._paginate("conversations", Conversation, params)

    def get_all(self) -> List[Conversation]:
        """
        Get all conversations as a list.

        Returns:
            List of Conversation instances
        """
        return list(self.list())
