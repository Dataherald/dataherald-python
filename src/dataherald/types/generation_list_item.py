# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GenerationListItem"]


class GenerationListItem(BaseModel):
    id: str

    created_by: str

    prompt_text: str

    confidence_score: Optional[float] = None

    created_at: Optional[datetime] = None

    display_id: Optional[str] = None

    nl_generation_text: Optional[str] = None

    status: Optional[Literal["INITIALIZED", "IN_PROGRESS", "NOT_VERIFIED", "VERIFIED", "ERROR", "REJECTED"]] = None
    """An enumeration."""
