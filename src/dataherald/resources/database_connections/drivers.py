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
from ...types.database_connections import DriverListResponse

__all__ = ["Drivers", "AsyncDrivers"]


class Drivers(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DriversWithRawResponse:
        return DriversWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DriversWithStreamingResponse:
        return DriversWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverListResponse:
        """Api Get Drivers"""
        return self._get(
            "/api/database-connections/drivers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DriverListResponse,
        )


class AsyncDrivers(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDriversWithRawResponse:
        return AsyncDriversWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDriversWithStreamingResponse:
        return AsyncDriversWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverListResponse:
        """Api Get Drivers"""
        return await self._get(
            "/api/database-connections/drivers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DriverListResponse,
        )


class DriversWithRawResponse:
    def __init__(self, drivers: Drivers) -> None:
        self._drivers = drivers

        self.list = to_raw_response_wrapper(
            drivers.list,
        )


class AsyncDriversWithRawResponse:
    def __init__(self, drivers: AsyncDrivers) -> None:
        self._drivers = drivers

        self.list = async_to_raw_response_wrapper(
            drivers.list,
        )


class DriversWithStreamingResponse:
    def __init__(self, drivers: Drivers) -> None:
        self._drivers = drivers

        self.list = to_streamed_response_wrapper(
            drivers.list,
        )


class AsyncDriversWithStreamingResponse:
    def __init__(self, drivers: AsyncDrivers) -> None:
        self._drivers = drivers

        self.list = async_to_streamed_response_wrapper(
            drivers.list,
        )
