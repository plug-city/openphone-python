"""
Messages resource for the OpenPhone Python SDK.
"""

from typing import List, Optional, Iterator
from openphone_python.models.message import Message
from openphone_python.utils.validation import validate_pagination_params
from openphone_python.utils.formatting import (
    format_phone_numbers_list,
    ensure_e164_format,
)
from .base import BaseResource


class MessagesResource(BaseResource):
    """
    Handle all message-related API operations.

    Endpoints covered:
    - GET /v1/messages (List messages)
    - POST /v1/messages (Send message)
    - GET /v1/messages/{id} (Get message by ID)
    """

    def list(
        self,
        phone_number_id: str,
        participants: List[str],
        user_id: Optional[str] = None,
        created_after: Optional[str] = None,
        created_before: Optional[str] = None,
        max_results: Optional[int] = None,
        page_token: Optional[str] = None,
        **kwargs,
    ) -> Iterator[Message]:
        """
        List messages with automatic pagination.

        Args:
            phone_number_id: OpenPhone number ID
            participants: List of participant phone numbers
            user_id: Optional user ID filter
            created_after: Filter messages created after this timestamp
            created_before: Filter messages created before this timestamp
            max_results: Maximum results per page (1-100)
            page_token: Page token for pagination
            **kwargs: Additional parameters

        Returns:
            Iterator yielding Message instances
        """
        # Validate and format parameters
        participants = format_phone_numbers_list(participants)
        params = validate_pagination_params(max_results, page_token)

        # Build request parameters
        params.update(
            {
                "phoneNumberId": phone_number_id,
                "participants": participants,
            }
        )

        if user_id:
            params["userId"] = user_id
        if created_after:
            params["createdAfter"] = created_after
        if created_before:
            params["createdBefore"] = created_before

        # Add any additional parameters
        params.update(kwargs)

        return self._paginate("messages", Message, params)

    def send(
        self,
        content: str,
        from_number: str,
        to_numbers: List[str],
        user_id: Optional[str] = None,
    ) -> Message:
        """
        Send a text message.

        Args:
            content: Message content
            from_number: Sender phone number
            to_numbers: List of recipient phone numbers
            user_id: Optional user ID to send as

        Returns:
            Message instance
        """
        # Validate and format phone numbers
        from_number = ensure_e164_format(from_number)
        to_numbers = format_phone_numbers_list(to_numbers)

        # Build request data
        data = {
            "content": content,
            "from": from_number,
            "to": to_numbers,
        }

        if user_id:
            data["userId"] = user_id

        response = self._post("messages", data)
        return Message(response)

    def get(self, message_id: str) -> Message:
        """
        Get a specific message by ID.

        Args:
            message_id: Message ID

        Returns:
            Message instance
        """
        response = self._get(f"messages/{message_id}")
        return Message(response)
