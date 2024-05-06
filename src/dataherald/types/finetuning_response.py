# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FinetuningResponse", "BaseLlm", "Metadata", "MetadataDhInternal"]


class BaseLlm(BaseModel):
    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)

    api_model_parameters: Optional[Dict[str, str]] = FieldInfo(alias="model_parameters", default=None)

    api_model_provider: Optional[str] = FieldInfo(alias="model_provider", default=None)


class MetadataDhInternal(BaseModel):
    organization_id: Optional[str] = None


class Metadata(BaseModel):
    dh_internal: Optional[MetadataDhInternal] = None


class FinetuningResponse(BaseModel):
    id: str

    alias: str

    db_connection_id: str

    base_llm: Optional[BaseLlm] = None

    created_at: Optional[datetime] = None

    error: Optional[str] = None

    finetuning_file_id: Optional[str] = None

    finetuning_job_id: Optional[str] = None

    golden_sqls: Optional[List[str]] = None

    metadata: Optional[Metadata] = None

    api_model_id: Optional[str] = FieldInfo(alias="model_id", default=None)

    status: Optional[str] = None
