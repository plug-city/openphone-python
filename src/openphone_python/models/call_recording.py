"""
Call Recording model for the OpenPhone Python SDK.
"""

from typing import Dict, Any, Optional
from openphone_python.models.base import BaseModel


class CallRecording(BaseModel):
    """
    Represents a call recording in OpenPhone.
    """

    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)

    @property
    def call_id(self) -> str:
        """Get the call ID associated with this recording."""
        return self._get_field("callId")

    @property
    def recording_url(self) -> Optional[str]:
        """Get the URL to download the recording."""
        return self._get_field("recordingUrl")

    @property
    def duration(self) -> Optional[int]:
        """Get the duration of the recording in seconds."""
        return self._get_field("duration")

    @property
    def file_size(self) -> Optional[int]:
        """Get the file size of the recording in bytes."""
        return self._get_field("fileSize")

    @property
    def created_at(self) -> Optional[str]:
        """Get when the recording was created."""
        return self._get_field("createdAt")

    @property
    def status(self) -> Optional[str]:
        """Get the status of the recording."""
        return self._get_field("status")

    def __repr__(self) -> str:
        """String representation of the call recording."""
        return f"CallRecording(call_id='{self.call_id}', status='{self.status}')"
