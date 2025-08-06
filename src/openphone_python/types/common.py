"""
Common type definitions for the OpenPhone Python SDK.
"""

from typing import TypeVar, Dict, Any, List, Union, Optional
from datetime import datetime

# Generic types
T = TypeVar("T")
JSONDict = Dict[str, Any]
PhoneNumberList = List[str]

# API response types
ApiResponse = JSONDict
PaginatedResponse = JSONDict

# Common field types
UserId = str
PhoneNumberId = str
ContactId = str
MessageId = str
CallId = str
WebhookId = str
ConversationId = str

# Phone number format
PhoneNumber = str  # Should be in E.164 format

# Timestamp type (can be string or datetime)
Timestamp = Union[str, datetime]

# Message direction
MessageDirection = str  # "incoming" or "outgoing"

# Call direction
CallDirection = str  # "incoming" or "outgoing"

# Status types
MessageStatus = str  # "sent", "delivered", "failed", etc.
CallStatus = str  # "completed", "missed", "busy", etc.
WebhookStatus = str  # "enabled", "disabled"

# Webhook events
WebhookEvent = str  # "message.received", "message.sent", etc.

# Contact source
ContactSource = str  # "public-api", "import", etc.

# Custom field types
CustomFieldType = str  # "text", "number", "date", "multi-select", etc.
CustomFieldValue = Union[str, int, float, List[str], bool, None]

# Pagination
PageToken = Optional[str]
MaxResults = Optional[int]
