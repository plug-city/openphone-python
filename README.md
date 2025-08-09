# OpenPhone Python SDK

A comprehensive Python SDK for integrating with the [OpenPhone API](https://www.openphone.com/docs/mdx/api-reference/introduction). This package provides a simple and intuitive interface for managing messages, contacts, phone numbers, calls, and webhooks.

## Features

- **Complete API Coverage**: Supports all OpenPhone API endpoints
- **Type Safety**: Full type hints and runtime validation
- **Automatic Pagination**: Seamless handling of paginated responses
- **Phone Number Validation**: Built-in E.164 formatting and validation
- **Error Handling**: Comprehensive exception handling with specific error types
- **Extensible Architecture**: Easy to extend and customize

## Installation

Install using pip:

```bash
pip install openphone-python
```

Or using uv:

```bash
uv add openphone-python
```

## Quick Start

```python
from openphone_python import OpenPhoneClient

# Initialize the client
client = OpenPhoneClient(api_key="your_api_key_here")

# Send a message
message = client.messages.send(
    content="Hello from OpenPhone!",
    from_number="+15555551234",
    to_numbers=["+15555555678"]
)

# List messages
for message in client.messages.list(
    phone_number_id="PN123abc",
    participants=["+15555555678"]
):
    print(f"Message: {message.text} (Status: {message.status})")

# Create a contact
contact = client.contacts.create({
    "defaultFields": {
        "firstName": "John",
        "lastName": "Doe",
        "company": "Example Corp"
    },
    "externalId": "external_123"
})
```

## Authentication

The OpenPhone API uses API key authentication. You can generate an API key from your OpenPhone workspace settings:

1. Log in to your OpenPhone account
2. Navigate to "API" tab under workspace settings
3. Click "Generate API key" and provide a descriptive label
4. Include the key in the Authorization header: `Authorization: YOUR_API_KEY`

**Note**: You need workspace owner or admin privileges to access the API settings.

## API Reference

### Messages

```python
# Send a message
message = client.messages.send(
    content="Hello!",
    from_number="+15555551234",
    to_numbers=["+15555555678"],
    user_id="optional_user_id"
)

# List messages with pagination
messages = client.messages.list(
    phone_number_id="PN123abc",
    participants=["+15555555678"],
    max_results=50
)

# Get a specific message
message = client.messages.get("message_id")
```

### Contacts

```python
# List contacts
contacts = client.contacts.list(max_results=25)

# Create a contact
contact = client.contacts.create({
    "defaultFields": {
        "firstName": "Jane",
        "lastName": "Smith",
        "emails": [{"name": "work", "value": "jane@example.com"}]
    }
})

# Update a contact
updated_contact = client.contacts.update("contact_id", {
    "defaultFields": {"company": "New Company"}
})

# Delete a contact
client.contacts.delete("contact_id")
```

### Phone Numbers

```python
# List all phone numbers
phone_numbers = client.phone_numbers.get_all()

# List phone numbers for a specific user
user_numbers = list(client.phone_numbers.list(user_id="US123abc"))
```

### Calls

```python
# List calls
calls = client.calls.list(
    phone_number_id="PN123abc",
    participants=["+15555555678"],
    created_after="2024-01-01T00:00:00Z"
)

# Get a specific call
call = client.calls.get("call_id")
```

### Webhooks

```python
# List webhooks
webhooks = client.webhooks.get_all()

# Smart webhook creation - automatically routes to correct endpoint
webhook = client.webhooks.create({
    "url": "https://your-domain.com/webhook",
    "events": ["message.received", "message.delivered"],
    "label": "My Webhook"
})  # Automatically uses /v1/webhooks/messages endpoint

# Create call webhook - routes to /v1/webhooks/calls
call_webhook = client.webhooks.create({
    "url": "https://your-domain.com/webhook",
    "events": ["call.completed", "call.ringing"],
    "label": "Call Events"
})

# Or use specialized methods for explicit control
message_webhook = client.webhooks.create_message_webhook(
    url="https://your-domain.com/webhook",
    events=["message.received"],
    label="Message Webhook"
)

# Update a webhook
updated_webhook = client.webhooks.update("webhook_id", {
    "status": "disabled"
})

# Delete a webhook
client.webhooks.delete("webhook_id")
```

## Error Handling

The SDK provides specific exception types for different error conditions:

```python
from openphone_python import OpenPhoneClient
from openphone_python.exceptions import (
    AuthenticationError,
    RateLimitError,
    ValidationError,
    NotFoundError,
    ApiError
)

try:
    client = OpenPhoneClient(api_key="your_api_key")
    message = client.messages.send(
        content="Hello!",
        from_number="+15555551234",
        to_numbers=["+15555555678"]
    )
except AuthenticationError:
    print("Invalid API key or authentication failed")
except RateLimitError as e:
    print(f"Rate limit exceeded. Retry after: {e.retry_after} seconds")
except ValidationError as e:
    print(f"Validation error: {e}")
except NotFoundError:
    print("Resource not found")
except ApiError as e:
    print(f"API error {e.status_code}: {e}")
```

## Phone Number Formatting

The SDK automatically handles phone number formatting to E.164 format:

```python
from openphone_python.utils import ensure_e164_format, is_valid_phone_number

# Format phone number
formatted = ensure_e164_format("(555) 123-4567")  # Returns "+15551234567"

# Validate phone number
is_valid = is_valid_phone_number("+15551234567")  # Returns True
```

## Development

### Setting up the development environment

```bash
# Clone the repository
git clone https://github.com/plug-city/openphone-python.git
cd openphone-python

# Install dependencies with uv
uv sync --dev

# Install pre-commit hooks
uv run pre-commit install
```

### Running tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=openphone_python

# Run specific test file
uv run pytest tests/test_client.py
```

### Code formatting and linting

```bash
# Format code with black
uv run black src/ tests/

# Run linting with flake8
uv run flake8 src/ tests/

# Type checking with mypy
uv run mypy src/
```

## Requirements

- Python 3.11+
- An active OpenPhone subscription
- OpenPhone API key with appropriate permissions

## US Messaging Registration

To send text messages to US numbers via the API, you must complete US Carrier Registration. Learn more in the [OpenPhone documentation](https://support.openphone.com/hc/en-us/articles/15519949741463-Guide-to-US-carrier-registration-for-OpenPhone-customers).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Links

- [OpenPhone API Documentation](https://www.openphone.com/docs/mdx/api-reference/introduction)
- [OpenPhone Support](https://support.openphone.com/)
- [Issue Tracker](https://github.com/plug-city/openphone-python/issues)
