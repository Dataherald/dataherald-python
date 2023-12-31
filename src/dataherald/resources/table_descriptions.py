# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List

import httpx

from ..types import (
    TableDescriptionResponse,
    TableDescriptionListResponse,
    table_description_list_params,
    table_description_update_params,
    table_description_sync_schemas_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import (
    make_request_options,
)

__all__ = ["TableDescriptions", "AsyncTableDescriptions"]


class TableDescriptions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TableDescriptionsWithRawResponse:
        return TableDescriptionsWithRawResponse(self)

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
        columns: List[table_description_update_params.Column] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        examples: List[object] | NotGiven = NOT_GIVEN,
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
        db_connection_id: str,
        table_names: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Api Sync Table Descriptions Schemas

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/table-descriptions/sync-schemas",
            body=maybe_transform(
                {
                    "db_connection_id": db_connection_id,
                    "table_names": table_names,
                },
                table_description_sync_schemas_params.TableDescriptionSyncSchemasParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncTableDescriptions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTableDescriptionsWithRawResponse:
        return AsyncTableDescriptionsWithRawResponse(self)

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
        columns: List[table_description_update_params.Column] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        examples: List[object] | NotGiven = NOT_GIVEN,
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
        return await self._put(
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

    async def sync_schemas(
        self,
        *,
        db_connection_id: str,
        table_names: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Api Sync Table Descriptions Schemas

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/table-descriptions/sync-schemas",
            body=maybe_transform(
                {
                    "db_connection_id": db_connection_id,
                    "table_names": table_names,
                },
                table_description_sync_schemas_params.TableDescriptionSyncSchemasParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class TableDescriptionsWithRawResponse:
    def __init__(self, table_descriptions: TableDescriptions) -> None:
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


class AsyncTableDescriptionsWithRawResponse:
    def __init__(self, table_descriptions: AsyncTableDescriptions) -> None:
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
