# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NlGenerationCreateParams", "SqlGeneration", "SqlGenerationPrompt"]


class NlGenerationCreateParams(TypedDict, total=False):
    sql_generation: Required[SqlGeneration]

    max_rows: int

    metadata: object


class SqlGenerationPrompt(TypedDict, total=False):
    db_connection_id: Required[str]

    text: Required[str]

    metadata: object


class SqlGeneration(TypedDict, total=False):
    prompt: Required[SqlGenerationPrompt]

    evaluate: bool

    finetuning_id: str

    metadata: object

    sql: str
