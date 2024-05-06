# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import (
    table_description_list_params,
    table_description_update_params,
    table_description_sync_schemas_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.table_description_response import TableDescriptionResponse
from ..types.table_description_list_response import TableDescriptionListResponse
from ..types.table_description_sync_schemas_response import TableDescriptionSyncSchemasResponse

__all__ = ["TableDescriptionsResource", "AsyncTableDescriptionsResource"]


class TableDescriptionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TableDescriptionsResourceWithRawResponse:
        return TableDescriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TableDescriptionsResourceWithStreamingResponse:
        return TableDescriptionsResourceWithStreamingResponse(self)

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
    ) -> TableDescriptionResponse:
        """
        Api Get Table Description

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/table-descriptions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TableDescriptionResponse,
        )

    def update(
        self,
        id: str,
        *,
        columns: Iterable[table_description_update_params.Column] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        examples: Iterable[object] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TableDescriptionResponse:
        """
        Api Update Table Description

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/api/table-descriptions/{id}",
            body=maybe_transform(
                {
                    "columns": columns,
                    "description": description,
                    "examples": examples,
                    "metadata": metadata,
                },
                table_description_update_params.TableDescriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TableDescriptionResponse,
        )

    def list(
        self,
        *,
        db_connection_id: str,
        table_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TableDescriptionListResponse:
        """
        Get Table Descriptions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/table-descriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "db_connection_id": db_connection_id,
                        "table_name": table_name,
                    },
                    table_description_list_params.TableDescriptionListParams,
                ),
            ),
            cast_to=TableDescriptionListResponse,
        )

    def sync_schemas(
        self,
        *,
        body: Iterable[table_description_sync_schemas_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TableDescriptionSyncSchemasResponse:
        """
        Sync Table Descriptions Schemas

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/table-descriptions/sync-schemas",
            body=maybe_transform(body, table_description_sync_schemas_params.TableDescriptionSyncSchemasParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TableDescriptionSyncSchemasResponse,
        )


class AsyncTableDescriptionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTableDescriptionsResourceWithRawResponse:
        return AsyncTableDescriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTableDescriptionsResourceWithStreamingResponse:
        return AsyncTableDescriptionsResourceWithStreamingResponse(self)

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
    ) -> TableDescriptionResponse:
        """
        Api Get Table Description

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/table-descriptions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TableDescriptionResponse,
        )

    async def update(
        self,
        id: str,
        *,
        columns: Iterable[table_description_update_params.Column] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        examples: Iterable[object] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TableDescriptionResponse:
        """
        Api Update Table Description

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/api/table-descriptions/{id}",
            body=await async_maybe_transform(
                {
                    "columns": columns,
                    "description": description,
                    "examples": examples,
                    "metadata": metadata,
                },
                table_description_update_params.TableDescriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TableDescriptionResponse,
        )

    async def list(
        self,
        *,
        db_connection_id: str,
        table_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TableDescriptionListResponse:
        """
        Get Table Descriptions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/table-descriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "db_connection_id": db_connection_id,
                        "table_name": table_name,
                    },
                    table_description_list_params.TableDescriptionListParams,
                ),
            ),
            cast_to=TableDescriptionListResponse,
        )

    async def sync_schemas(
        self,
        *,
        body: Iterable[table_description_sync_schemas_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TableDescriptionSyncSchemasResponse:
        """
        Sync Table Descriptions Schemas

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/table-descriptions/sync-schemas",
            body=await async_maybe_transform(
                body, table_description_sync_schemas_params.TableDescriptionSyncSchemasParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TableDescriptionSyncSchemasResponse,
        )


class TableDescriptionsResourceWithRawResponse:
    def __init__(self, table_descriptions: TableDescriptionsResource) -> None:
        self._table_descriptions = table_descriptions

        self.retrieve = to_raw_response_wrapper(
            table_descriptions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            table_descriptions.update,
        )
        self.list = to_raw_response_wrapper(
            table_descriptions.list,
        )
        self.sync_schemas = to_raw_response_wrapper(
            table_descriptions.sync_schemas,
        )


class AsyncTableDescriptionsResourceWithRawResponse:
    def __init__(self, table_descriptions: AsyncTableDescriptionsResource) -> None:
        self._table_descriptions = table_descriptions

        self.retrieve = async_to_raw_response_wrapper(
            table_descriptions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            table_descriptions.update,
        )
        self.list = async_to_raw_response_wrapper(
            table_descriptions.list,
        )
        self.sync_schemas = async_to_raw_response_wrapper(
            table_descriptions.sync_schemas,
        )


class TableDescriptionsResourceWithStreamingResponse:
    def __init__(self, table_descriptions: TableDescriptionsResource) -> None:
        self._table_descriptions = table_descriptions

        self.retrieve = to_streamed_response_wrapper(
            table_descriptions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            table_descriptions.update,
        )
        self.list = to_streamed_response_wrapper(
            table_descriptions.list,
        )
        self.sync_schemas = to_streamed_response_wrapper(
            table_descriptions.sync_schemas,
        )


class AsyncTableDescriptionsResourceWithStreamingResponse:
    def __init__(self, table_descriptions: AsyncTableDescriptionsResource) -> None:
        self._table_descriptions = table_descriptions

        self.retrieve = async_to_streamed_response_wrapper(
            table_descriptions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            table_descriptions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            table_descriptions.list,
        )
        self.sync_schemas = async_to_streamed_response_wrapper(
            table_descriptions.sync_schemas,
        )
