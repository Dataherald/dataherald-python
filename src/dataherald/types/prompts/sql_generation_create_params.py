# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SqlGenerationCreateParams"]


class SqlGenerationCreateParams(TypedDict, total=False):
    evaluate: bool

    finetuning_id: str

    metadata: object

    sql: str
