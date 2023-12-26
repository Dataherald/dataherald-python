# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FinetuningResponse", "BaseLlm", "Metadata", "MetadataDataheraldInternal"]


class BaseLlm(BaseModel):
    _model_name: Optional[str] = None

    _model_parameters: Optional[Dict[str, str]] = None

    _model_provider: Optional[str] = None


class MetadataDataheraldInternal(BaseModel):
    organization_id: Optional[str] = None


class Metadata(BaseModel):
    dataherald_internal: Optional[MetadataDataheraldInternal] = None


class FinetuningResponse(BaseModel):
    id: str

    _model_id: Optional[str] = None

    base_llm: Optional[BaseLlm] = None

    created_at: Optional[datetime] = None

    db_connection_id: Optional[str] = None

    error: Optional[str] = None

    finetuning_file_id: Optional[str] = None

    finetuning_job_id: Optional[str] = None

    golden_records: Optional[List[str]] = None

    metadata: Optional[Metadata] = None

    status: Optional[str] = None
