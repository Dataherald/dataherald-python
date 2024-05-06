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
from ...types.database_connections.driver_list_response import DriverListResponse

__all__ = ["DriversResource", "AsyncDriversResource"]


class DriversResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DriversResourceWithRawResponse:
        return DriversResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DriversResourceWithStreamingResponse:
        return DriversResourceWithStreamingResponse(self)

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


class AsyncDriversResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDriversResourceWithRawResponse:
        return AsyncDriversResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDriversResourceWithStreamingResponse:
        return AsyncDriversResourceWithStreamingResponse(self)

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


class DriversResourceWithRawResponse:
    def __init__(self, drivers: DriversResource) -> None:
        self._drivers = drivers

        self.list = to_raw_response_wrapper(
            drivers.list,
        )


class AsyncDriversResourceWithRawResponse:
    def __init__(self, drivers: AsyncDriversResource) -> None:
        self._drivers = drivers

        self.list = async_to_raw_response_wrapper(
            drivers.list,
        )


class DriversResourceWithStreamingResponse:
    def __init__(self, drivers: DriversResource) -> None:
        self._drivers = drivers

        self.list = to_streamed_response_wrapper(
            drivers.list,
        )


class AsyncDriversResourceWithStreamingResponse:
    def __init__(self, drivers: AsyncDriversResource) -> None:
        self._drivers = drivers

        self.list = async_to_streamed_response_wrapper(
            drivers.list,
        )
