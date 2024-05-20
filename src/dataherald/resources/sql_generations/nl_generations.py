# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ...types.sql_generations import nl_generation_create_params, nl_generation_retrieve_params
from ...types.shared.nl_generation_response import NlGenerationResponse

__all__ = ["NlGenerationsResource", "AsyncNlGenerationsResource"]


class NlGenerationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NlGenerationsResourceWithRawResponse:
        return NlGenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NlGenerationsResourceWithStreamingResponse:
        return NlGenerationsResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        max_rows: int | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NlGenerationResponse:
        """
        Create Nl Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/sql-generations/{id}/nl-generations",
            body=maybe_transform(
                {
                    "max_rows": max_rows,
                    "metadata": metadata,
                },
                nl_generation_create_params.NlGenerationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NlGenerationResponse,
        )

    def retrieve(
        self,
        id: str,
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
    ) -> object:
        """
        Get Nl Generations By Sql Generation Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/sql-generations/{id}/nl-generations",
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
                    nl_generation_retrieve_params.NlGenerationRetrieveParams,
                ),
            ),
            cast_to=object,
        )


class AsyncNlGenerationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNlGenerationsResourceWithRawResponse:
        return AsyncNlGenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNlGenerationsResourceWithStreamingResponse:
        return AsyncNlGenerationsResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        max_rows: int | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NlGenerationResponse:
        """
        Create Nl Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/sql-generations/{id}/nl-generations",
            body=await async_maybe_transform(
                {
                    "max_rows": max_rows,
                    "metadata": metadata,
                },
                nl_generation_create_params.NlGenerationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NlGenerationResponse,
        )

    async def retrieve(
        self,
        id: str,
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
    ) -> object:
        """
        Get Nl Generations By Sql Generation Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/sql-generations/{id}/nl-generations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ascend": ascend,
                        "order": order,
                        "page": page,
                        "page_size": page_size,
                    },
                    nl_generation_retrieve_params.NlGenerationRetrieveParams,
                ),
            ),
            cast_to=object,
        )


class NlGenerationsResourceWithRawResponse:
    def __init__(self, nl_generations: NlGenerationsResource) -> None:
        self._nl_generations = nl_generations

        self.create = to_raw_response_wrapper(
            nl_generations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            nl_generations.retrieve,
        )


class AsyncNlGenerationsResourceWithRawResponse:
    def __init__(self, nl_generations: AsyncNlGenerationsResource) -> None:
        self._nl_generations = nl_generations

        self.create = async_to_raw_response_wrapper(
            nl_generations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            nl_generations.retrieve,
        )


class NlGenerationsResourceWithStreamingResponse:
    def __init__(self, nl_generations: NlGenerationsResource) -> None:
        self._nl_generations = nl_generations

        self.create = to_streamed_response_wrapper(
            nl_generations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            nl_generations.retrieve,
        )


class AsyncNlGenerationsResourceWithStreamingResponse:
    def __init__(self, nl_generations: AsyncNlGenerationsResource) -> None:
        self._nl_generations = nl_generations

        self.create = async_to_streamed_response_wrapper(
            nl_generations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            nl_generations.retrieve,
        )
