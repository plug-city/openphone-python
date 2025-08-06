"""
Validation utilities for the OpenPhone Python SDK.
"""

import re
from typing import Union
import phonenumbers
import requests
from openphone_python.exceptions import (
    ValidationError,
    ApiError,
    AuthenticationError,
    RateLimitError,
    ServerError,
    NotFoundError,
)


def validate_phone_number(phone_number: str) -> str:
    """
    Validate and format phone number to E.164 format.

    Args:
        phone_number: Phone number string

    Returns:
        Formatted phone number in E.164 format

    Raises:
        ValidationError: If phone number is invalid
    """
    if not phone_number or not isinstance(phone_number, str):
        raise ValidationError("Phone number must be a non-empty string")

    try:
        parsed = phonenumbers.parse(phone_number, None)
        if not phonenumbers.is_valid_number(parsed):
            raise ValidationError(f"Invalid phone number: {phone_number}")

        return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
    except phonenumbers.NumberParseException as e:
        raise ValidationError(f"Failed to parse phone number {phone_number}: {e}")


def validate_email(email: str) -> bool:
    """
    Validate email address format.

    Args:
        email: Email address string

    Returns:
        True if valid, False otherwise
    """
    if not email or not isinstance(email, str):
        return False

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def validate_api_response(response: requests.Response) -> dict:
    """
    Validate API response and handle errors.

    Args:
        response: HTTP response object

    Returns:
        Parsed JSON response

    Raises:
        Various OpenPhone exceptions based on status code
    """
    try:
        response_data = response.json()
    except ValueError:
        response_data = {}

    if response.status_code == 401:
        raise AuthenticationError("Invalid API key or authentication failed")
    elif response.status_code == 403:
        raise AuthenticationError("Access forbidden - check your permissions")
    elif response.status_code == 404:

        raise NotFoundError("Resource not found")
    elif response.status_code == 429:
        retry_after = response.headers.get("Retry-After")
        retry_after_int = (
            int(retry_after) if retry_after and retry_after.isdigit() else None
        )
        raise RateLimitError("Rate limit exceeded", retry_after=retry_after_int)
    elif response.status_code >= 500:

        raise ServerError(f"Server error: {response.status_code}")
    elif response.status_code >= 400:
        error_message = response_data.get("error", {}).get(
            "message", f"API error: {response.status_code}"
        )
        raise ApiError(error_message, response.status_code, response_data)

    return response_data


def validate_pagination_params(
    max_results: Union[int, None] = None, page_token: Union[str, None] = None
) -> dict:
    """
    Validate pagination parameters.

    Args:
        max_results: Maximum number of results per page
        page_token: Page token for pagination

    Returns:
        Dictionary of valid pagination parameters

    Raises:
        ValidationError: If parameters are invalid
    """
    params = {}

    if max_results is not None:
        if not isinstance(max_results, int) or max_results < 1 or max_results > 100:
            raise ValidationError("max_results must be an integer between 1 and 100")
        params["maxResults"] = max_results

    if page_token is not None:
        if not isinstance(page_token, str) or len(page_token.strip()) == 0:
            raise ValidationError("page_token must be a non-empty string")
        params["pageToken"] = page_token

    return params
