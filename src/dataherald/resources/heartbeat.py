# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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

__all__ = ["Heartbeat", "AsyncHeartbeat"]


class Heartbeat(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HeartbeatWithRawResponse:
        return HeartbeatWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HeartbeatWithStreamingResponse:
        return HeartbeatWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Heartbeat"""
        return self._get(
            "/heartbeat",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncHeartbeat(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHeartbeatWithRawResponse:
        return AsyncHeartbeatWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHeartbeatWithStreamingResponse:
        return AsyncHeartbeatWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Heartbeat"""
        return await self._get(
            "/heartbeat",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class HeartbeatWithRawResponse:
    def __init__(self, heartbeat: Heartbeat) -> None:
        self._heartbeat = heartbeat

        self.retrieve = to_raw_response_wrapper(
            heartbeat.retrieve,
        )


class AsyncHeartbeatWithRawResponse:
    def __init__(self, heartbeat: AsyncHeartbeat) -> None:
        self._heartbeat = heartbeat

        self.retrieve = async_to_raw_response_wrapper(
            heartbeat.retrieve,
        )


class HeartbeatWithStreamingResponse:
    def __init__(self, heartbeat: Heartbeat) -> None:
        self._heartbeat = heartbeat

        self.retrieve = to_streamed_response_wrapper(
            heartbeat.retrieve,
        )


class AsyncHeartbeatWithStreamingResponse:
    def __init__(self, heartbeat: AsyncHeartbeat) -> None:
        self._heartbeat = heartbeat

        self.retrieve = async_to_streamed_response_wrapper(
            heartbeat.retrieve,
        )
