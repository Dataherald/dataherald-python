# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SqlGenerationNlGenerationsParams", "SqlGeneration"]


class SqlGenerationNlGenerationsParams(TypedDict, total=False):
    sql_generation: Required[SqlGeneration]

    max_rows: int

    metadata: object


class SqlGeneration(TypedDict, total=False):
    evaluate: bool

    finetuning_id: str

    low_latency_mode: bool

    metadata: object

    sql: str
