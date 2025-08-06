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

        # Example: List webhooks
        print("\n--- Listing Webhooks ---")
        try:
            webhooks = client.webhooks.get_all()
            for webhook in webhooks:
                print(
                    f"Webhook: {webhook.label} ({webhook.url}) - Status: {webhook.status}"
                )
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
