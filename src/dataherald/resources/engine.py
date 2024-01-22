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

__all__ = ["Engine", "AsyncEngine"]


class Engine(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EngineWithRawResponse:
        return EngineWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EngineWithStreamingResponse:
        return EngineWithStreamingResponse(self)

    def heartbeat(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Engine Heartbeat"""
        return self._get(
            "/engine/heartbeat",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncEngine(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEngineWithRawResponse:
        return AsyncEngineWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEngineWithStreamingResponse:
        return AsyncEngineWithStreamingResponse(self)

    async def heartbeat(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Engine Heartbeat"""
        return await self._get(
            "/engine/heartbeat",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class EngineWithRawResponse:
    def __init__(self, engine: Engine) -> None:
        self._engine = engine

        self.heartbeat = to_raw_response_wrapper(
            engine.heartbeat,
        )


class AsyncEngineWithRawResponse:
    def __init__(self, engine: AsyncEngine) -> None:
        self._engine = engine

        self.heartbeat = async_to_raw_response_wrapper(
            engine.heartbeat,
        )


class EngineWithStreamingResponse:
    def __init__(self, engine: Engine) -> None:
        self._engine = engine

        self.heartbeat = to_streamed_response_wrapper(
            engine.heartbeat,
        )


class AsyncEngineWithStreamingResponse:
    def __init__(self, engine: AsyncEngine) -> None:
        self._engine = engine

        self.heartbeat = async_to_streamed_response_wrapper(
            engine.heartbeat,
        )
