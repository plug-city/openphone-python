"""
Formatting utilities for the OpenPhone Python SDK.
"""

import phonenumbers
from typing import Optional
from openphone_python.exceptions import ValidationError


def format_phone_number(phone_number: str, format_type: str = "E164") -> str:
    """
    Format phone number to specified format.

    Args:
        phone_number: Phone number string
        format_type: Format type ('E164', 'INTERNATIONAL', 'NATIONAL', 'RFC3966')

    Returns:
        Formatted phone number

    Raises:
        ValidationError: If phone number is invalid or format type is unsupported
    """
    if not phone_number or not isinstance(phone_number, str):
        raise ValidationError("Phone number must be a non-empty string")

    try:
        parsed = phonenumbers.parse(phone_number, None)
        if not phonenumbers.is_valid_number(parsed):
            raise ValidationError(f"Invalid phone number: {phone_number}")

        format_map = {
            "E164": phonenumbers.PhoneNumberFormat.E164,
            "INTERNATIONAL": phonenumbers.PhoneNumberFormat.INTERNATIONAL,
            "NATIONAL": phonenumbers.PhoneNumberFormat.NATIONAL,
            "RFC3966": phonenumbers.PhoneNumberFormat.RFC3966,
        }

        if format_type not in format_map:
            raise ValidationError(f"Unsupported format type: {format_type}")

        return phonenumbers.format_number(parsed, format_map[format_type])

    except phonenumbers.NumberParseException as e:
        raise ValidationError(
            f"Failed to parse phone number {phone_number}: {e}"
        ) from e


def ensure_e164_format(phone_number: str) -> str:
    """
    Ensure phone number is in E.164 format.

    Args:
        phone_number: Phone number string

    Returns:
        Phone number in E.164 format
    """
    return format_phone_number(phone_number, "E164")


def format_phone_numbers_list(phone_numbers: list) -> list:
    """
    Format a list of phone numbers to E.164 format.

    Args:
        phone_numbers: List of phone number strings

    Returns:
        List of formatted phone numbers

    Raises:
        ValidationError: If any phone number is invalid
    """
    if not isinstance(phone_numbers, list):
        raise ValidationError("phone_numbers must be a list")

    formatted = []
    for i, phone_number in enumerate(phone_numbers):
        try:
            formatted.append(ensure_e164_format(phone_number))
        except ValidationError as e:
            raise ValidationError(f"Invalid phone number at index {i}: {e}") from e

    return formatted


def extract_country_code(phone_number: str) -> Optional[str]:
    """
    Extract country code from phone number.

    Args:
        phone_number: Phone number string

    Returns:
        Country code (e.g., 'US', 'CA') or None if unable to determine
    """
    try:
        parsed = phonenumbers.parse(phone_number, None)
        return phonenumbers.region_code_for_number(parsed)
    except phonenumbers.NumberParseException:
        return None


def is_valid_phone_number(phone_number: str) -> bool:
    """
    Check if phone number is valid.

    Args:
        phone_number: Phone number string

    Returns:
        True if valid, False otherwise
    """
    try:
        parsed = phonenumbers.parse(phone_number, None)
        return phonenumbers.is_valid_number(parsed)
    except (phonenumbers.NumberParseException, TypeError):
        return False
