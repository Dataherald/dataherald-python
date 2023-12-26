# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["TableDescriptionSyncSchemasParams"]


class TableDescriptionSyncSchemasParams(TypedDict, total=False):
    db_connection_id: Required[str]

    table_names: List[str]
