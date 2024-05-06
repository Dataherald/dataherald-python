# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["DatabaseConnectionCreateParams", "SSHSettings"]


class DatabaseConnectionCreateParams(TypedDict, total=False):
    alias: Required[str]

    connection_uri: Required[str]

    bigquery_credential_file_content: Union[str, object]

    metadata: object

    sqlite_file_path: str

    ssh_settings: SSHSettings

    use_ssh: bool


class SSHSettings(TypedDict, total=False):
    host: str

    password: str

    username: str
