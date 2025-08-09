"""
Resources module for the OpenPhone Python SDK.
"""

from .base import BaseResource
from .messages import MessagesResource
from .contacts import ContactsResource
from .contact_custom_fields import ContactCustomFieldsResource
from .phone_numbers import PhoneNumbersResource
from .calls import CallsResource
from .call_recordings import CallRecordingsResource
from .call_summaries import CallSummariesResource
from .call_transcripts import CallTranscriptsResource
from .webhooks import WebhooksResource
from .conversations import ConversationsResource

__all__ = [
    "BaseResource",
    "MessagesResource",
    "ContactsResource",
    "ContactCustomFieldsResource",
    "PhoneNumbersResource",
    "CallsResource",
    "CallRecordingsResource",
    "CallSummariesResource",
    "CallTranscriptsResource",
    "WebhooksResource",
    "ConversationsResource",
]
