# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict

__all__ = ["DatabaseConnectionCreateParams", "SSHSettings"]


class DatabaseConnectionCreateParams(TypedDict, total=False):
    alias: str

    connection_uri: str

    credential_file_content: Union[object, str]

    llm_api_key: str

    metadata: object

    ssh_settings: SSHSettings

    use_ssh: bool


class SSHSettings(TypedDict, total=False):
    db_driver: str

    db_name: str

    host: str

    password: str

    private_key_password: str

    remote_db_name: str

    remote_db_password: str

    remote_host: str

    username: str
