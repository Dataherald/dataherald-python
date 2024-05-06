# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GenerationResponse", "SlackInfo"]


class SlackInfo(BaseModel):
    channel_id: Optional[str] = None

    thread_ts: Optional[str] = None

    user_id: Optional[str] = None

    username: Optional[str] = None


class GenerationResponse(BaseModel):
    id: str

    db_connection_id: str

    prompt_text: str

    confidence_score: Optional[float] = None

    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    display_id: Optional[str] = None

    message: Optional[str] = None

    nl_generation_text: Optional[str] = None

    organization_id: Optional[str] = None

    slack_info: Optional[SlackInfo] = None

    sql: Optional[str] = None

    sql_generation_error: Optional[str] = None

    status: Optional[Literal["INITIALIZED", "IN_PROGRESS", "NOT_VERIFIED", "VERIFIED", "ERROR", "REJECTED"]] = None
    """An enumeration."""

    updated_at: Optional[datetime] = None

    updated_by: Optional[str] = None
