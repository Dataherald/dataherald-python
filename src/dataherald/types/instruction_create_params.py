# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InstructionCreateParams"]


class InstructionCreateParams(TypedDict, total=False):
    instruction: Required[str]

    db_connection_id: str

    metadata: object
