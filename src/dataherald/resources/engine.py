# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from .._types import (
    NOT_GIVEN,
    Body,
    Query,
    Headers,
    NotGiven,
    UnknownResponse,
)
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import (
    make_request_options,
)

if TYPE_CHECKING:
    from .._client import Dataherald, AsyncDataherald

__all__ = ["Engine", "AsyncEngine"]


class Engine(SyncAPIResource):
    with_raw_response: EngineWithRawResponse

    def __init__(self, client: Dataherald) -> None:
        super().__init__(client)
        self.with_raw_response = EngineWithRawResponse(self)

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
            cast_to=UnknownResponse,
        )


class AsyncEngine(AsyncAPIResource):
    with_raw_response: AsyncEngineWithRawResponse

    def __init__(self, client: AsyncDataherald) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncEngineWithRawResponse(self)

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
            cast_to=UnknownResponse,
        )


class EngineWithRawResponse:
    def __init__(self, engine: Engine) -> None:
        self.heartbeat = to_raw_response_wrapper(
            engine.heartbeat,
        )


class AsyncEngineWithRawResponse:
    def __init__(self, engine: AsyncEngine) -> None:
        self.heartbeat = async_to_raw_response_wrapper(
            engine.heartbeat,
        )
