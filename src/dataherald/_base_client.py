from typing import (
    Generic, 
    TypeVar, 
    Union
) 

_HttpxClientT = TypeVar("_HttpxClientT", bound=Union[httpx.Client, httpx.AsyncClient])


class BaseClient(Generic[_HttpxClientT]):

class SyncAPIClient(BaseClient[httpx.Client]):
    _client: httpx.Client

    def __init__():
        super().__init__()
    


class AsyncAPIClient(BaseClient[httpx.AsyncClient]):
    _client: httpx.AsyncClient

    def __init__():
        super().__init__()