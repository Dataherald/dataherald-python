# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DriverResponse"]


class DriverResponse(BaseModel):
    driver: str

    name: Optional[str] = None
