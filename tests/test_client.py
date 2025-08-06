"""
Basic tests for the OpenPhone Python SDK.
"""

import pytest
from openphone_python import OpenPhoneClient
from openphone_python.exceptions import InvalidApiKeyError


def test_client_initialization():
    """Test client initialization with valid API key."""
    client = OpenPhoneClient(api_key="test_api_key")
    assert client.base_url == "https://api.openphone.com/v1"
    assert client.version == "0.1.0"


def test_client_invalid_api_key():
    """Test client initialization with invalid API key."""
    with pytest.raises(InvalidApiKeyError):
        OpenPhoneClient(api_key="")

    with pytest.raises(InvalidApiKeyError):
        OpenPhoneClient(api_key=None)


def test_client_custom_base_url():
    """Test client with custom base URL."""
    custom_url = "https://custom.api.com/v1"
    client = OpenPhoneClient(api_key="test_key", base_url=custom_url)
    assert client.base_url == custom_url


def test_lazy_resource_loading():
    """Test that resources are lazily loaded."""
    client = OpenPhoneClient(api_key="test_key")

    # Resources should not be initialized yet
    assert client._messages is None
    assert client._contacts is None

    # Accessing should initialize them
    messages = client.messages
    assert client._messages is not None
    assert messages is client.messages  # Should return same instance

    contacts = client.contacts
    assert client._contacts is not None
    assert contacts is client.contacts  # Should return same instance


def test_client_repr():
    """Test client string representation."""
    client = OpenPhoneClient(api_key="test_key")
    assert "OpenPhoneClient" in repr(client)
    assert "https://api.openphone.com/v1" in repr(client)


if __name__ == "__main__":
    pytest.main([__file__])
