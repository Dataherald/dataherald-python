# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FinetuningResponse", "BaseLlm", "Metadata", "MetadataDataheraldInternal"]


class BaseLlm(BaseModel):
    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)

    api_model_parameters: Optional[Dict[str, str]] = FieldInfo(alias="model_parameters", default=None)

    api_model_provider: Optional[str] = FieldInfo(alias="model_provider", default=None)


class MetadataDataheraldInternal(BaseModel):
    organization_id: Optional[str] = None


class Metadata(BaseModel):
    dataherald_internal: Optional[MetadataDataheraldInternal] = None


class FinetuningResponse(BaseModel):
    id: str

    api_model_id: Optional[str] = FieldInfo(alias="_model_id", default=None)

    base_llm: Optional[BaseLlm] = None

    created_at: Optional[datetime] = None

    db_connection_id: Optional[str] = None

    error: Optional[str] = None

    finetuning_file_id: Optional[str] = None

    finetuning_job_id: Optional[str] = None

    golden_records: Optional[List[str]] = None

    metadata: Optional[Metadata] = None

    status: Optional[str] = None
