# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import TypedDict

__all__ = ["TableDescriptionUpdateParams", "Column"]


class TableDescriptionUpdateParams(TypedDict, total=False):
    columns: Iterable[Column]

    description: str

    examples: Iterable[object]

    metadata: object


class Column(TypedDict, total=False):
    categories: List[str]

    data_type: str

    description: str

    foreign_key: object

    is_primary_key: bool

    low_cardinality: bool

    name: str
