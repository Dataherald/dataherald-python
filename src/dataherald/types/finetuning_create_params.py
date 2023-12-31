# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Required, TypedDict

__all__ = ["FinetuningCreateParams", "BaseLlm"]


class FinetuningCreateParams(TypedDict, total=False):
    db_connection_id: Required[str]

    alias: str

    base_llm: BaseLlm

    golden_records: List[str]

    metadata: object


class BaseLlm(TypedDict, total=False):
    _model_name: str

    _model_parameters: Dict[str, str]

    _model_provider: str
