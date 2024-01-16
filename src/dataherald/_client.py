# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, DataheraldError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Dataherald",
    "AsyncDataherald",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.dataherald.ai/",
    "staging": "https://stage.api.dataherald.ai/",
}


class Dataherald(SyncAPIClient):
    database_connections: resources.DatabaseConnections
    finetunings: resources.Finetunings
    golden_sqls: resources.GoldenSqls
    instructions: resources.Instructions
    generations: resources.Generations
    prompts: resources.Prompts
    sql_generations: resources.SqlGenerations
    nl_generations: resources.NlGenerations
    table_descriptions: resources.TableDescriptions
    heartbeat: resources.Heartbeat
    engine: resources.Engine
    with_raw_response: DataheraldWithRawResponse
    with_streaming_response: DataheraldWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "staging"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Dataherald client instance.

        This automatically infers the `api_key` argument from the `DATAHERALD_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("DATAHERALD_API_KEY")
        if api_key is None:
            raise DataheraldError(
                "The api_key client option must be set either by passing api_key to the client or by setting the DATAHERALD_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("DATAHERALD_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `DATAHERALD_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.database_connections = resources.DatabaseConnections(self)
        self.finetunings = resources.Finetunings(self)
        self.golden_sqls = resources.GoldenSqls(self)
        self.instructions = resources.Instructions(self)
        self.generations = resources.Generations(self)
        self.prompts = resources.Prompts(self)
        self.sql_generations = resources.SqlGenerations(self)
        self.nl_generations = resources.NlGenerations(self)
        self.table_descriptions = resources.TableDescriptions(self)
        self.heartbeat = resources.Heartbeat(self)
        self.engine = resources.Engine(self)
        self.with_raw_response = DataheraldWithRawResponse(self)
        self.with_streaming_response = DataheraldWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncDataherald(AsyncAPIClient):
    database_connections: resources.AsyncDatabaseConnections
    finetunings: resources.AsyncFinetunings
    golden_sqls: resources.AsyncGoldenSqls
    instructions: resources.AsyncInstructions
    generations: resources.AsyncGenerations
    prompts: resources.AsyncPrompts
    sql_generations: resources.AsyncSqlGenerations
    nl_generations: resources.AsyncNlGenerations
    table_descriptions: resources.AsyncTableDescriptions
    heartbeat: resources.AsyncHeartbeat
    engine: resources.AsyncEngine
    with_raw_response: AsyncDataheraldWithRawResponse
    with_streaming_response: AsyncDataheraldWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "staging"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async Dataherald client instance.

        This automatically infers the `api_key` argument from the `DATAHERALD_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("DATAHERALD_API_KEY")
        if api_key is None:
            raise DataheraldError(
                "The api_key client option must be set either by passing api_key to the client or by setting the DATAHERALD_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("DATAHERALD_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `DATAHERALD_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.database_connections = resources.AsyncDatabaseConnections(self)
        self.finetunings = resources.AsyncFinetunings(self)
        self.golden_sqls = resources.AsyncGoldenSqls(self)
        self.instructions = resources.AsyncInstructions(self)
        self.generations = resources.AsyncGenerations(self)
        self.prompts = resources.AsyncPrompts(self)
        self.sql_generations = resources.AsyncSqlGenerations(self)
        self.nl_generations = resources.AsyncNlGenerations(self)
        self.table_descriptions = resources.AsyncTableDescriptions(self)
        self.heartbeat = resources.AsyncHeartbeat(self)
        self.engine = resources.AsyncEngine(self)
        self.with_raw_response = AsyncDataheraldWithRawResponse(self)
        self.with_streaming_response = AsyncDataheraldWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class DataheraldWithRawResponse:
    def __init__(self, client: Dataherald) -> None:
        self.database_connections = resources.DatabaseConnectionsWithRawResponse(client.database_connections)
        self.finetunings = resources.FinetuningsWithRawResponse(client.finetunings)
        self.golden_sqls = resources.GoldenSqlsWithRawResponse(client.golden_sqls)
        self.instructions = resources.InstructionsWithRawResponse(client.instructions)
        self.generations = resources.GenerationsWithRawResponse(client.generations)
        self.prompts = resources.PromptsWithRawResponse(client.prompts)
        self.sql_generations = resources.SqlGenerationsWithRawResponse(client.sql_generations)
        self.nl_generations = resources.NlGenerationsWithRawResponse(client.nl_generations)
        self.table_descriptions = resources.TableDescriptionsWithRawResponse(client.table_descriptions)
        self.heartbeat = resources.HeartbeatWithRawResponse(client.heartbeat)
        self.engine = resources.EngineWithRawResponse(client.engine)


