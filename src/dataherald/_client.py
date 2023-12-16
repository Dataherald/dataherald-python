import httpx

import os
from typing import Union

from . import resources, _exceptions
from ._base_client import DEFAULT_MAX_RETRIES, SyncAPIClient, AsyncAPIClient
from ._types import (
    Timout,
    NotGiven
)

from _exceptions import DataheraldError

class Dataherald(SyncAPIClient):
    sql_generations: resources.SQLGenerations
    nl_generations: resources.NLGenerations
    organization: str | None


    def __init__(
        self,
        timeout: Union[float, None],
        api_key: str = None,
        base_url:str | httpx.URL | None = None,
        organization: str | None = None,
        max_retries: int = DEFAULT_MAX_RETRIES,
     ) -> None:
        """
        Constructs a new synchronous Dataherald client instance

        This will infer the following arguements from the environment variables if they are not provided 
        - `api_key` - `DATAHERALD_API_KEY`
        - `organization` - `DATAHERALD_ORG_ID`
        """ 
        if api_key is None:
            api_key = os.environ.get("DATAHERALD_API_KEY")
        if api_key is None:
            raise DataheraldError(
                "No API key provided. Please provide an API key or set the DATAHERALD_API_KEY environment variable."
            )
        self.api_key = api_key

        if organization is None:
            organization = os.environ.get("OPENAI_ORG_ID")
        self.organization = organization

        if base_url is None:
            base_url = os.environ.get("OPENAI_BASE_URL")
        if base_url is None:
            base_url = f"https://api.dataherald.ai/api/v1"



class AsyncDataherald(AsyncAPIClient):
    pass



