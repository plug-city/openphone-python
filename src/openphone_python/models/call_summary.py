"""
Call Summary model for the OpenPhone Python SDK.
"""

from typing import Dict, Any, Optional, List
from openphone_python.models.base import BaseModel


class CallSummary(BaseModel):
    """
    Represents a call summary in OpenPhone.
    """

    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)

    @property
    def call_id(self) -> str:
        """Get the call ID associated with this summary."""
        return self._get_field("callId")

    @property
    def summary(self) -> Optional[str]:
        """Get the AI-generated summary of the call."""
        return self._get_field("summary")

    @property
    def next_steps(self) -> Optional[str]:
        """Get the AI-generated next steps from the call."""
        return self._get_field("nextSteps")

    @property
    def status(self) -> str:
        """
        Get the status of the summary generation.

        Possible values: 'completed', 'processing', 'failed'
        """
        return self._get_field("status")

    @property
    def jobs(self) -> Optional[List[Dict[str, Any]]]:
        """Get the processing jobs associated with this summary."""
        return self._get_field("jobs")

    def __repr__(self) -> str:
        """String representation of the call summary."""
        return f"CallSummary(call_id='{self.call_id}', status='{self.status}')"
