"""
Call Summaries resource for the OpenPhone Python SDK.
"""

from typing import Optional
from openphone_python.models.call_summary import CallSummary
from openphone_python.resources.base import BaseResource


class CallSummariesResource(BaseResource):
    """
    Handle call summary-related API operations.

    Endpoints covered:
    - GET /v1/call-summaries/{callId} (Get call summary)
    """

    def get(self, call_id: str) -> CallSummary:
        """
        Get a call summary by call ID.

        Args:
            call_id: The unique identifier of the call

        Returns:
            CallSummary instance

        Raises:
            NotFoundError: If the call or summary is not found
            BadRequestError: If the request is invalid
            ForbiddenError: If access to the summary is forbidden
        """
        response = self._get(f"call-summaries/{call_id}")
        return CallSummary(response)
