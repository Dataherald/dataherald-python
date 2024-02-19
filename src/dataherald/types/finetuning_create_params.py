# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Required, TypedDict

__all__ = ["FinetuningCreateParams", "BaseLlm"]


class FinetuningCreateParams(TypedDict, total=False):
    alias: Required[str]

    base_llm: Required[BaseLlm]

    db_connection_id: Required[str]

    golden_sqls: List[str]

    metadata: object


class BaseLlm(TypedDict, total=False):
    model_name: str

    model_parameters: Dict[str, str]

    model_provider: str
