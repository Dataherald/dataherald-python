# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["InstructionResponse", "Metadata"]


class Metadata(BaseModel):
    dh_internal: Optional[object] = None


class InstructionResponse(BaseModel):
    id: str

    instruction: str

    created_at: Optional[datetime] = None

    db_connection_id: Optional[str] = None

    metadata: Optional[Metadata] = None
