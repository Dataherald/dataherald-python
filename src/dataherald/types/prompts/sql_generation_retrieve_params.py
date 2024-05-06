# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SqlGenerationRetrieveParams"]


class SqlGenerationRetrieveParams(TypedDict, total=False):
    ascend: bool

    order: str

    page: int

    page_size: int
