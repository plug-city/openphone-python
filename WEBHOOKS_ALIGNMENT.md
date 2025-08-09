# Webhooks Resource - OpenAPI Alignment Summary

## Overview

The webhooks resource has been comprehensively updated to align with the OpenAPI 3.1.0 specification, adding specialized webhook creation endpoints and maintaining full backward compatibility.

## 🆕 New Features Added

### Specialized Webhook Creation Methods

#### 1. Message Webhooks (`create_message_webhook()`)
- **Endpoint**: `POST /v1/webhooks/messages`
- **Purpose**: Create webhooks for message events
- **Supported Events**:
  - `message.received`
  - `message.delivered`
- **Parameters**:
  - `url` (required): Webhook endpoint URL
  - `events` (required): List of message events
  - `resource_ids` (optional): Phone number IDs or ["*"] for all
  - `label` (optional): Webhook label
  - `status` (optional): enabled/disabled (default: enabled)
  - `user_id` (optional): User ID (defaults to workspace owner)

#### 2. Call Webhooks (`create_call_webhook()`)
- **Endpoint**: `POST /v1/webhooks/calls`
- **Purpose**: Create webhooks for call events
- **Supported Events**:
  - `call.completed`
  - `call.ringing`
  - `call.recording.completed`
- **Parameters**: Same as message webhooks

#### 3. Call Summary Webhooks (`create_call_summary_webhook()`)
- **Endpoint**: `POST /v1/webhooks/call-summaries`
- **Purpose**: Create webhooks for AI-generated call summaries
- **Supported Events**: `call.summary.completed` (automatically set)
- **Parameters**: Same as message webhooks (events parameter not needed)

#### 4. Call Transcript Webhooks (`create_call_transcript_webhook()`)
- **Endpoint**: `POST /v1/webhooks/call-transcripts`
- **Purpose**: Create webhooks for call transcription events
- **Supported Events**: `call.transcript.completed` (automatically set)
- **Parameters**: Same as message webhooks (events parameter not needed)

## 🔧 Enhanced Functionality

### Event Validation
- **Message Events**: Validates against `["message.received", "message.delivered"]`
- **Call Events**: Validates against `["call.completed", "call.ringing", "call.recording.completed"]`
- **Automatic Events**: Call summary and transcript webhooks automatically set appropriate events
- **Error Handling**: Raises `ValueError` for invalid event types

### Backward Compatibility
- **Maintained**: Original `create()` method still works
- **Deprecated Notice**: Clear deprecation message guiding users to new methods
- **No Breaking Changes**: Existing code continues to function

### Type Safety
- **Full Type Hints**: All parameters properly typed
- **Return Types**: All methods return `Webhook` instances
- **Optional Parameters**: Proper `Optional[]` typing for optional parameters

## 📊 OpenAPI Compliance Summary

### ✅ Fully Implemented Endpoints
1. `GET /v1/webhooks` - `list()` method
2. `GET /v1/webhooks/{id}` - `get()` method
3. `PUT /v1/webhooks/{id}` - `update()` method
4. `DELETE /v1/webhooks/{id}` - `delete()` method
5. `POST /v1/webhooks/messages` - `create_message_webhook()` method
6. `POST /v1/webhooks/calls` - `create_call_webhook()` method
7. `POST /v1/webhooks/call-summaries` - `create_call_summary_webhook()` method
8. `POST /v1/webhooks/call-transcripts` - `create_call_transcript_webhook()` method

### ✅ Model Compliance
All webhook model properties align with OpenAPI schema:
- `id`, `userId`, `orgId`, `label`, `status`, `url`, `key`
- `createdAt`, `updatedAt`, `deletedAt`, `events`, `resourceIds`

## 🚀 Usage Examples

### Creating Message Webhooks
```python
from openphone_python import OpenPhoneClient

client = OpenPhoneClient('your_api_key')

# Create message webhook
message_webhook = client.webhooks.create_message_webhook(
    url='https://your-app.com/webhooks/messages',
    events=['message.received', 'message.delivered'],
    resource_ids=['PN123abc'],  # Specific phone number
    label='My Message Webhook',
    status='enabled'
)
```

### Creating Call Webhooks
```python
# Create call webhook
call_webhook = client.webhooks.create_call_webhook(
    url='https://your-app.com/webhooks/calls',
    events=['call.completed', 'call.ringing'],
    resource_ids=['*'],  # All phone numbers
    label='My Call Webhook'
)
```

### Creating Summary/Transcript Webhooks
```python
# Create call summary webhook
summary_webhook = client.webhooks.create_call_summary_webhook(
    url='https://your-app.com/webhooks/summaries',
    label='Call Summaries',
    resource_ids=['PN123abc']
)

# Create call transcript webhook
transcript_webhook = client.webhooks.create_call_transcript_webhook(
    url='https://your-app.com/webhooks/transcripts',
    label='Call Transcripts'
)
```

### Backward Compatible Usage
```python
# Original method still works (deprecated)
webhook = client.webhooks.create({
    'url': 'https://your-app.com/webhook',
    'events': ['message.received'],
    'label': 'Legacy Webhook'
})
```

## 🧪 Validation & Testing

### Event Validation Testing
```python
# Valid events - works
client.webhooks.create_message_webhook(
    url='https://example.com',
    events=['message.received']
)

# Invalid events - raises ValueError
try:
    client.webhooks.create_message_webhook(
        url='https://example.com',
        events=['invalid.event']  # This will fail
    )
except ValueError as e:
    print(f"Validation error: {e}")
```

### Method Availability
```python
# All new methods are available
assert hasattr(client.webhooks, 'create_message_webhook')
assert hasattr(client.webhooks, 'create_call_webhook')
assert hasattr(client.webhooks, 'create_call_summary_webhook')
assert hasattr(client.webhooks, 'create_call_transcript_webhook')
```

## 📈 Benefits

1. **OpenAPI Compliance**: Fully aligned with official specification
2. **Event-Specific Creation**: Specialized methods for different webhook types
3. **Better Validation**: Event type validation prevents errors
4. **Improved UX**: Clear method names and parameters
5. **Type Safety**: Full type hint coverage
6. **Backward Compatibility**: Existing code continues to work
7. **Future-Proof**: Aligned with OpenPhone's API evolution

## 🔮 Migration Guide

### For New Users
- Use the specialized creation methods based on your webhook type
- Leverage built-in event validation
- Take advantage of comprehensive type hints

### For Existing Users
- **No immediate action needed** - existing code continues to work
- **Recommended**: Migrate to specialized methods for better validation and UX
- **Deprecation Notice**: Plan to migrate from generic `create()` method

### Migration Examples
```python
# Before (still works, but deprecated)
webhook = client.webhooks.create({
    'url': 'https://example.com',
    'events': ['message.received'],
    'label': 'My Webhook'
})

# After (recommended)
webhook = client.webhooks.create_message_webhook(
    url='https://example.com',
    events=['message.received'],
    label='My Webhook'
)
```

## ✅ Quality Assurance

- **✅ All endpoints implemented** according to OpenAPI spec
- **✅ Event validation** prevents invalid webhook configurations
- **✅ Type safety** with comprehensive type hints
- **✅ Backward compatibility** maintained
- **✅ Documentation** updated with examples
- **✅ Error handling** enhanced with specific validations
- **✅ Testing** comprehensive coverage of new functionality

The webhooks resource now provides complete OpenAPI compliance while maintaining the SDK's architectural principles and user-friendly interface.
