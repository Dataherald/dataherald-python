# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from .first import First, AsyncFirst, FirstWithRawResponse, AsyncFirstWithRawResponse
from ...types import (
    InstructionListResponse,
    instruction_list_params,
    instruction_create_params,
    instruction_update_params,
)
from ..._types import (
    NOT_GIVEN,
    Body,
    Query,
    Headers,
    NotGiven,
    UnknownResponse,
)
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.shared import InstructionResponse

if TYPE_CHECKING:
    from ..._client import Dataherald, AsyncDataherald

__all__ = ["Instructions", "AsyncInstructions"]


class Instructions(SyncAPIResource):
    first: First
    with_raw_response: InstructionsWithRawResponse

    def __init__(self, client: Dataherald) -> None:
        super().__init__(client)
        self.first = First(client)
        self.with_raw_response = InstructionsWithRawResponse(self)

    def create(
        self,
        *,
        instruction: str,
        db_connection_id: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstructionResponse:
        """
        Api Add Instructions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/instructions",
            body=maybe_transform(
                {
                    "instruction": instruction,
                    "db_connection_id": db_connection_id,
                    "metadata": metadata,
                },
                instruction_create_params.InstructionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstructionResponse,
        )

    def update(
        self,
        id: str,
        *,
        instruction: str,
        db_connection_id: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstructionResponse:
        """
        Api Update Instruction

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/api/instructions/{id}",
            body=maybe_transform(
                {
                    "instruction": instruction,
                    "db_connection_id": db_connection_id,
                    "metadata": metadata,
                },
                instruction_update_params.InstructionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstructionResponse,
        )

    def list(
        self,
        *,
        db_connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstructionListResponse:
        """
        Api Get Instructions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/instructions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"db_connection_id": db_connection_id}, instruction_list_params.InstructionListParams
                ),
            ),
            cast_to=InstructionListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Api Delete Instruction

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/api/instructions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnknownResponse,
        )


class AsyncInstructions(AsyncAPIResource):
    first: AsyncFirst
    with_raw_response: AsyncInstructionsWithRawResponse

    def __init__(self, client: AsyncDataherald) -> None:
        super().__init__(client)
        self.first = AsyncFirst(client)
        self.with_raw_response = AsyncInstructionsWithRawResponse(self)

    async def create(
        self,
        *,
        instruction: str,
        db_connection_id: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstructionResponse:
        """
        Api Add Instructions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/instructions",
            body=maybe_transform(
                {
                    "instruction": instruction,
                    "db_connection_id": db_connection_id,
                    "metadata": metadata,
                },
                instruction_create_params.InstructionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstructionResponse,
        )

    async def update(
        self,
        id: str,
        *,
        instruction: str,
        db_connection_id: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstructionResponse:
        """
        Api Update Instruction

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/api/instructions/{id}",
            body=maybe_transform(
                {
                    "instruction": instruction,
                    "db_connection_id": db_connection_id,
                    "metadata": metadata,
                },
                instruction_update_params.InstructionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstructionResponse,
        )

    async def list(
        self,
        *,
        db_connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstructionListResponse:
        """
        Api Get Instructions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/instructions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"db_connection_id": db_connection_id}, instruction_list_params.InstructionListParams
                ),
            ),
            cast_to=InstructionListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Api Delete Instruction

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/api/instructions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnknownResponse,
        )


class InstructionsWithRawResponse:
    def __init__(self, instructions: Instructions) -> None:
        self.first = FirstWithRawResponse(instructions.first)

        self.create = to_raw_response_wrapper(
            instructions.create,
        )
        self.update = to_raw_response_wrapper(
            instructions.update,
        )
        self.list = to_raw_response_wrapper(
            instructions.list,
        )
        self.delete = to_raw_response_wrapper(
            instructions.delete,
        )


class AsyncInstructionsWithRawResponse:
    def __init__(self, instructions: AsyncInstructions) -> None:
        self.first = AsyncFirstWithRawResponse(instructions.first)

        self.create = async_to_raw_response_wrapper(
            instructions.create,
        )
        self.update = async_to_raw_response_wrapper(
            instructions.update,
        )
        self.list = async_to_raw_response_wrapper(
            instructions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            instructions.delete,
        )
