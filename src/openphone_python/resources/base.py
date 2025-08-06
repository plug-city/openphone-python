"""
Base resource class for the OpenPhone Python SDK.
"""

from typing import Dict, Any, Optional, Iterator, TYPE_CHECKING
import requests
from openphone_python.exceptions import ApiError
from openphone_python.utils.validation import validate_api_response
from openphone_python.utils.pagination import PaginatedResult

if TYPE_CHECKING:
    from openphone_python.client import OpenPhoneClient
    from openphone_python.models.base import BaseModel


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
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Make HTTP request to OpenPhone API.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint path
            params: Query parameters
            data: Request body data
            **kwargs: Additional arguments for requests

        Returns:
            Parsed JSON response

        Raises:
            Various OpenPhone exceptions based on response
        """
        url = f"{self.client.base_url}/{endpoint.lstrip('/')}"

        try:
            response = self.session.request(
                method=method, url=url, params=params, json=data, **kwargs
            )

            return validate_api_response(response)

        except requests.RequestException as e:
            raise ApiError(f"Request failed: {e}", 0) from e

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
