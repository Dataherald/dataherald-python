# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["GoldenSqlUserUploadParams", "Body"]


class GoldenSqlUserUploadParams(TypedDict, total=False):
    body: Required[List[Body]]


class Body(TypedDict, total=False):
    db_connection_id: Required[str]

    prompt_text: Required[str]

    sql: Required[str]

    metadata: object
