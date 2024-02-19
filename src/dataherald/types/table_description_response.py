# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TableDescriptionResponse", "Column", "Metadata"]


class Column(BaseModel):
    categories: Optional[List[str]] = None

    data_type: Optional[str] = None

    description: Optional[str] = None

    foreign_key: Optional[object] = None

    is_primary_key: Optional[bool] = None

    low_cardinality: Optional[bool] = None

    name: Optional[str] = None


class Metadata(BaseModel):
    dh_internal: Optional[object] = None


class TableDescriptionResponse(BaseModel):
    id: str

    columns: Optional[List[Column]] = None

    created_at: Optional[datetime] = None

    db_connection_id: Optional[str] = None

    description: Optional[str] = None

    examples: Optional[List[object]] = None

    last_schema_sync: Optional[datetime] = None

    metadata: Optional[Metadata] = None

    status: Optional[Literal["NOT_SYNCHRONIZED", "SYNCHRONIZING", "SYNCHRONIZED", "DEPRECATED", "FAILED"]] = None
    """An enumeration."""

    table_name: Optional[str] = None
