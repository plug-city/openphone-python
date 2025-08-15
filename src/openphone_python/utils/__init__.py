"""
Utilities module for the OpenPhone Python SDK.
"""

from .validation import (
    validate_phone_number,
    validate_email,
    validate_api_response,
    validate_pagination_params,
)
from .pagination import PaginatedResult
from .formatting import (
    format_phone_number,
    ensure_e164_format,
    format_phone_numbers_list,
    extract_country_code,
    is_valid_phone_number,
)
from .raw_request import (
    raw_request,
    raw_request_with_response_object,
)

__all__ = [
    "validate_phone_number",
    "validate_email",
    "validate_api_response",
    "validate_pagination_params",
    "PaginatedResult",
    "format_phone_number",
    "ensure_e164_format",
    "format_phone_numbers_list",
    "extract_country_code",
    "is_valid_phone_number",
    "raw_request",
    "raw_request_with_response_object",
]
