# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InstructionUpdateParams"]


class InstructionUpdateParams(TypedDict, total=False):
    instruction: Required[str]

    db_connection_id: str

    metadata: object
