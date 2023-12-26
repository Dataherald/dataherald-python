# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SqlGenerationCreateParams", "Prompt"]


class SqlGenerationCreateParams(TypedDict, total=False):
    prompt: Required[Prompt]

    evaluate: bool

    finetuning_id: str

    metadata: object

    sql: str


class Prompt(TypedDict, total=False):
    db_connection_id: Required[str]

    text: Required[str]

    metadata: object
