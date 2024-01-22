# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    GenerationResponse,
    GenerationListResponse,
    generation_list_params,
    generation_update_params,
    generation_sql_generation_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
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
from ..types.shared import NlGenerationResponse

__all__ = ["Generations", "AsyncGenerations"]


class Generations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenerationsWithRawResponse:
        return GenerationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerationsWithStreamingResponse:
        return GenerationsWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationResponse:
        """
        Api Create Sql Nl Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/generations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationResponse,
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
    ) -> GenerationResponse:
        """
        Api Get Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/generations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationResponse,
        )

    def update(
        self,
        id: str,
        *,
        generation_status: Literal["INITIALIZED", "IN_PROGRESS", "NOT_VERIFIED", "VERIFIED", "ERROR", "REJECTED"]
        | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationResponse:
        """
        Api Update Generation

        Args:
          generation_status: An enumeration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/api/generations/{id}",
            body=maybe_transform(
                {
                    "generation_status": generation_status,
                    "message": message,
                },
                generation_update_params.GenerationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationResponse,
        )

    def list(
        self,
        *,
        ascend: bool | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationListResponse:
        """
        Api Get Generations

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/generations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ascend": ascend,
                        "order": order,
                        "page": page,
                        "page_size": page_size,
                    },
                    generation_list_params.GenerationListParams,
                ),
            ),
            cast_to=GenerationListResponse,
        )

    def nl_generation(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NlGenerationResponse:
        """
        Api Generate Message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/generations/{id}/nl-generation",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NlGenerationResponse,
        )

    def sql_generation(
        self,
        id: str,
        *,
        sql: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationResponse:
        """
        Api Generate Sql Result

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/generations/{id}/sql-generation",
            body=maybe_transform({"sql": sql}, generation_sql_generation_params.GenerationSqlGenerationParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationResponse,
        )


class AsyncGenerations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenerationsWithRawResponse:
        return AsyncGenerationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerationsWithStreamingResponse:
        return AsyncGenerationsWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationResponse:
        """
        Api Create Sql Nl Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/generations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationResponse,
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
    ) -> GenerationResponse:
        """
        Api Get Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/generations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationResponse,
        )

    async def update(
        self,
        id: str,
        *,
        generation_status: Literal["INITIALIZED", "IN_PROGRESS", "NOT_VERIFIED", "VERIFIED", "ERROR", "REJECTED"]
        | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationResponse:
        """
        Api Update Generation

        Args:
          generation_status: An enumeration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/api/generations/{id}",
            body=maybe_transform(
                {
                    "generation_status": generation_status,
                    "message": message,
                },
                generation_update_params.GenerationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationResponse,
        )

    async def list(
        self,
        *,
        ascend: bool | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationListResponse:
        """
        Api Get Generations

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/generations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ascend": ascend,
                        "order": order,
                        "page": page,
                        "page_size": page_size,
                    },
                    generation_list_params.GenerationListParams,
                ),
            ),
            cast_to=GenerationListResponse,
        )

    async def nl_generation(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NlGenerationResponse:
        """
        Api Generate Message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/generations/{id}/nl-generation",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NlGenerationResponse,
        )

    async def sql_generation(
        self,
        id: str,
        *,
        sql: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationResponse:
        """
        Api Generate Sql Result

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/generations/{id}/sql-generation",
            body=maybe_transform({"sql": sql}, generation_sql_generation_params.GenerationSqlGenerationParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationResponse,
        )


class GenerationsWithRawResponse:
    def __init__(self, generations: Generations) -> None:
        self._generations = generations

        self.create = to_raw_response_wrapper(
            generations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            generations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            generations.update,
        )
        self.list = to_raw_response_wrapper(
            generations.list,
        )
        self.nl_generation = to_raw_response_wrapper(
            generations.nl_generation,
        )
        self.sql_generation = to_raw_response_wrapper(
            generations.sql_generation,
        )


class AsyncGenerationsWithRawResponse:
    def __init__(self, generations: AsyncGenerations) -> None:
        self._generations = generations

        self.create = async_to_raw_response_wrapper(
            generations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            generations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            generations.update,
        )
        self.list = async_to_raw_response_wrapper(
            generations.list,
        )
        self.nl_generation = async_to_raw_response_wrapper(
            generations.nl_generation,
        )
        self.sql_generation = async_to_raw_response_wrapper(
            generations.sql_generation,
        )


class GenerationsWithStreamingResponse:
    def __init__(self, generations: Generations) -> None:
        self._generations = generations

        self.create = to_streamed_response_wrapper(
            generations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            generations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            generations.update,
        )
        self.list = to_streamed_response_wrapper(
            generations.list,
        )
        self.nl_generation = to_streamed_response_wrapper(
            generations.nl_generation,
        )
        self.sql_generation = to_streamed_response_wrapper(
            generations.sql_generation,
        )


class AsyncGenerationsWithStreamingResponse:
    def __init__(self, generations: AsyncGenerations) -> None:
        self._generations = generations

        self.create = async_to_streamed_response_wrapper(
            generations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            generations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            generations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            generations.list,
        )
        self.nl_generation = async_to_streamed_response_wrapper(
            generations.nl_generation,
        )
        self.sql_generation = async_to_streamed_response_wrapper(
            generations.sql_generation,
        )
