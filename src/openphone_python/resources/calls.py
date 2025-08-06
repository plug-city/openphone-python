"""
Calls resource for the OpenPhone Python SDK.
"""

from typing import List, Optional, Iterator
from openphone_python.models.call import Call
from openphone_python.utils.validation import validate_pagination_params
from openphone_python.utils.formatting import format_phone_numbers_list
from openphone_python.resources.base import BaseResource


class CallsResource(BaseResource):
    """
    Handle all call-related API operations.

    Endpoints covered:
    - GET /v1/calls (List calls)
    - GET /v1/calls/{id} (Get call by ID)
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
    ) -> Iterator[Call]:
        """
        List calls with automatic pagination.

        Args:
            phone_number_id: OpenPhone number ID
            participants: List of participant phone numbers (max 1 for now)
            user_id: Optional user ID filter
            created_after: Filter calls created after this timestamp
            created_before: Filter calls created before this timestamp
            max_results: Maximum results per page (1-100)
            page_token: Page token for pagination
            **kwargs: Additional parameters

        Returns:
            Iterator yielding Call instances
        """
        # Validate participants length (API limitation)
        if len(participants) > 1:
            from openphone_python.exceptions import ValidationError

            raise ValidationError(
                "Currently limited to one-to-one (1:1) conversations only"
            )

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

        return self._paginate("calls", Call, params)

    def get(self, call_id: str) -> Call:
        """
        Get a specific call by ID.

        Args:
            call_id: Call ID

        Returns:
            Call instance
        """
        response = self._get(f"calls/{call_id}")
        return Call(response)
