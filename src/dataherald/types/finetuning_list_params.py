# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FinetuningListParams"]


class FinetuningListParams(TypedDict, total=False):
    db_connection_id: Required[str]
