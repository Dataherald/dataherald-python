# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GenerationSqlGenerationParams"]


class GenerationSqlGenerationParams(TypedDict, total=False):
    sql: Required[str]
