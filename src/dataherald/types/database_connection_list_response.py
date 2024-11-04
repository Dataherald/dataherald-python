# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .db_connection_response import DBConnectionResponse

__all__ = ["DatabaseConnectionListResponse"]

DatabaseConnectionListResponse: TypeAlias = List[DBConnectionResponse]
