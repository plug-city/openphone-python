"""
Webhooks resource for the OpenPhone Python SDK.
"""

from typing import List, Dict, Any, Optional, Iterator
from openphone_python.models.webhook import Webhook
from openphone_python.resources.base import BaseResource


class WebhooksResource(BaseResource):
    """
    Handle all webhook-related API operations.

    Endpoints covered:
    - GET /v1/webhooks (List webhooks)
    - POST /v1/webhooks (Create webhook)
    - GET /v1/webhooks/{id} (Get webhook)
    - PUT /v1/webhooks/{id} (Update webhook)
    - DELETE /v1/webhooks/{id} (Delete webhook)
    """

    def list(self, user_id: Optional[str] = None, **kwargs) -> Iterator[Webhook]:
        """
        List webhooks.

        Args:
            user_id: Optional user ID filter (defaults to workspace owner)
            **kwargs: Additional parameters

        Returns:
            Iterator yielding Webhook instances
        """
        params = {}

        if user_id:
            params["userId"] = user_id

        # Add any additional parameters
        params.update(kwargs)

        return self._paginate("webhooks", Webhook, params)

    def create(self, webhook_data: Dict[str, Any]) -> Webhook:
        """
        Create a new webhook.

        Args:
            webhook_data: Webhook configuration

        Returns:
            Webhook instance
        """
        response = self._post("webhooks", webhook_data)
        return Webhook(response)

    def get(self, webhook_id: str) -> Webhook:
        """
        Get a specific webhook by ID.

        Args:
            webhook_id: Webhook ID

        Returns:
            Webhook instance
        """
        response = self._get(f"webhooks/{webhook_id}")
        return Webhook(response)

    def update(self, webhook_id: str, webhook_data: Dict[str, Any]) -> Webhook:
        """
        Update an existing webhook.

        Args:
            webhook_id: Webhook ID
            webhook_data: Updated webhook configuration

        Returns:
            Updated Webhook instance
        """
        response = self._put(f"webhooks/{webhook_id}", webhook_data)
        return Webhook(response)

    def delete(self, webhook_id: str) -> bool:
        """
        Delete a webhook.

        Args:
            webhook_id: Webhook ID

        Returns:
            True if successful
        """
        self._delete(f"webhooks/{webhook_id}")
        return True

    def get_all(self, user_id: Optional[str] = None) -> List[Webhook]:
        """
        Get all webhooks as a list.

        Args:
            user_id: Optional user ID filter

        Returns:
            List of Webhook instances
        """
        return list(self.list(user_id=user_id))
