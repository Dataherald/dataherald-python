# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SqlGenerationResponse", "Metadata", "MetadataDhInternal"]


class MetadataDhInternal(BaseModel):
    organization_id: Optional[str] = None


class Metadata(BaseModel):
    dh_internal: Optional[MetadataDhInternal] = None


class SqlGenerationResponse(BaseModel):
    id: Optional[str] = None

    completed_at: Optional[datetime] = None

    confidence_score: Optional[float] = None

    created_at: Optional[datetime] = None

    error: Optional[str] = None

    finetuning_id: Optional[str] = None

    metadata: Optional[Metadata] = None

    prompt_id: Optional[str] = None

    sql: Optional[str] = None

    status: Optional[Literal["VALID", "INVALID"]] = None
    """An enumeration."""

    tokens_used: Optional[int] = None
