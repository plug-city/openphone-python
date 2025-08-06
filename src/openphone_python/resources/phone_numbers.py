"""
Phone numbers resource for the OpenPhone Python SDK.
"""

from typing import List, Optional, Iterator
from openphone_python.models.phone_number import PhoneNumber
from openphone_python.resources.base import BaseResource


class PhoneNumbersResource(BaseResource):
    """
    Handle all phone number-related API operations.

    Endpoints covered:
    - GET /v1/phone-numbers (List phone numbers)
    """

    def list(self, user_id: Optional[str] = None, **kwargs) -> Iterator[PhoneNumber]:
        """
        List phone numbers.

        Args:
            user_id: Optional user ID filter
            **kwargs: Additional parameters

        Returns:
            Iterator yielding PhoneNumber instances
        """
        params = {}

        if user_id:
            params["userId"] = user_id

        # Add any additional parameters
        params.update(kwargs)

        return self._paginate("phone-numbers", PhoneNumber, params)

    def get_all(self, user_id: Optional[str] = None) -> List[PhoneNumber]:
        """
        Get all phone numbers as a list.

        Args:
            user_id: Optional user ID filter

        Returns:
            List of PhoneNumber instances
        """
        return list(self.list(user_id=user_id))
