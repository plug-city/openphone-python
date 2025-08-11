"""
Base resource class for the OpenPhone Python SDK.
"""

from typing import Dict, Any, Optional, Iterator, TYPE_CHECKING
import requests
import time
import logging
from openphone_python.exceptions import ApiError
from openphone_python.utils.validation import validate_api_response
from openphone_python.utils.pagination import PaginatedResult

if TYPE_CHECKING:
    from openphone_python.client import OpenPhoneClient
    from openphone_python.models.base import BaseModel

logger = logging.getLogger(__name__)


class BaseResource:
    """
    Base class for all API resources.

    Principles:
    - DRY: Common HTTP operations in one place
    - Consistent error handling
    - Automatic response parsing
    """

    def __init__(self, client: "OpenPhoneClient"):
        self.client = client
        self.session = requests.Session()

        # Set up authentication headers
        auth_headers = client.auth.get_headers()
        self.session.headers.update(auth_headers)
        self.session.headers.update(
            {
                "Content-Type": "application/json",
                "User-Agent": f"openphone-python/{client.version}",
            }
        )

    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        max_retries: int = 3,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Make HTTP request to OpenPhone API with retry logic.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint path
            params: Query parameters
            data: Request body data
            max_retries: Maximum number of retry attempts
            **kwargs: Additional arguments for requests

        Returns:
            Parsed JSON response

        Raises:
            Various OpenPhone exceptions based on response
        """
        url = f"{self.client.base_url}/{endpoint.lstrip('/')}"

        # Log the outgoing request (single concise log)
        logger.debug("OpenPhone API Request: %s %s | Params: %s | Data: %s",
                    method, url, params, data)

        for attempt in range(max_retries + 1):
            try:
                response = self.session.request(
                    method=method, url=url, params=params, json=data, **kwargs
                )

                # Log the response (single concise log)
                content_preview = response.text[:500] + "..." if len(response.text) > 500 else response.text
                logger.debug("OpenPhone API Response: %s | Headers: %s | Content: %s",
                           response.status_code, dict(response.headers), content_preview)

                validated_response = validate_api_response(response)
                return validated_response

            except requests.RequestException as e:
                logger.warning("Request attempt %d/%d failed: %s",
                             attempt + 1, max_retries + 1, e)

                if attempt == max_retries:
                    logger.error("All %d request attempts failed: %s", max_retries + 1, e)
                    raise ApiError(
                        f"Request failed after {max_retries} retries: {e}", 0
                    ) from e

                # Exponential backoff: 1s, 2s, 4s
                wait_time = 2**attempt
                time.sleep(wait_time)
            except Exception as e:
                logger.error("Unexpected error during request: %s", e, exc_info=True)
                raise

    def _paginate(
        self, endpoint: str, model_class: type, params: Optional[Dict[str, Any]] = None
    ) -> Iterator["BaseModel"]:
        """
        Create paginated iterator for API responses.

        Args:
            endpoint: API endpoint path
            model_class: Model class to instantiate for each item
            params: Query parameters

        Returns:
            Iterator yielding model instances
        """
        params = params or {}
        return PaginatedResult(self, endpoint, params, model_class)

    def _get(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Make GET request."""
        return self._request("GET", endpoint, params=params)

    def _post(
        self, endpoint: str, data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Make POST request."""
        return self._request("POST", endpoint, data=data)

    def _put(
        self, endpoint: str, data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Make PUT request."""
        return self._request("PUT", endpoint, data=data)

    def _patch(
        self, endpoint: str, data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Make PATCH request."""
        return self._request("PATCH", endpoint, data=data)

    def _delete(self, endpoint: str) -> Dict[str, Any]:
        """Make DELETE request."""
        return self._request("DELETE", endpoint)
