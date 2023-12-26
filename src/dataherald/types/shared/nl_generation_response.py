# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["NlGenerationResponse", "Metadata", "MetadataDataheraldInternal"]


class MetadataDataheraldInternal(BaseModel):
    organization_id: Optional[str] = None


class Metadata(BaseModel):
    dataherald_internal: Optional[MetadataDataheraldInternal] = None


class NlGenerationResponse(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    metadata: Optional[Metadata] = None

    sql_generation_id: Optional[str] = None

    text: Optional[str] = None
