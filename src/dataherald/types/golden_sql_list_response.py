# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.golden_sql_response import GoldenSqlResponse

__all__ = ["GoldenSqlListResponse"]

GoldenSqlListResponse: TypeAlias = List[GoldenSqlResponse]
