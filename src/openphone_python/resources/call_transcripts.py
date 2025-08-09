"""
Call Transcripts resource for the OpenPhone Python SDK.
"""

from typing import Optional
from openphone_python.models.call_transcript import CallTranscript
from openphone_python.resources.base import BaseResource


class CallTranscriptsResource(BaseResource):
    """
    Handle call transcript-related API operations.

    Endpoints covered:
    - GET /v1/call-transcripts/{id} (Get call transcript)
    """

    def get(self, transcript_id: str) -> CallTranscript:
        """
        Get a call transcript by transcript ID.

        Args:
            transcript_id: The unique identifier of the transcript

        Returns:
            CallTranscript instance

        Raises:
            NotFoundError: If the transcript is not found
            UnauthorizedError: If authentication fails
            ForbiddenError: If access to the transcript is forbidden
        """
        response = self._get(f"call-transcripts/{transcript_id}")
        return CallTranscript(response)
