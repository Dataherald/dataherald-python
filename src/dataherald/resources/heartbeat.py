# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, UnknownResponse
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import Dataherald, AsyncDataherald

__all__ = ["Heartbeat", "AsyncHeartbeat"]


class Heartbeat(SyncAPIResource):
    with_raw_response: HeartbeatWithRawResponse

    def __init__(self, client: Dataherald) -> None:
        super().__init__(client)
        self.with_raw_response = HeartbeatWithRawResponse(self)

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
            cast_to=UnknownResponse,
        )


class AsyncHeartbeat(AsyncAPIResource):
    with_raw_response: AsyncHeartbeatWithRawResponse

    def __init__(self, client: AsyncDataherald) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncHeartbeatWithRawResponse(self)

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
            cast_to=UnknownResponse,
        )


class HeartbeatWithRawResponse:
    def __init__(self, heartbeat: Heartbeat) -> None:
        self.retrieve = to_raw_response_wrapper(
            heartbeat.retrieve,
        )


class AsyncHeartbeatWithRawResponse:
    def __init__(self, heartbeat: AsyncHeartbeat) -> None:
        self.retrieve = async_to_raw_response_wrapper(
            heartbeat.retrieve,
        )
