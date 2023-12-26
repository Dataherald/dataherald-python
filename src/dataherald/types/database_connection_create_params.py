# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["DatabaseConnectionCreateParams"]


class DatabaseConnectionCreateParams(TypedDict, total=False):
    db_connection_request_json: Required[str]

    file: FileTypes
