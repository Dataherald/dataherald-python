# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["GenerationUpdateParams"]


class GenerationUpdateParams(TypedDict, total=False):
    generation_status: Literal["INITIALIZED", "IN_PROGRESS", "NOT_VERIFIED", "VERIFIED", "ERROR", "REJECTED"]
    """An enumeration."""

    message: str
