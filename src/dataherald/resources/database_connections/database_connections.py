# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union

import httpx

from ...types import (
    DBConnectionResponse,
    DatabaseConnectionListResponse,
    database_connection_create_params,
    database_connection_update_params,
)
from .drivers import (
    Drivers,
    AsyncDrivers,
    DriversWithRawResponse,
    AsyncDriversWithRawResponse,
    DriversWithStreamingResponse,
    AsyncDriversWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["DatabaseConnections", "AsyncDatabaseConnections"]


class DatabaseConnections(SyncAPIResource):
    @cached_property
    def drivers(self) -> Drivers:
        return Drivers(self._client)

    @cached_property
    def with_raw_response(self) -> DatabaseConnectionsWithRawResponse:
        return DatabaseConnectionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatabaseConnectionsWithStreamingResponse:
        return DatabaseConnectionsWithStreamingResponse(self)

    def create(
        self,
        *,
        alias: str,
        connection_uri: str,
        bigquery_credential_file_content: Union[object, str] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        sqlite_file_path: str | NotGiven = NOT_GIVEN,
        ssh_settings: database_connection_create_params.SSHSettings | NotGiven = NOT_GIVEN,
        use_ssh: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DBConnectionResponse:
        """
        Add Db Connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/database-connections",
            body=maybe_transform(
                {
                    "alias": alias,
                    "connection_uri": connection_uri,
                    "bigquery_credential_file_content": bigquery_credential_file_content,
                    "metadata": metadata,
                    "sqlite_file_path": sqlite_file_path,
                    "ssh_settings": ssh_settings,
                    "use_ssh": use_ssh,
                },
                database_connection_create_params.DatabaseConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DBConnectionResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DBConnectionResponse:
        """
        Api Get Db Connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/database-connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DBConnectionResponse,
        )

    def update(
        self,
        id: str,
        *,
        alias: str,
        connection_uri: str,
        bigquery_credential_file_content: Union[object, str] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        sqlite_file_path: str | NotGiven = NOT_GIVEN,
        ssh_settings: database_connection_update_params.SSHSettings | NotGiven = NOT_GIVEN,
        use_ssh: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DBConnectionResponse:
        """
        Update Db Connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/api/database-connections/{id}",
            body=maybe_transform(
                {
                    "alias": alias,
                    "connection_uri": connection_uri,
                    "bigquery_credential_file_content": bigquery_credential_file_content,
                    "metadata": metadata,
                    "sqlite_file_path": sqlite_file_path,
                    "ssh_settings": ssh_settings,
                    "use_ssh": use_ssh,
                },
                database_connection_update_params.DatabaseConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DBConnectionResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseConnectionListResponse:
        """Get Db Connections"""
        return self._get(
            "/api/database-connections",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatabaseConnectionListResponse,
        )


class AsyncDatabaseConnections(AsyncAPIResource):
    @cached_property
    def drivers(self) -> AsyncDrivers:
        return AsyncDrivers(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatabaseConnectionsWithRawResponse:
        return AsyncDatabaseConnectionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatabaseConnectionsWithStreamingResponse:
        return AsyncDatabaseConnectionsWithStreamingResponse(self)

    async def create(
        self,
        *,
        alias: str,
        connection_uri: str,
        bigquery_credential_file_content: Union[object, str] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        sqlite_file_path: str | NotGiven = NOT_GIVEN,
        ssh_settings: database_connection_create_params.SSHSettings | NotGiven = NOT_GIVEN,
        use_ssh: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DBConnectionResponse:
        """
        Add Db Connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/database-connections",
            body=maybe_transform(
                {
                    "alias": alias,
                    "connection_uri": connection_uri,
                    "bigquery_credential_file_content": bigquery_credential_file_content,
                    "metadata": metadata,
                    "sqlite_file_path": sqlite_file_path,
                    "ssh_settings": ssh_settings,
                    "use_ssh": use_ssh,
                },
                database_connection_create_params.DatabaseConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DBConnectionResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DBConnectionResponse:
        """
        Api Get Db Connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/database-connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DBConnectionResponse,
        )

    async def update(
        self,
        id: str,
        *,
        alias: str,
        connection_uri: str,
        bigquery_credential_file_content: Union[object, str] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        sqlite_file_path: str | NotGiven = NOT_GIVEN,
        ssh_settings: database_connection_update_params.SSHSettings | NotGiven = NOT_GIVEN,
        use_ssh: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DBConnectionResponse:
        """
        Update Db Connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/api/database-connections/{id}",
            body=maybe_transform(
                {
                    "alias": alias,
                    "connection_uri": connection_uri,
                    "bigquery_credential_file_content": bigquery_credential_file_content,
                    "metadata": metadata,
                    "sqlite_file_path": sqlite_file_path,
                    "ssh_settings": ssh_settings,
                    "use_ssh": use_ssh,
                },
                database_connection_update_params.DatabaseConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DBConnectionResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseConnectionListResponse:
        """Get Db Connections"""
        return await self._get(
            "/api/database-connections",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatabaseConnectionListResponse,
        )


class DatabaseConnectionsWithRawResponse:
    def __init__(self, database_connections: DatabaseConnections) -> None:
        self._database_connections = database_connections

        self.create = to_raw_response_wrapper(
            database_connections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            database_connections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            database_connections.update,
        )
        self.list = to_raw_response_wrapper(
            database_connections.list,
        )

    @cached_property
    def drivers(self) -> DriversWithRawResponse:
        return DriversWithRawResponse(self._database_connections.drivers)


class AsyncDatabaseConnectionsWithRawResponse:
    def __init__(self, database_connections: AsyncDatabaseConnections) -> None:
        self._database_connections = database_connections

        self.create = async_to_raw_response_wrapper(
            database_connections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            database_connections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            database_connections.update,
        )
        self.list = async_to_raw_response_wrapper(
            database_connections.list,
        )

    @cached_property
    def drivers(self) -> AsyncDriversWithRawResponse:
        return AsyncDriversWithRawResponse(self._database_connections.drivers)


class DatabaseConnectionsWithStreamingResponse:
    def __init__(self, database_connections: DatabaseConnections) -> None:
        self._database_connections = database_connections

        self.create = to_streamed_response_wrapper(
            database_connections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            database_connections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            database_connections.update,
        )
        self.list = to_streamed_response_wrapper(
            database_connections.list,
        )

    @cached_property
    def drivers(self) -> DriversWithStreamingResponse:
        return DriversWithStreamingResponse(self._database_connections.drivers)


class AsyncDatabaseConnectionsWithStreamingResponse:
    def __init__(self, database_connections: AsyncDatabaseConnections) -> None:
        self._database_connections = database_connections

        self.create = async_to_streamed_response_wrapper(
            database_connections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            database_connections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            database_connections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            database_connections.list,
        )

    @cached_property
    def drivers(self) -> AsyncDriversWithStreamingResponse:
        return AsyncDriversWithStreamingResponse(self._database_connections.drivers)
