"""
Example usage of the OpenPhone Python SDK.
"""

import os
from openphone_python import OpenPhoneClient
from openphone_python.exceptions import (
    AuthenticationError,
    RateLimitError,
    ValidationError,
    NotFoundError,
    ApiError,
)


def main():
    """Example usage of the OpenPhone Python SDK."""

    # Initialize client (replace with your actual API key)
    api_key = os.getenv("OPENPHONE_API_KEY", "your_api_key_here")

    if api_key == "your_api_key_here":
        print(
            "Please set the OPENPHONE_API_KEY environment variable or update the api_key variable"
        )
        return

    try:
        client = OpenPhoneClient(api_key=api_key)
        print(f"Initialized OpenPhone client: {client}")

        # Example: List phone numbers
        print("\n--- Listing Phone Numbers ---")
        phone_numbers = client.phone_numbers.get_all()
        for phone_number in phone_numbers:
            print(f"Phone Number: {phone_number.number} (ID: {phone_number.id})")

        if not phone_numbers:
            print(
                "No phone numbers found. You need at least one phone number to send messages."
            )
            return

        # Use the first phone number for examples
        phone_number = phone_numbers[0]

        # Example: List recent messages
        print(f"\n--- Recent Messages for {phone_number.number} ---")
        try:
            messages = list(
                client.messages.list(
                    phone_number_id=phone_number.id,
                    participants=["+15555555678"],  # Replace with actual number
                    max_results=5,
                )
            )

            for message in messages:
                print(f"Message: {message.text[:50]}... (Status: {message.status})")
        except Exception as e:
            print(f"Error listing messages: {e}")

        # Example: List contacts
        print("\n--- Listing Contacts ---")
        try:
            contacts = list(client.contacts.list(max_results=5))
            for contact in contacts:
                name = f"{contact.default_fields.first_name or ''} {contact.default_fields.last_name or ''}".strip()
                print(f"Contact: {name or 'No name'} (ID: {contact.id})")
        except Exception as e:
            print(f"Error listing contacts: {e}")

        # NEW: List contact custom fields
        print("\n--- Listing Contact Custom Fields ---")
        try:
            custom_fields = client.contact_custom_fields.list()
            for field in custom_fields:
                print(f"Custom Field: {field.name} (Type: {field.field_type})")
        except Exception as e:
            print(f"Error listing contact custom fields: {e}")

        # Example: List conversations with enhanced filtering
        print("\n--- Listing Conversations ---")
        try:
            conversations = list(
                client.conversations.list(
                    phone_numbers=[phone_number.id], max_results=3
                )
            )
            for conversation in conversations:
                print(
                    f"Conversation: {conversation.name or 'No name'} (ID: {conversation.id})"
                )
        except Exception as e:
            print(f"Error listing conversations: {e}")

        # Example: List calls
        print(f"\n--- Recent Calls for {phone_number.number} ---")
        try:
            calls = list(
                client.calls.list(
                    phone_number_id=phone_number.id,
                    participants=["+15555555678"],  # Replace with actual number
                    max_results=3,
                )
            )
            for call in calls:
                print(f"Call: {call.direction} - Status: {call.status} (ID: {call.id})")

                # NEW: Try to get call recording, summary, and transcript
                try:
                    recording = client.call_recordings.get(call.id)
                    print(f"  Recording available: {recording.status}")
                except NotFoundError:
                    print("  No recording available")
                except Exception as e:
                    print(f"  Recording error: {e}")

                try:
                    summary = client.call_summaries.get(call.id)
                    print(f"  Summary status: {summary.status}")
                except NotFoundError:
                    print("  No summary available")
                except Exception as e:
                    print(f"  Summary error: {e}")

        except Exception as e:
            print(f"Error listing calls: {e}")

        # Example: List webhooks
        print("\n--- Listing Webhooks ---")
        try:
            webhooks = client.webhooks.get_all()
            for webhook in webhooks:
                print(
                    f"Webhook: {webhook.label} ({webhook.url}) - Status: {webhook.status}"
                )
                print(f"  Events: {', '.join(webhook.events)}")

            # Example: Create different types of webhooks (commented out to avoid actual creation)
            print("\n--- Webhook Creation Examples ---")

            print("# Smart routing with generic create() method:")
            print("# webhook = client.webhooks.create({")
            print("#     'url': 'https://your-app.com/webhooks',")
            print("#     'events': ['message.received', 'message.delivered'],")
            print("#     'label': 'Auto-routed Message Webhook'")
            print("# })  # Automatically routes to /webhooks/messages")
            print()

            print("# Or use specialized methods for more control:")
            print("# message_webhook = client.webhooks.create_message_webhook(")
            print("#     url='https://your-app.com/webhooks/messages',")
            print("#     events=['message.received', 'message.delivered'],")
            print("#     label='My Message Webhook'")
            print("# )")

            print("# call_webhook = client.webhooks.create_call_webhook(")
            print("#     url='https://your-app.com/webhooks/calls',")
            print("#     events=['call.completed', 'call.ringing'],")
            print("#     label='My Call Webhook'")
            print("# )")

            print("# summary_webhook = client.webhooks.create_call_summary_webhook(")
            print("#     url='https://your-app.com/webhooks/call-summaries',")
            print("#     label='My Call Summary Webhook'")
            print("# )")

            print("# Create call transcript webhook:")
            print("# transcript_webhook = client.webhooks.create_call_transcript_webhook(")
            print("#     url='https://your-app.com/webhooks/call-transcripts',")
            print("#     label='My Call Transcript Webhook'")
            print("# )")

        except Exception as e:
            print(f"Error listing webhooks: {e}")

    except AuthenticationError:
        print("Authentication failed. Please check your API key.")
    except RateLimitError as e:
        print(f"Rate limit exceeded. Retry after: {e.retry_after} seconds")
    except ApiError as e:
        print(f"API Error {e.status_code}: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
