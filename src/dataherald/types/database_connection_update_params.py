# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["DatabaseConnectionUpdateParams", "SSHSettings"]


class DatabaseConnectionUpdateParams(TypedDict, total=False):
    alias: Required[str]

    connection_uri: Required[str]

    bigquery_credential_file_content: Union[object, str]

    metadata: object

    sqlite_file_path: str

    ssh_settings: SSHSettings

    use_ssh: bool


class SSHSettings(TypedDict, total=False):
    host: str

    password: str

    username: str
