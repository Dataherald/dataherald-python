# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.shared import InstructionResponse

__all__ = ["First", "AsyncFirst"]


class First(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FirstWithRawResponse:
        return FirstWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FirstWithStreamingResponse:
        return FirstWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstructionResponse:
        """Api Get First Instruction"""
        return self._get(
            "/api/instructions/first",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstructionResponse,
        )


class AsyncFirst(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFirstWithRawResponse:
        return AsyncFirstWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFirstWithStreamingResponse:
        return AsyncFirstWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstructionResponse:
        """Api Get First Instruction"""
        return await self._get(
            "/api/instructions/first",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstructionResponse,
        )


class FirstWithRawResponse:
    def __init__(self, first: First) -> None:
        self._first = first

        self.retrieve = to_raw_response_wrapper(
            first.retrieve,
        )


class AsyncFirstWithRawResponse:
    def __init__(self, first: AsyncFirst) -> None:
        self._first = first

        self.retrieve = async_to_raw_response_wrapper(
            first.retrieve,
        )


class FirstWithStreamingResponse:
    def __init__(self, first: First) -> None:
        self._first = first

        self.retrieve = to_streamed_response_wrapper(
            first.retrieve,
        )


class AsyncFirstWithStreamingResponse:
    def __init__(self, first: AsyncFirst) -> None:
        self._first = first

        self.retrieve = async_to_streamed_response_wrapper(
            first.retrieve,
        )
