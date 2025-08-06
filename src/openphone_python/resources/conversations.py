"""
Conversations resource for the OpenPhone Python SDK.
"""

from typing import List, Optional, Iterator
from openphone_python.models.conversation import Conversation
from openphone_python.utils.validation import validate_pagination_params
from openphone_python.resources.base import BaseResource


class ConversationsResource(BaseResource):
    """
    Handle all conversation-related API operations.

    Endpoints covered:
    - GET /v1/conversations (List conversations)
    """

    def list(
        self,
        max_results: Optional[int] = None,
        page_token: Optional[str] = None,
        **kwargs,
    ) -> Iterator[Conversation]:
        """
        List conversations with automatic pagination.

        Args:
            max_results: Maximum results per page
            page_token: Page token for pagination
            **kwargs: Additional parameters

        Returns:
            Iterator yielding Conversation instances
        """
        # Validate pagination parameters
        params = validate_pagination_params(max_results, page_token)

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
