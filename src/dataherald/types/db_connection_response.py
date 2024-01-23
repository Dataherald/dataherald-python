# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["DBConnectionResponse", "Metadata", "MetadataDataheraldInternal", "SSHSettings"]


class MetadataDataheraldInternal(BaseModel):
    organization_id: Optional[str] = None


class Metadata(BaseModel):
    dataherald_internal: Optional[MetadataDataheraldInternal] = None


class SSHSettings(BaseModel):
    host: Optional[str] = None

    password: Optional[str] = None

    private_key_password: Optional[str] = None

    username: Optional[str] = None


class DBConnectionResponse(BaseModel):
    alias: str

    connection_uri: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    llm_api_key: Optional[str] = None

    metadata: Optional[Metadata] = None

    path_to_credentials_file: Optional[str] = None

    ssh_settings: Optional[SSHSettings] = None

    use_ssh: Optional[bool] = None
