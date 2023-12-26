# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SqlGenerationListParams"]


class SqlGenerationListParams(TypedDict, total=False):
    ascend: bool

    order: str

    page: int

    page_size: int
