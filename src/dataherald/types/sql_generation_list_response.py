# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.sql_generation_response import SqlGenerationResponse

__all__ = ["SqlGenerationListResponse"]

SqlGenerationListResponse: TypeAlias = List[SqlGenerationResponse]
