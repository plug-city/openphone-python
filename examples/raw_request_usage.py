"""
Example usage of the raw request utilities for direct OpenPhone API access.

This example shows how to use the simple raw_request utilities to make
direct API calls without any SDK model processing.
"""

import os
import requests
from openphone_python.utils import raw_request, raw_request_with_response_object


def example_raw_requests():
    """Examples of using the raw request utilities."""
    # Get API key from environment
    api_key = os.getenv("OPENPHONE_API_KEY")
    if not api_key:
        print("Please set OPENPHONE_API_KEY environment variable")
        return

    print("=== Raw Request Examples ===\n")

    # Example 1: Simple GET request for contacts
    print("1. Listing contacts with raw_request():")
    try:
        response = raw_request(
            api_key=api_key,
            endpoint="contacts",
            params={"maxResults": 5}
        )
        print(f"Response type: {type(response)}")
        print(f"Keys in response: {list(response.keys())}")
        print(f"Number of contacts: {len(response.get('data', []))}")
        print()
    except (requests.RequestException, ValueError) as e:
        print(f"Error: {e}\n")

    # Example 2: Using the response object version
    print("2. Getting response object with raw_request_with_response_object():")
    try:
        response = raw_request_with_response_object(
            api_key=api_key,
            endpoint="contacts",
            params={"maxResults": 3}
        )
        print(f"Status code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print(f"Response type: {type(response)}")

        # Parse JSON yourself
        data = response.json()
        print(f"Parsed data keys: {list(data.keys())}")
        print()
    except (requests.RequestException, ValueError) as e:
        print(f"Error: {e}\n")

    # Example 3: Different endpoint
    print("3. Getting messages:")
    try:
        response = raw_request(
            api_key=api_key,
            endpoint="messages",
            params={"maxResults": 2}
        )
        print(f"Messages response keys: {list(response.keys())}")
        if 'data' in response:
            print(f"Number of messages: {len(response['data'])}")
        print()
    except (requests.RequestException, ValueError) as e:
        print(f"Error: {e}\n")

    print("=== End Examples ===")


if __name__ == "__main__":
    example_raw_requests()
