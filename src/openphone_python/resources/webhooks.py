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
    - GET /v1/webhooks/{id} (Get webhook)
    - PUT /v1/webhooks/{id} (Update webhook)
    - DELETE /v1/webhooks/{id} (Delete webhook)
    - POST /v1/webhooks/messages (Create message webhook)
    - POST /v1/webhooks/calls (Create call webhook)
    - POST /v1/webhooks/call-summaries (Create call summary webhook)
    - POST /v1/webhooks/call-transcripts (Create call transcript webhook)
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
        Create a new webhook with intelligent routing based on events.

        This method automatically routes to the appropriate specialized endpoint
        based on the events specified in webhook_data.

        Args:
            webhook_data: Webhook configuration including 'events' list

        Returns:
            Webhook instance

        Raises:
            ValueError: If events are not specified or are invalid/mixed types
        """
        events = webhook_data.get("events", [])
        if not events:
            raise ValueError("webhook_data must include 'events' list")

        # Define event categories
        message_events = {"message.received", "message.delivered"}
        call_events = {"call.completed", "call.ringing", "call.recording.completed"}
        summary_events = {"call.summary.completed"}
        transcript_events = {"call.transcript.completed"}

        events_set = set(events)

        # Check for single-category events and route accordingly
        if events_set.issubset(message_events):
            return self._create_via_specialized_endpoint("webhooks/messages", webhook_data)
        elif events_set.issubset(call_events):
            return self._create_via_specialized_endpoint("webhooks/calls", webhook_data)
        elif events_set == summary_events:
            return self._create_via_specialized_endpoint("webhooks/call-summaries", webhook_data)
        elif events_set == transcript_events:
            return self._create_via_specialized_endpoint("webhooks/call-transcripts", webhook_data)
        else:
            # Mixed or unknown events - provide helpful error
            if len(events_set.intersection(message_events)) > 0 and len(events_set.intersection(call_events)) > 0:
                raise ValueError(
                    "Cannot mix message and call events in a single webhook. "
                    "Create separate webhooks or use specialized methods: "
                    "create_message_webhook(), create_call_webhook()"
                )
            else:
                unknown_events = events_set - message_events - call_events - summary_events - transcript_events
                raise ValueError(
                    f"Unknown events: {list(unknown_events)}. "
                    f"Valid events are: {list(message_events | call_events | summary_events | transcript_events)}"
                )

    def _create_via_specialized_endpoint(self, endpoint: str, webhook_data: Dict[str, Any]) -> Webhook:
        """
        Helper method to create webhook via specialized endpoint.

        Args:
            endpoint: The specialized endpoint path
            webhook_data: Webhook configuration

        Returns:
            Webhook instance
        """
        response = self._post(endpoint, webhook_data)
        return Webhook(response)

    def create_message_webhook(
        self,
        url: str,
        events: List[str],
        resource_ids: Optional[List[str]] = None,
        label: Optional[str] = None,
        status: str = "enabled",
        user_id: Optional[str] = None,
    ) -> Webhook:
        """
        Create a new webhook for message events.

        Args:
            url: The endpoint that receives events from the webhook
            events: List of message events (message.received, message.delivered)
            resource_ids: List of phone number IDs or ["*"] for all
            label: Webhook's label
            status: Webhook status (enabled/disabled)
            user_id: User ID that creates the webhook (defaults to workspace owner)

        Returns:
            Webhook instance
        """
        # Validate events
        valid_events = ["message.received", "message.delivered"]
        for event in events:
            if event not in valid_events:
                raise ValueError(f"Invalid message event: {event}. Valid events: {valid_events}")

        webhook_data = {
            "url": url,
            "events": events,
            "status": status,
        }

        if resource_ids:
            webhook_data["resourceIds"] = resource_ids
        if label:
            webhook_data["label"] = label
        if user_id:
            webhook_data["userId"] = user_id

        response = self._post("webhooks/messages", webhook_data)
        return Webhook(response)

    def create_call_webhook(
        self,
        url: str,
        events: List[str],
        resource_ids: Optional[List[str]] = None,
        label: Optional[str] = None,
        status: str = "enabled",
        user_id: Optional[str] = None,
    ) -> Webhook:
        """
        Create a new webhook for call events.

        Args:
            url: The endpoint that receives events from the webhook
            events: List of call events (call.completed, call.ringing, call.recording.completed)
            resource_ids: List of phone number IDs or ["*"] for all
            label: Webhook's label
            status: Webhook status (enabled/disabled)
            user_id: User ID that creates the webhook (defaults to workspace owner)

        Returns:
            Webhook instance
        """
        # Validate events
        valid_events = ["call.completed", "call.ringing", "call.recording.completed"]
        for event in events:
            if event not in valid_events:
                raise ValueError(f"Invalid call event: {event}. Valid events: {valid_events}")

        webhook_data = {
            "url": url,
            "events": events,
            "status": status,
        }

        if resource_ids:
            webhook_data["resourceIds"] = resource_ids
        if label:
            webhook_data["label"] = label
        if user_id:
            webhook_data["userId"] = user_id

        response = self._post("webhooks/calls", webhook_data)
        return Webhook(response)

    def create_call_summary_webhook(
        self,
        url: str,
        resource_ids: Optional[List[str]] = None,
        label: Optional[str] = None,
        status: str = "enabled",
        user_id: Optional[str] = None,
    ) -> Webhook:
        """
        Create a new webhook for call summary events.

        Args:
            url: The endpoint that receives events from the webhook
            resource_ids: List of phone number IDs or ["*"] for all
            label: Webhook's label
            status: Webhook status (enabled/disabled)
            user_id: User ID that creates the webhook (defaults to workspace owner)

        Returns:
            Webhook instance
        """
        webhook_data = {
            "url": url,
            "events": ["call.summary.completed"],
            "status": status,
        }

        if resource_ids:
            webhook_data["resourceIds"] = resource_ids
        if label:
            webhook_data["label"] = label
        if user_id:
            webhook_data["userId"] = user_id

        response = self._post("webhooks/call-summaries", webhook_data)
        return Webhook(response)

    def create_call_transcript_webhook(
        self,
        url: str,
        resource_ids: Optional[List[str]] = None,
        label: Optional[str] = None,
        status: str = "enabled",
        user_id: Optional[str] = None,
    ) -> Webhook:
        """
        Create a new webhook for call transcript events.

        Args:
            url: The endpoint that receives events from the webhook
            resource_ids: List of phone number IDs or ["*"] for all
            label: Webhook's label (optional)
            status: Webhook status (enabled/disabled)
            user_id: User ID that creates the webhook (defaults to workspace owner)

        Returns:
            Webhook instance
        """
        webhook_data = {
            "url": url,
            "events": ["call.transcript.completed"],
            "status": status,
        }

        if resource_ids:
            webhook_data["resourceIds"] = resource_ids
        if label:
            webhook_data["label"] = label
        if user_id:
            webhook_data["userId"] = user_id

        response = self._post("webhooks/call-transcripts", webhook_data)
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
