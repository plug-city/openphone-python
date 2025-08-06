"""
Pagination utilities for the OpenPhone Python SDK.
"""

from typing import Iterator, Dict, Any, Optional, Type, TYPE_CHECKING

if TYPE_CHECKING:
    from openphone_python.resources.base import BaseResource
    from openphone_python.models.base import BaseModel


class PaginatedResult:
    """
    Handle paginated API responses.

    Principles:
    - Lazy loading of pages
    - Iterator interface for easy consumption
    - Automatic page token management
    """

    def __init__(
        self,
        resource: "BaseResource",
        endpoint: str,
        params: Dict[str, Any],
        model_class: Type["BaseModel"],
    ):
        self.resource = resource
        self.endpoint = endpoint
        self.params = params.copy()
        self.model_class = model_class
        self._current_items: list = []
        self._current_index = 0
        self._next_page_token: Optional[str] = None
        self._has_more = True
        self._total_items: Optional[int] = None

    def __iter__(self) -> Iterator["BaseModel"]:
        """Return iterator."""
        return self

    def __next__(self) -> "BaseModel":
        """Get next item."""
        # If we've exhausted current items, try to load next page
        if self._current_index >= len(self._current_items):
            if not self._has_more:
                raise StopIteration

            self._load_next_page()

            # If still no items after loading, we're done
            if self._current_index >= len(self._current_items):
                raise StopIteration

        item = self._current_items[self._current_index]
        self._current_index += 1
        return self.model_class(item)

    def _load_next_page(self) -> None:
        """Load the next page of results."""
        if not self._has_more:
            return

        # Set up pagination parameters
        request_params = self.params.copy()
        if self._next_page_token:
            request_params["pageToken"] = self._next_page_token

        # Make the API call
        response = self.resource._request("GET", self.endpoint, params=request_params)

        # Extract data
        data = response.get("data", [])
        self._current_items.extend(data)

        # Update pagination state
        self._next_page_token = response.get("nextPageToken")
        self._has_more = bool(self._next_page_token)

        # Store total items if available
        if "totalItems" in response:
            self._total_items = response["totalItems"]

    @property
    def total_items(self) -> Optional[int]:
        """Get total number of items if available."""
        return self._total_items

    def to_list(self, limit: Optional[int] = None) -> list:
        """
        Convert to list, optionally limiting the number of items.

        Args:
            limit: Maximum number of items to return

        Returns:
            List of model instances
        """
        items = []
        count = 0

        for item in self:
            items.append(item)
            count += 1

            if limit is not None and count >= limit:
                break

        return items
