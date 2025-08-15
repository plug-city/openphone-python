"""
Example usage of raw request functionality - both standalone utilities and client methods.

This example shows different ways to make direct API calls without SDK model processing.
"""

import os
import requests
from openphone_python import OpenPhoneClient
from openphone_python.utils import raw_request, raw_request_with_response_object


def example_standalone_raw_requests():
    """Examples using standalone raw request utilities."""
    api_key = os.getenv("OPENPHONE_API_KEY")
    if not api_key:
        print("Please set OPENPHONE_API_KEY environment variable")
        return

    print("=== Standalone Raw Request Utilities ===\n")

    try:
        # Using standalone utility functions
        response = raw_request(
            api_key=api_key,
            endpoint="contacts",
            params={"maxResults": 3}
        )
        print(f"Standalone raw_request: {len(response.get('data', []))} contacts")

        response_obj = raw_request_with_response_object(
            api_key=api_key,
            endpoint="messages",
            params={"maxResults": 2}
        )
        print(f"Standalone response object: Status {response_obj.status_code}")
        print()

    except (requests.RequestException, ValueError) as e:
        print(f"Standalone error: {e}\n")


def example_client_raw_requests():
    """Examples using client raw request methods."""
    api_key = os.getenv("OPENPHONE_API_KEY")
    if not api_key:
        print("Please set OPENPHONE_API_KEY environment variable")
        return

    print("=== Client Raw Request Methods ===\n")

    try:
        # Create client instance
        client = OpenPhoneClient(api_key=api_key)

        # Using client methods - cleaner syntax!
        response = client.raw_request(
            endpoint="contacts",
            params={"maxResults": 3}
        )
        print(f"Client raw_request: {len(response.get('data', []))} contacts")

        response_obj = client.raw_request_with_response_object(
            endpoint="messages",
            params={"maxResults": 2}
        )
        print(f"Client response object: Status {response_obj.status_code}")

        # Example with POST request
        print("\nTesting POST request structure (won't actually create):")
        contact_data = {
            "defaultFields": {
                "firstName": "Test",
                "lastName": "User"
            }
        }
        print(f"Would POST: {contact_data}")
        print()

    except (requests.RequestException, ValueError) as e:
        print(f"Client error: {e}\n")


def compare_approaches():
    """Compare different approaches for making raw requests."""
    api_key = os.getenv("OPENPHONE_API_KEY")
    if not api_key:
        print("Please set OPENPHONE_API_KEY environment variable")
        return

    print("=== Comparison of Approaches ===\n")

    print("1. Standalone utility:")
    print("   raw_request(api_key='...', endpoint='contacts')")
    print("   ✓ Direct function call")
    print("   ✓ No client instance needed")
    print()

    print("2. Client method:")
    print("   client = OpenPhoneClient(api_key='...')")
    print("   client.raw_request(endpoint='contacts')")
    print("   ✓ Cleaner syntax (no api_key repetition)")
    print("   ✓ Consistent with SDK patterns")
    print("   ✓ Same client instance for regular and raw requests")
    print()

    print("3. Mixed usage:")
    print("   client = OpenPhoneClient(api_key='...')")
    print("   # Use SDK models for common operations")
    print("   contacts = client.contacts.list()")
    print("   # Use raw requests for special cases")
    print("   custom_data = client.raw_request('custom-endpoint')")
    print("   ✓ Best of both worlds!")


if __name__ == "__main__":
    example_standalone_raw_requests()
    example_client_raw_requests()
    compare_approaches()
