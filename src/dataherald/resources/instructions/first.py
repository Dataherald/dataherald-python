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
from ...types.shared import InstructionResponse

if TYPE_CHECKING:
    from ..._client import Dataherald, AsyncDataherald

__all__ = ["First", "AsyncFirst"]


class First(SyncAPIResource):
    with_raw_response: FirstWithRawResponse

    def __init__(self, client: Dataherald) -> None:
        super().__init__(client)
        self.with_raw_response = FirstWithRawResponse(self)

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
    with_raw_response: AsyncFirstWithRawResponse

    def __init__(self, client: AsyncDataherald) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncFirstWithRawResponse(self)

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
        self.retrieve = to_raw_response_wrapper(
            first.retrieve,
        )


class AsyncFirstWithRawResponse:
    def __init__(self, first: AsyncFirst) -> None:
        self.retrieve = async_to_raw_response_wrapper(
            first.retrieve,
        )
