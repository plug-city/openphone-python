"""
Main client class for the OpenPhone Python SDK.
"""

from typing import Optional
from openphone_python.auth.api_key import ApiKeyAuth
from openphone_python.resources.messages import MessagesResource
from openphone_python.resources.contacts import ContactsResource
from openphone_python.resources.contact_custom_fields import ContactCustomFieldsResource
from openphone_python.resources.phone_numbers import PhoneNumbersResource
from openphone_python.resources.calls import CallsResource
from openphone_python.resources.call_recordings import CallRecordingsResource
from openphone_python.resources.call_summaries import CallSummariesResource
from openphone_python.resources.call_transcripts import CallTranscriptsResource
from openphone_python.resources.webhooks import WebhooksResource
from openphone_python.resources.conversations import ConversationsResource


class OpenPhoneClient:
    """
    Main client for interacting with the OpenPhone API.

    Principles:
    - Single entry point for all API operations
    - Lazy loading of resources
    - Centralized configuration and authentication
    """

    def __init__(self, api_key: str, base_url: str = "https://api.openphone.com/v1"):
        """
        Initialize OpenPhone client.

        Args:
            api_key: OpenPhone API key
            base_url: Base URL for OpenPhone API
        """
        self.base_url = base_url.rstrip("/")
        self.auth = ApiKeyAuth(api_key)
        self.version = "0.1.0"

        # Lazy-loaded resources
        self._messages: Optional[MessagesResource] = None
        self._contacts: Optional[ContactsResource] = None
        self._contact_custom_fields: Optional[ContactCustomFieldsResource] = None
        self._phone_numbers: Optional[PhoneNumbersResource] = None
        self._calls: Optional[CallsResource] = None
        self._call_recordings: Optional[CallRecordingsResource] = None
        self._call_summaries: Optional[CallSummariesResource] = None
        self._call_transcripts: Optional[CallTranscriptsResource] = None
        self._webhooks: Optional[WebhooksResource] = None
        self._conversations: Optional[ConversationsResource] = None

    @property
    def messages(self) -> MessagesResource:
        """Get messages resource."""
        if self._messages is None:
            self._messages = MessagesResource(self)
        return self._messages

    @property
    def contacts(self) -> ContactsResource:
        """Get contacts resource."""
        if self._contacts is None:
            self._contacts = ContactsResource(self)
        return self._contacts

    @property
    def contact_custom_fields(self) -> ContactCustomFieldsResource:
        """Get contact custom fields resource."""
        if self._contact_custom_fields is None:
            self._contact_custom_fields = ContactCustomFieldsResource(self)
        return self._contact_custom_fields

    @property
    def phone_numbers(self) -> PhoneNumbersResource:
        """Get phone numbers resource."""
        if self._phone_numbers is None:
            self._phone_numbers = PhoneNumbersResource(self)
        return self._phone_numbers

    @property
    def calls(self) -> CallsResource:
        """Get calls resource."""
        if self._calls is None:
            self._calls = CallsResource(self)
        return self._calls

    @property
    def call_recordings(self) -> CallRecordingsResource:
        """Get call recordings resource."""
        if self._call_recordings is None:
            self._call_recordings = CallRecordingsResource(self)
        return self._call_recordings

    @property
    def call_summaries(self) -> CallSummariesResource:
        """Get call summaries resource."""
        if self._call_summaries is None:
            self._call_summaries = CallSummariesResource(self)
        return self._call_summaries

    @property
    def call_transcripts(self) -> CallTranscriptsResource:
        """Get call transcripts resource."""
        if self._call_transcripts is None:
            self._call_transcripts = CallTranscriptsResource(self)
        return self._call_transcripts

    @property
    def webhooks(self) -> WebhooksResource:
        """Get webhooks resource."""
        if self._webhooks is None:
            self._webhooks = WebhooksResource(self)
        return self._webhooks

    @property
    def conversations(self) -> ConversationsResource:
        """Get conversations resource."""
        if self._conversations is None:
            self._conversations = ConversationsResource(self)
        return self._conversations

    def __repr__(self) -> str:
        """String representation of client."""
        return f"OpenPhoneClient(base_url='{self.base_url}')"
