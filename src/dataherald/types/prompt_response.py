# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PromptResponse", "Metadata", "MetadataDhInternal", "MetadataDhInternalSlackInfo"]


class MetadataDhInternalSlackInfo(BaseModel):
    channel_id: Optional[str] = None

    thread_ts: Optional[str] = None

    user_id: Optional[str] = None

    username: Optional[str] = None


class MetadataDhInternal(BaseModel):
    created_by: Optional[str] = None

    display_id: Optional[str] = None

    generation_status: Optional[
        Literal["INITIALIZED", "IN_PROGRESS", "NOT_VERIFIED", "VERIFIED", "ERROR", "REJECTED"]
    ] = None
    """An enumeration."""

    message: Optional[str] = None

    organization_id: Optional[str] = None

    slack_info: Optional[MetadataDhInternalSlackInfo] = None

    updated_by: Optional[str] = None


class Metadata(BaseModel):
    dh_internal: Optional[MetadataDhInternal] = None


class PromptResponse(BaseModel):
    id: str

    db_connection_id: str

    text: str

    created_at: Optional[datetime] = None

    metadata: Optional[Metadata] = None
