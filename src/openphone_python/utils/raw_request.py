"""
Raw API request utility for the OpenPhone Python SDK.

Simple utility for making direct API calls when you need raw responses.
"""

from typing import Dict, Any, Optional
import requests
import logging
from openphone_python.auth.api_key import ApiKeyAuth
from openphone_python.utils.validation import validate_api_response

logger = logging.getLogger(__name__)


def raw_request(
    api_key: str,
    endpoint: str,
    method: str = "GET",
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    base_url: str = "https://api.openphone.com/v1",
    timeout: int = 30
) -> Dict[str, Any]:
    """
    Make a raw API request to OpenPhone with authentication.

    Simple utility for when you need direct access to API responses
    without any SDK processing or model parsing.

    Args:
        api_key: OpenPhone API key
        endpoint: API endpoint (e.g., "contacts", "messages", "calls/{id}")
        method: HTTP method (GET, POST, PUT, PATCH, DELETE)
        params: Query parameters as dictionary
        data: Request body data as dictionary (for POST/PUT/PATCH)
        base_url: OpenPhone API base URL
        timeout: Request timeout in seconds (default: 30)

    Returns:
        Parsed JSON response as dictionary

    Raises:
        requests.RequestException: On network errors

    Examples:
        # List contacts
        response = raw_request("api_key", "contacts", params={"maxResults": 10})

        # Get single contact
        response = raw_request("api_key", "contacts/CNT123")

        # Create contact
        contact_data = {"defaultFields": {"firstName": "John"}}
        response = raw_request("api_key", "contacts", "POST", data=contact_data)

        # Update contact
        update_data = {"defaultFields": {"firstName": "Jane"}}
        response = raw_request("api_key", "contacts/CNT123", "PATCH", data=update_data)
    """
    # Set up authentication
    auth = ApiKeyAuth(api_key)

    # Build URL
    url = f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"

    # Set up headers
    headers = auth.get_headers()
    headers.update({
        "Content-Type": "application/json",
        "User-Agent": "openphone-python-raw-util/1.0"
    })

    # Log the request
    logger.debug("Raw API Request: %s %s | Params: %s | Data: %s", method, url, params, data)

    try:
        # Make the request
        response = requests.request(
            method=method.upper(),
            url=url,
            params=params,
            json=data,
            headers=headers,
            timeout=timeout
        )

        # Log the response
        content_preview = response.text[:500] + "..." if len(response.text) > 500 else response.text
        logger.debug("Raw API Response: %s | Content: %s", response.status_code, content_preview)

        # Validate and return parsed response
        return validate_api_response(response)

    except requests.RequestException as e:
        logger.error("Raw API request failed: %s", e)
        raise
    except Exception as e:
        logger.error("Unexpected error in raw API request: %s", e)
        raise


def raw_request_with_response_object(
    api_key: str,
    endpoint: str,
    method: str = "GET",
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    base_url: str = "https://api.openphone.com/v1",
    timeout: int = 30
) -> requests.Response:
    """
    Make a raw API request and return the full Response object.

    Alternative to raw_request() that returns the full requests.Response
    object instead of parsed JSON. Useful when you need access to headers,
    status codes, or want to handle parsing yourself.

    Args:
        api_key: OpenPhone API key
        endpoint: API endpoint (e.g., "contacts", "messages", "calls/{id}")
        method: HTTP method (GET, POST, PUT, PATCH, DELETE)
        params: Query parameters as dictionary
        data: Request body data as dictionary (for POST/PUT/PATCH)
        base_url: OpenPhone API base URL
        timeout: Request timeout in seconds (default: 30)

    Returns:
        Full requests.Response object

    Examples:
        # Get response object
        response = raw_request_with_response_object("api_key", "contacts")
        print(response.status_code)
        print(response.headers)
        print(response.json())  # Parse yourself
    """
    # Set up authentication
    auth = ApiKeyAuth(api_key)

    # Build URL
    url = f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"

    # Set up headers
    headers = auth.get_headers()
    headers.update({
        "Content-Type": "application/json",
        "User-Agent": "openphone-python-raw-util/1.0"
    })

    # Log the request
    logger.debug("Raw API Request (response object): %s %s | Params: %s | Data: %s",
                method, url, params, data)

    try:
        # Make the request and return full response object
        response = requests.request(
            method=method.upper(),
            url=url,
            params=params,
            json=data,
            headers=headers,
            timeout=timeout
        )

        # Log the response
        logger.debug("Raw API Response (response object): %s", response.status_code)

        return response

    except requests.RequestException as e:
        logger.error("Raw API request (response object) failed: %s", e)
        raise
    except Exception as e:
        logger.error("Unexpected error in raw API request (response object): %s", e)
        raise
