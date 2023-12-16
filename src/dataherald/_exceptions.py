import httpx
from typing import Any, Optional, cast
from typing_extensions import TypeGuard



#To-Do move these to a utils class
def is_dict(obj: object) -> TypeGuard[dict[object, object]]:
    return isinstance(obj, dict)


class DataheraldError(Exception):
    pass


class APIError(DataheraldError):
    message: str
    request: httpx.Request

    body: object | None
    """The API response body.

    If the API responded with a valid JSON structure then this property will be the
    decoded result.

    If it isn't a valid JSON structure then this will be the raw response.

    If there was no response associated with this error then it will be `None`.
    """

    code: Optional[str]
    param: Optional[str]
    type: Optional[str]

    def __init__(self, message: str, request: httpx.Request, *, body: object | None) -> None:
        super().__init__(message)
        self.request = request
        self.message = message
        self.body = body

        if is_dict(body):
            self.code = cast(Any, body.get("code"))
            self.param = cast(Any, body.get("param"))
            self.type = cast(Any, body.get("type"))
        else:
            self.code = None
            self.param = None
            self.type = None