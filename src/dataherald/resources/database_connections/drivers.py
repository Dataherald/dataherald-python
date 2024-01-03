# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..._types import (
    NOT_GIVEN,
    Body,
    Query,
    Headers,
    NotGiven,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.database_connections import DriverListResponse

if TYPE_CHECKING:
    from ..._client import Dataherald, AsyncDataherald

__all__ = ["Drivers", "AsyncDrivers"]


class Drivers(SyncAPIResource):
    with_raw_response: DriversWithRawResponse

    def __init__(self, client: Dataherald) -> None:
        super().__init__(client)
        self.with_raw_response = DriversWithRawResponse(self)

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
    with_raw_response: AsyncDriversWithRawResponse

    def __init__(self, client: AsyncDataherald) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncDriversWithRawResponse(self)

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
        self.list = to_raw_response_wrapper(
            drivers.list,
        )


class AsyncDriversWithRawResponse:
    def __init__(self, drivers: AsyncDrivers) -> None:
        self.list = async_to_raw_response_wrapper(
            drivers.list,
        )