# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
from ...types.shared.instruction_response import InstructionResponse

__all__ = ["FirstResource", "AsyncFirstResource"]


class FirstResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FirstResourceWithRawResponse:
        return FirstResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FirstResourceWithStreamingResponse:
        return FirstResourceWithStreamingResponse(self)

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


class AsyncFirstResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFirstResourceWithRawResponse:
        return AsyncFirstResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFirstResourceWithStreamingResponse:
        return AsyncFirstResourceWithStreamingResponse(self)

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


class FirstResourceWithRawResponse:
    def __init__(self, first: FirstResource) -> None:
        self._first = first

        self.retrieve = to_raw_response_wrapper(
            first.retrieve,
        )


class AsyncFirstResourceWithRawResponse:
    def __init__(self, first: AsyncFirstResource) -> None:
        self._first = first

        self.retrieve = async_to_raw_response_wrapper(
            first.retrieve,
        )


class FirstResourceWithStreamingResponse:
    def __init__(self, first: FirstResource) -> None:
        self._first = first

        self.retrieve = to_streamed_response_wrapper(
            first.retrieve,
        )


class AsyncFirstResourceWithStreamingResponse:
    def __init__(self, first: AsyncFirstResource) -> None:
        self._first = first

        self.retrieve = async_to_streamed_response_wrapper(
            first.retrieve,
        )
