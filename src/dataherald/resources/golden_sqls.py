# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import golden_sql_list_params, golden_sql_upload_params
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
from ..types.golden_sql_list_response import GoldenSqlListResponse
from ..types.golden_sql_upload_response import GoldenSqlUploadResponse
from ..types.shared.golden_sql_response import GoldenSqlResponse

__all__ = ["GoldenSqlsResource", "AsyncGoldenSqlsResource"]


class GoldenSqlsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GoldenSqlsResourceWithRawResponse:
        return GoldenSqlsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GoldenSqlsResourceWithStreamingResponse:
        return GoldenSqlsResourceWithStreamingResponse(self)

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
    ) -> GoldenSqlResponse:
        """
        Api Get Golden Sql

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/golden-sqls/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GoldenSqlResponse,
        )

    def list(
        self,
        *,
        ascend: bool | NotGiven = NOT_GIVEN,
        db_connection_id: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GoldenSqlListResponse:
        """
        Api Get Golden Sqls

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/golden-sqls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ascend": ascend,
                        "db_connection_id": db_connection_id,
                        "order": order,
                        "page": page,
                        "page_size": page_size,
                    },
                    golden_sql_list_params.GoldenSqlListParams,
                ),
            ),
            cast_to=GoldenSqlListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Api Delete Golden Sql

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/golden-sqls/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def upload(
        self,
        *,
        body: Iterable[golden_sql_upload_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GoldenSqlUploadResponse:
        """
        Api Add User Upload Golden Sql

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/golden-sqls",
            body=maybe_transform(body, golden_sql_upload_params.GoldenSqlUploadParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GoldenSqlUploadResponse,
        )


class AsyncGoldenSqlsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGoldenSqlsResourceWithRawResponse:
        return AsyncGoldenSqlsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGoldenSqlsResourceWithStreamingResponse:
        return AsyncGoldenSqlsResourceWithStreamingResponse(self)

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
    ) -> GoldenSqlResponse:
        """
        Api Get Golden Sql

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/golden-sqls/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GoldenSqlResponse,
        )

    async def list(
        self,
        *,
        ascend: bool | NotGiven = NOT_GIVEN,
        db_connection_id: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GoldenSqlListResponse:
        """
        Api Get Golden Sqls

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/golden-sqls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ascend": ascend,
                        "db_connection_id": db_connection_id,
                        "order": order,
                        "page": page,
                        "page_size": page_size,
                    },
                    golden_sql_list_params.GoldenSqlListParams,
                ),
            ),
            cast_to=GoldenSqlListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Api Delete Golden Sql

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/golden-sqls/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def upload(
        self,
        *,
        body: Iterable[golden_sql_upload_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GoldenSqlUploadResponse:
        """
        Api Add User Upload Golden Sql

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/golden-sqls",
            body=await async_maybe_transform(body, golden_sql_upload_params.GoldenSqlUploadParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GoldenSqlUploadResponse,
        )


class GoldenSqlsResourceWithRawResponse:
    def __init__(self, golden_sqls: GoldenSqlsResource) -> None:
        self._golden_sqls = golden_sqls

        self.retrieve = to_raw_response_wrapper(
            golden_sqls.retrieve,
        )
        self.list = to_raw_response_wrapper(
            golden_sqls.list,
        )
        self.delete = to_raw_response_wrapper(
            golden_sqls.delete,
        )
        self.upload = to_raw_response_wrapper(
            golden_sqls.upload,
        )


class AsyncGoldenSqlsResourceWithRawResponse:
    def __init__(self, golden_sqls: AsyncGoldenSqlsResource) -> None:
        self._golden_sqls = golden_sqls

        self.retrieve = async_to_raw_response_wrapper(
            golden_sqls.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            golden_sqls.list,
        )
        self.delete = async_to_raw_response_wrapper(
            golden_sqls.delete,
        )
        self.upload = async_to_raw_response_wrapper(
            golden_sqls.upload,
        )


class GoldenSqlsResourceWithStreamingResponse:
    def __init__(self, golden_sqls: GoldenSqlsResource) -> None:
        self._golden_sqls = golden_sqls

        self.retrieve = to_streamed_response_wrapper(
            golden_sqls.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            golden_sqls.list,
        )
        self.delete = to_streamed_response_wrapper(
            golden_sqls.delete,
        )
        self.upload = to_streamed_response_wrapper(
            golden_sqls.upload,
        )


class AsyncGoldenSqlsResourceWithStreamingResponse:
    def __init__(self, golden_sqls: AsyncGoldenSqlsResource) -> None:
        self._golden_sqls = golden_sqls

        self.retrieve = async_to_streamed_response_wrapper(
            golden_sqls.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            golden_sqls.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            golden_sqls.delete,
        )
        self.upload = async_to_streamed_response_wrapper(
            golden_sqls.upload,
        )
