"""
Call Recordings resource for the OpenPhone Python SDK.
"""

from typing import Optional
from openphone_python.models.call_recording import CallRecording
from openphone_python.resources.base import BaseResource


class CallRecordingsResource(BaseResource):
    """
    Handle call recording-related API operations.

    Endpoints covered:
    - GET /v1/call-recordings/{callId} (Get call recording)
    """

    def get(self, call_id: str) -> CallRecording:
        """
        Get a call recording by call ID.

        Args:
            call_id: The unique identifier of the call

        Returns:
            CallRecording instance

        Raises:
            NotFoundError: If the call or recording is not found
            ForbiddenError: If access to the recording is forbidden
        """
        response = self._get(f"call-recordings/{call_id}")
        return CallRecording(response)
