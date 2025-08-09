"""
Call Transcript model for the OpenPhone Python SDK.
"""

from typing import Dict, Any, Optional, List
from openphone_python.models.base import BaseModel


class CallTranscript(BaseModel):
    """
    Represents a call transcript in OpenPhone.
    """

    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)

    @property
    def id(self) -> str:
        """Get the unique identifier of the transcript."""
        return self._get_field("id")

    @property
    def call_id(self) -> str:
        """Get the call ID associated with this transcript."""
        return self._get_field("callId")

    @property
    def transcript(self) -> Optional[str]:
        """Get the full transcript text."""
        return self._get_field("transcript")

    @property
    def segments(self) -> Optional[List[Dict[str, Any]]]:
        """
        Get the transcript segments with speaker information and timestamps.

        Each segment contains:
        - speaker: Speaker identifier
        - text: The spoken text
        - start_time: Start time in seconds
        - end_time: End time in seconds
        """
        return self._get_field("segments")

    @property
    def confidence(self) -> Optional[float]:
        """Get the confidence score of the transcription (0-1)."""
        return self._get_field("confidence")

    @property
    def language(self) -> Optional[str]:
        """Get the detected language of the call."""
        return self._get_field("language")

    @property
    def created_at(self) -> Optional[str]:
        """Get when the transcript was created."""
        return self._get_field("createdAt")

    @property
    def status(self) -> str:
        """
        Get the status of the transcript.

        Possible values: 'completed', 'processing', 'failed'
        """
        return self._get_field("status", "unknown")

    def __repr__(self) -> str:
        """String representation of the call transcript."""
        return f"CallTranscript(id='{self.id}', call_id='{self.call_id}', status='{self.status}')"
