# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["DBConnectionResponse", "Metadata", "MetadataDataheraldInternal", "SshSettings"]


class MetadataDataheraldInternal(BaseModel):
    organization_id: Optional[str] = None


class Metadata(BaseModel):
    dataherald_internal: Optional[MetadataDataheraldInternal] = None


class SshSettings(BaseModel):
    db_driver: Optional[str] = None

    db_name: Optional[str] = None

    host: Optional[str] = None

    password: Optional[str] = None

    private_key_password: Optional[str] = None

    remote_db_name: Optional[str] = None

    remote_db_password: Optional[str] = None

    remote_host: Optional[str] = None

    username: Optional[str] = None


class DBConnectionResponse(BaseModel):
    id: str

    alias: Optional[str] = None

    created_at: Optional[datetime] = None

    llm_api_key: Optional[str] = None

    metadata: Optional[Metadata] = None

    path_to_credentials_file: Optional[str] = None

    ssh_settings: Optional[SshSettings] = None

    uri: Optional[str] = None

    use_ssh: Optional[bool] = None