class AsyncDataheraldWithRawResponse:
    def __init__(self, client: AsyncDataherald) -> None:
        self.database_connections = resources.AsyncDatabaseConnectionsWithRawResponse(client.database_connections)
        self.finetunings = resources.AsyncFinetuningsWithRawResponse(client.finetunings)
        self.golden_sqls = resources.AsyncGoldenSqlsWithRawResponse(client.golden_sqls)
        self.instructions = resources.AsyncInstructionsWithRawResponse(client.instructions)
        self.generations = resources.AsyncGenerationsWithRawResponse(client.generations)
        self.prompts = resources.AsyncPromptsWithRawResponse(client.prompts)
        self.sql_generations = resources.AsyncSqlGenerationsWithRawResponse(client.sql_generations)
        self.nl_generations = resources.AsyncNlGenerationsWithRawResponse(client.nl_generations)
        self.table_descriptions = resources.AsyncTableDescriptionsWithRawResponse(client.table_descriptions)
        self.heartbeat = resources.AsyncHeartbeatWithRawResponse(client.heartbeat)
        self.engine = resources.AsyncEngineWithRawResponse(client.engine)


class DataheraldWithStreamedResponse:
    def __init__(self, client: Dataherald) -> None:
        self.database_connections = resources.DatabaseConnectionsWithStreamingResponse(client.database_connections)
        self.finetunings = resources.FinetuningsWithStreamingResponse(client.finetunings)
        self.golden_sqls = resources.GoldenSqlsWithStreamingResponse(client.golden_sqls)
        self.instructions = resources.InstructionsWithStreamingResponse(client.instructions)
        self.generations = resources.GenerationsWithStreamingResponse(client.generations)
        self.prompts = resources.PromptsWithStreamingResponse(client.prompts)
        self.sql_generations = resources.SqlGenerationsWithStreamingResponse(client.sql_generations)
        self.nl_generations = resources.NlGenerationsWithStreamingResponse(client.nl_generations)
        self.table_descriptions = resources.TableDescriptionsWithStreamingResponse(client.table_descriptions)
        self.heartbeat = resources.HeartbeatWithStreamingResponse(client.heartbeat)
        self.engine = resources.EngineWithStreamingResponse(client.engine)


class AsyncDataheraldWithStreamedResponse:
    def __init__(self, client: AsyncDataherald) -> None:
        self.database_connections = resources.AsyncDatabaseConnectionsWithStreamingResponse(client.database_connections)
        self.finetunings = resources.AsyncFinetuningsWithStreamingResponse(client.finetunings)
        self.golden_sqls = resources.AsyncGoldenSqlsWithStreamingResponse(client.golden_sqls)
        self.instructions = resources.AsyncInstructionsWithStreamingResponse(client.instructions)
        self.generations = resources.AsyncGenerationsWithStreamingResponse(client.generations)
        self.prompts = resources.AsyncPromptsWithStreamingResponse(client.prompts)
        self.sql_generations = resources.AsyncSqlGenerationsWithStreamingResponse(client.sql_generations)
        self.nl_generations = resources.AsyncNlGenerationsWithStreamingResponse(client.nl_generations)
        self.table_descriptions = resources.AsyncTableDescriptionsWithStreamingResponse(client.table_descriptions)
        self.heartbeat = resources.AsyncHeartbeatWithStreamingResponse(client.heartbeat)
        self.engine = resources.AsyncEngineWithStreamingResponse(client.engine)


Client = Dataherald

AsyncClient = AsyncDataherald
