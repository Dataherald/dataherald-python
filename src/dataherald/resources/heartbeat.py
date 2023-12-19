import httpx
from.._resource import SyncAPIResource
from .._client import Dataherald

class HeartBeat(SyncAPIResource):
    def __init__(self, client: Dataherald):
        super.__init__(client)
        return self.response(200, "OK")