# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["GoldenSqlResponse", "Metadata", "MetadataDhInternal"]


class MetadataDhInternal(BaseModel):
    display_id: Optional[str] = None

    organization_id: Optional[str] = None

    prompt_id: Optional[str] = None

    source: Optional[Literal["USER_UPLOAD", "VERIFIED_QUERY"]] = None
    """An enumeration."""


class Metadata(BaseModel):
    dh_internal: Optional[MetadataDhInternal] = None


class GoldenSqlResponse(BaseModel):
    id: str

    db_connection_id: str

    prompt_text: str

    sql: str

    created_at: Optional[datetime] = None

    metadata: Optional[Metadata] = None
